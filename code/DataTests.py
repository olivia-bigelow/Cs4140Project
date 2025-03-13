#data opening tests
import os
import pandas as pd

# Get the absolute path to the 'data' folder
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "co2_emissions.csv")

# Read the CSV file
emissions = pd.read_csv(data_path)
print(emissions.head())

# Read the CSV file
methane = pd.read_csv(os.path.join(base_dir, "data", "methane_emissions.csv"))
print(methane.head())

# Read the CSV file
forest = pd.read_csv(os.path.join(base_dir, "data", "net_forest.csv"))
print(forest.head())

# Read the CSV file
surface = pd.read_csv(os.path.join(base_dir, "data", "surface_temperature.csv"))
print(surface.head())

