import pandas as pd
import numpy as np
from pathlib import Path
import logging
from datetime import datetime

def setup_logging():
    """Configure logging for the data cleaning process"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def clean_numeric_string(value):
    """Clean strings containing numbers with commas"""
    if isinstance(value, str):
        return float(value.replace(',', ''))
    return value

def parse_month(month_str):
    """Convert month string (e.g., '21-Jan') to numeric month"""
    try:
        # If it's already a number, return it
        return int(month_str)
    except ValueError:
        try:
            # Parse date string and extract month number
            date = datetime.strptime(month_str, '%y-%b')
            return date.month
        except ValueError:
            logging.error(f"Could not parse month: {month_str}")
            return None

def clean_google_ads_data(input_file: str, output_file: str):
    """
    Clean and process Google Ads data according to project requirements
    """
    logging.info(f"Starting Google Ads data cleaning process")
    
    try:
        # Read the raw data
        df = pd.read_csv(input_file)
        logging.info(f"Loaded {len(df)} rows from {input_file}")
        
        # Store original column names for reference
        original_columns = df.columns.tolist()
        logging.info(f"Original columns: {original_columns}")
        
        # Drop unnecessary columns
        columns_to_drop = ['Currency code', 'CTR', 'Avg. CPC', 
                          'Conversions', 'Conv. rate', 'Revenue']
        df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
        
        # Clean numeric columns
        df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')
        df['Clicks'] = df['Clicks'].apply(clean_numeric_string)
        df['Impr.'] = df['Impr.'].apply(clean_numeric_string)
        
        # Clean and convert Month column
        df['Month'] = df['Month'].apply(parse_month)
        
        # Validate data types
        df['Year'] = df['Year'].astype(int)
        df['Month'] = df['Month'].astype(int)
        
        # Add derived metrics
        df['CPC'] = df['Cost'] / df['Clicks']
        df['CTR'] = (df['Clicks'] / df['Impr.'] * 100).round(2)
        
        # Perform data validation
        validation_results = {
            'Missing values': df.isnull().sum(),
            'Negative values': {
                col: (df[col] < 0).sum() 
                for col in ['Cost', 'Clicks', 'Impr.']
            },
            'Zero impressions': (df['Impr.'] == 0).sum(),
            'Invalid CPC': (df['CPC'] <= 0).sum()
        }
        
        # Log validation results
        logging.info("\nData Validation Results:")
        for check, result in validation_results.items():
            logging.info(f"\n{check}:")
            logging.info(result)
        
        # Add date column for time series analysis
        df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(Day=1))
        
        # Calculate month-over-month changes
        df['MoM_Cost_Change'] = df['Cost'].pct_change()
        df['MoM_Clicks_Change'] = df['Clicks'].pct_change()
        
        # Sort by date
        df = df.sort_values('Date')
        
        # Generate summary statistics
        summary_stats = {
            'Monthly averages': df.groupby(['Year', 'Month']).agg({
                'Cost': 'mean',
                'Clicks': 'mean',
                'Impr.': 'mean',
                'CPC': 'mean'
            }).round(2),
            
            'Yearly totals': df.groupby('Year').agg({
                'Cost': 'sum',
                'Clicks': 'sum',
                'Impr.': 'sum'
            }).round(2)
        }
        
        # Log summary statistics
        logging.info("\nSummary Statistics:")
        for metric, data in summary_stats.items():
            logging.info(f"\n{metric}:")
            logging.info(data)
        
        # Save cleaned data
        df.to_csv(output_file, index=False)
        logging.info(f"\nCleaned data saved to {output_file}")
        
        return df, summary_stats
        
    except Exception as e:
        logging.error(f"Error during data cleaning: {str(e)}")
        raise