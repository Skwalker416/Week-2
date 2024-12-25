# Telecom Data Analysis and Dashboard

## Overview
This project is part of the 10 Academy AI Mastery Week 2 challenge. The goal is to analyze telecom data to provide actionable insights for improving user engagement, user experience, and customer satisfaction. Additionally, a dashboard was developed to visualize insights for stakeholders in a user-friendly manner.

## Objectives
1. **User Overview Analysis**: Analyze user behavior, identify popular handsets, and provide insights for marketing strategies.
2. **User Engagement Analysis**: Assess user engagement levels through metrics like session frequency, session duration, and data traffic.
3. **User Experience Analysis**: Evaluate network performance metrics (e.g., TCP retransmission, RTT, throughput) and device characteristics to understand user experience.
4. **Customer Satisfaction Analysis**: Derive satisfaction scores using engagement and experience metrics and predict satisfaction levels.
5. **Dashboard Development**: Create a Streamlit-based interactive dashboard to visualize all insights and KPIs.

## Project Implementation
### Features
- **Data Cleaning & Transformation**: Missing values and outliers were treated using appropriate imputation techniques.
- **EDA (Exploratory Data Analysis)**: Insightful univariate, bivariate, and correlation analyses were performed to understand data relationships.
- **Clustering**: K-means clustering was used for segmenting users based on engagement, experience, and satisfaction metrics.
- **Dimensionality Reduction**: PCA was used to simplify data dimensions while preserving significant information.
- **Regression Modeling**: A predictive model was built to forecast customer satisfaction scores.
- **SQL Integration**: Results were stored in a MySQL database for easy access and further use.
- **Dashboard**: A user-friendly dashboard with pages for each analysis and interactive plots was developed using Streamlit.

### Repository Structure
```plaintext
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       ├── unittests.yml
├── src/
│   ├── data_cleaning.py
│   ├── clustering.py
│   ├── regression.py
│   ├── dashboard.py
│   └── utils.py
├── tests/
│   ├── test_data_cleaning.py
│   ├── test_clustering.py
│   └── test_regression.py
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   └── clustering_analysis.ipynb
├── requirements.txt
├── README.md
├── Dockerfile
├── dashboard.py
└── LICENSE
