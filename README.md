# Cs4140Project

## Purpose Of Project
For our project, **Climate Patterns**, we are investigating climate change by analyzing global climate data from 1990 to 2018. We aim to apply a variety of clustering and similarity techniques learned in class to find significant trends and anomalies that highlight the many impacts of climate change. By making use of data mining methods we have discussed this semester, we aim to identify patterns that correlate with major environmental factors such as deforestation, greenhouse gas emissions (Methane and CO2), and extreme global temperatures.

## Data Being Used
**CO2 Emissions:** https://www.kaggle.com/datasets/ulrikthygepedersen/co2-emissions-by-country  
**Methane Emissions:** https://www.kaggle.com/datasets/kkhandekar/methane-emissions-across-the-world-19902018  
**Deforestation and Forest Loss:** https://www.kaggle.com/datasets/chiticariucristian/deforestation-and-forest-loss  
**Global Warming Trends:** https://www.kaggle.com/datasets/jawadawan/global-warming-trends-1961-2022

## Updates
### 03/14/2025
Refactor `change_point_anomalies.py` to:
- Compute the LLR ratio for each country
  - A higher observed LLR indicates a stronger anomaly 
- Run permutation testing because we do not know $\mu$ well enough to sample
- Resample to calculate p-values
- Filter by significant anomalies (p-value < 0.05)
- Sort the results by LLR ration in descending order

Currently, this works for `co2_emissions.csv` and `surface_temperature.csv`. `methane_emissions.csv` and `net_forest.csv` are a work in progress.