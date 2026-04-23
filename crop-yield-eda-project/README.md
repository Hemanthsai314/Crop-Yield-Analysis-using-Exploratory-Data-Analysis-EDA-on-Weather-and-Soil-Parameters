# Exploratory Analysis of Crop Yield in Relation to Weather and Soil Parameters

This repository contains a mini-project on **Exploratory Data Analysis (EDA)** for studying the relationship between **crop yield** and **weather/soil parameters** such as rainfall, temperature, soil pH, and nutrients.

## Project Objective
The goal of this project is to analyze how environmental and soil-related factors affect agricultural productivity and to generate insights that can support data-driven farming decisions.

## Problem Addressed
Agriculture is highly sensitive to climatic and environmental changes. Farmers and planners often need better insights into how rainfall, temperature, and soil conditions influence crop yield. This project addresses that need through exploratory data analysis.

## Method Used
- Data collection from crop yield, weather, and soil datasets
- Data cleaning and preprocessing
- Statistical summary analysis
- Correlation analysis
- Visualization using histograms, boxplots, scatter plots, and heatmaps

## Key Findings
- Rainfall and temperature can strongly influence crop productivity.
- Soil characteristics such as pH and nutrient levels also affect yield.
- EDA helps identify trends, regional differences, and variable relationships.

## Repository Structure
```text
crop-yield-eda-project/
├── data/
│   └── sample_crop_yield.csv
├── docs/
│   └── crop_yield_research_paper.pdf
├── notebooks/
│   └── crop_yield_eda.ipynb
├── results/
│   └── figures_tables.md
├── src/
│   └── eda_analysis.py
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Dataset Columns
Expected dataset columns:
- `Region`
- `Season`
- `Crop`
- `Yield`
- `Rainfall`
- `Temperature`
- `Soil_pH`
- `Nutrients`

You can replace the sample dataset with your original dataset.

## Installation
```bash
pip install -r requirements.txt
```

## Run the analysis
```bash
python src/eda_analysis.py
```

## Outputs
The script creates:
- summary statistics
- correlation matrix
- plots in the `results/` folder

## Suggested GitHub Repository Name
`crop-yield-eda-project`

## Author
HemanthSai
