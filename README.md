# Media Mix Modeling (MMM)

## Project Overview
The objective of this project is to statistically analyze the impact of various marketing channels on overall sales. This is achieved through the development of a Media Mix Model (MMM) using historical data from Google Ads and Google Analytics 4 (GA4). The MMM helps in understanding the contribution of each marketing channel to sales and optimizing future marketing strategies.

## Data Sources
- **Google Ads Data**: Campaign performance metrics including costs, clicks, and impressions
- **Google Analytics 4 (GA4)**: User behavior and conversion data across different channels

## Data Processing & Methodology

### Data Cleaning and Preprocessing
- **Campaign Performance Data**:
  - Removed unnecessary columns (Currency code, CTR, Avg. CPC, etc.)
  - Standardized date formats
  - Converted string dates to datetime format
  - Ensured data consistency and integrity
  - Removed any duplicate or irrelevant data
  - Handled missing values appropriately
  - Ensured data types are appropriate for analysis
  - Checked for outliers and anomalies
  - Added derived metrics (CPC, CTR, MoM changes)

- **Google Analytics (GA4) Data**:
  - Created date components (Year, Month, Day)
  - Aggregated metrics by channel, year, and month
  - Calculated engagement rates
  - Focused on key channels:
    - Organic Search
    - Paid Search
    - Direct Traffic
    - Organic Shopping
    - Organic Social
    - Organic Video
    - Paid Shopping
    - Paid Other

### Analysis Focus
The analysis primarily concentrates on 2023-2024 data due to:
- Data recency and relevance to current market conditions
- Complete and consistent GA4 data availability
- More reliable comparison between channels
- Better reflection of current marketing strategies

## Key Findings
- **Correlation Analysis**:
  - Cross-network correlation with PPC costs shows moderate positive relationship (0.46)
  - No evidence of cannibalization between paid and organic search channels
  - Multiple channel relationships observed:
    - Paid Search to Cost: 0.82 (strong positive correlation)
    - Organic Search to Cost: 0.31 (moderate positive correlation)
    - Direct Traffic to Cost: 0.28 (weak positive correlation)
    - Cross-network: 0.46 (moderate positive correlation)
    - Organic Shopping to Cost: 0.25 (weak positive correlation)
    - Organic Social to Cost: 0.22 (weak positive correlation)
    - Organic Video to Cost: 0.18 (weak positive correlation)
    - Paid Shopping to Cost: 0.16 (weak positive correlation)
    - Paid Other to Cost: 0.17 (weak positive correlation)

## Project Structure
```
├── Resources/
│   ├── Campaign performance.csv
│   ├── cleaned_google_ads_data.csv
│   ├── cleaned_google_analytics_data.csv
│   └── channel_analysis_results.csv
├── google_ads_cleaning.py
├── media-mix-model.ipynb
└── README.md
```

## Dependencies
- Python 3.12+
- pandas
- numpy
- matplotlib
- seaborn
- pathlib

## Usage
1. Ensure all required dependencies are installed
2. Place raw data files in the Resources directory
3. Run the data cleaning script:
   ```python
   python google_ads_cleaning.py
   ```
4. Open and run the Jupyter notebook:
   ```bash
   jupyter notebook media-mix-model.ipynb
   ```

## Future Improvements
- Implementation of advanced statistical models
- Addition of seasonal adjustment factors
- Integration of external factors (market conditions, competitors)
- Development of predictive capabilities
- Automation of data collection and processing

