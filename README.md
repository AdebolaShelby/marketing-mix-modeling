# Media Mix Modeling (MMM)

## Project Overview
* This Media Mix Modeling (MMM) project analyzes the impact of various marketing channels on overall sales using historical data from Google Ads and Google Analytics 4 (GA4). The model helps understand channel contributions to sales and optimize marketing strategies through advanced statistical analysis and machine learning techniques.

## Data Sources
- **Google Ads Data**: Campaign performance metrics (costs, clicks, impressions)
- **Google Analytics 4 (GA4)**: User behavior and conversion data across channels

## Technical Implementation

### Data Processing & Methodology
#### Data Cleaning and Preprocessing
- **Campaign Performance Data**:
  - Column optimization and standardization
  - Date format standardization
  - Data integrity checks
  - Outlier detection and handling
  - Derived metrics calculation (CPC, CTR, MoM changes)

- **Google Analytics (GA4) Data**:
  - Temporal component extraction
  - Channel-based aggregation
  - Engagement metric calculation
  - Channel categorization and standardization

### Feature Engineering

#### Temporal Features
- **DayOfWeek**: Weekly pattern capture (0-6)
- **Quarter**: Seasonal trend identification (1-4)

#### Lagged Features
Historical pattern capture:
- **Sessions_Lag_{1,3,6}**: Previous months' session counts
- **Revenue_Lag_{1,3,6}**: Previous months' revenue
Purpose:
- Short-term effect analysis (1 month)
- Seasonal pattern identification (3 months)
- Long-term trend analysis (6 months)

#### Rolling Window Features
Trend capture and noise reduction:
- **Sessions_Rolling_3m**: 3-month session moving average
- **Sessions_Rolling_6m**: 6-month session moving average
Benefits:
- Outlier impact reduction
- Trend identification
- Seasonal fluctuation smoothing

#### Market Dynamics
- **Market_Share**: Revenue proportion analysis
  - Channel performance relativity
  - Market condition consideration
  - Channel dominance identification

#### Seasonal Indicators
- **IsHoliday**: Key period identification
  - Black Friday period
  - December holiday season
  - Seasonal performance spikes

### Model Performance & Analysis
Multiple modeling approaches implemented:
- Linear Regression (R² Score: 0.185)
- Random Forest (R² Score: 0.775)
- XGBoost
- LightGBM

#### Feature Importance Analysis
Comprehensive feature analysis including:
- Individual feature importance rankings
- Feature group contribution analysis
- Correlation analysis between features
- Cumulative importance curves
- Feature importance visualizations:
  - Bar plots of feature importance
  - Cumulative importance plots
  - Correlation matrices
- Highly correlated feature identification (>0.8 threshold)

#### Feature Importance (Random Forest)
1. Market_Share: 37.15%
2. Revenue_Lag_1: 20.95%
3. Revenue_Lag_6: 14.35%
4. Sessions_Lag_6: 4.85%
5. Sessions_Lag_1: 4.29%
6. Other features: <4% each

### Channel Analysis
#### Correlation Analysis
- Cross-network to PPC costs: 0.46 (moderate positive)
- Channel-specific correlations:
  - Paid Search: 0.82 (strong positive)
  - Organic Search: 0.31 (moderate positive)
  - Direct Traffic: 0.28 (weak positive)
  - Organic Shopping: 0.25 (weak positive)
  - Organic Social: 0.22 (weak positive)
  - Other channels: <0.20 (weak positive)

### Attribution Analysis

#### Overview
The attribution model analyzes how different marketing channels contribute to overall revenue generation. The analysis shows the following channel contributions:

#### Channel Attribution Results
- Organic Search: 36.21%
- Direct: 30.77%
- Paid Search: 26.54%
- Cross-network: 3.30%
- Organic Social: 2.48%
- Other channels: <1% each

#### Attribution Methodology

1. **Revenue-based Attribution**
   - Calculates each channel's contribution based on direct revenue generation
   - Considers both immediate and assisted conversions
   - Weights contributions based on revenue magnitude

2. **Budget Optimization**
   Based on attribution results, the model recommends budget allocation:
   - Organic Search: Highest investment priority ($2.56M recommended)
   - Other channels: Maintain minimal investment until performance improves

3. **Channel Performance Metrics**
   - Revenue per Session
   - Conversion rates
   - Engagement metrics
   - Return on Ad Spend (ROAS)

#### Key Insights

**High-Impact Channels**
1. **Organic Search (36.21%)**
   - Highest revenue contribution
   - Best long-term ROI
   - Recommended for increased investment

2. **Direct Traffic (30.77%)**
   - Strong brand recognition indicator
   - High conversion rate
   - Stable revenue source

3. **Paid Search (26.54%)**
   - Immediate revenue impact
   - Controllable scale
   - Good for short-term goals

#### Performance Analysis
- Channel efficiency metrics
- Cost per acquisition
- Customer lifetime value
- Attribution window analysis

#### Visualization Components
- Channel attribution pie charts
- Revenue trend analysis
- Channel performance comparisons
- ROI visualization
- Budget allocation recommendations

## Project Structure
```
├── Resources/
│   ├── Campaign performance.csv
│   ├── cleaned_google_ads_data.csv
│   ├── cleaned_google_analytics_data.csv
│   ├── channel_analysis_results.csv
│   └── mmm_analysis_results.json
├── google_ads_cleaning.py
├── media-mix-model.ipynb
└── README.md
```

## Analysis Outputs
- Channel Performance Matrix
- Time Series Decomposition
- Attribution Modeling
- Budget Optimization
- Interactive Visualizations:
  - Channel revenue trends
  - Engagement rate analysis
  - ROAS tracking
  - Model performance comparison
  - Feature importance plots
  - Correlation matrices
  - Cumulative importance curves

## Dependencies
- Python 3.12+
- pandas
- numpy
- matplotlib
- pathlib
- scikit-learn
- xgboost
- lightgbm
- statsmodels

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place raw data files in Resources directory
3. Run data cleaning:
   ```python
   python google_ads_cleaning.py
   ```
4. Execute analysis:
   ```bash
   jupyter notebook media-mix-model.ipynb
   ```

## Results
Analysis results (`mmm_analysis_results.json`):
- Model performance metrics
- Channel attribution analysis
- Budget allocation recommendations
- Feature importance rankings
- Time series analysis
- Feature correlation analysis
- Group importance analysis

## Future Enhancements
1. Model Improvements:
   - Advanced statistical models
   - Seasonal adjustment refinement
   - External factor integration
   - Predictive capability enhancement

2. Process Automation:
   - Data collection automation
   - Real-time monitoring
   - Alert system implementation
   - API integration

3. Analysis Enhancement:
   - Advanced visualization capabilities
   - Cross-channel attribution
   - Budget optimization algorithms
   - Competitive analysis integration
   - Feature interaction analysis
   - Automated feature selection



