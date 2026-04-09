# trendpulse-roshnara
Mini Project 1

# TrendPulse — Real-Time Data Pipeline Project

TrendPulse is a Python-based data pipeline that fetches live trending data from HackerNews, processes it, performs analysis, and visualizes insights.

---

## Project Overview

This project is divided into 4 stages:

1. **Data Collection**
   - Fetches top trending stories using HackerNews API
   - Categorizes them into:
     - Technology
     - World News
     - Sports
     - Science
     - Entertainment

2. **Data Processing**
   - Cleans missing or inconsistent data
   - Converts JSON data into structured CSV format

3. **Data Analysis**
   - Performs analysis using Pandas
   - Extracts insights like:
     - Top posts
     - Average score per category
     - Most active authors

4. **Data Visualization**
   - Visualizes data using Matplotlib
   - Generates charts for:
     - Category distribution
     - Score trends
     - Comment distribution

---

##  Project Structure

```
trendpulse-roshnara/
│
├── data/
│   ├── trends_YYYYMMDD.json
│   └── trends_cleaned.csv
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
│
├── requirements.txt
└── README.md
```
