import numpy as np
import pandas as pd

# TODO: finish this data cleaning script
# Need to figure out how to handle missing values properly

def load_data(filepath):
    """Load CSV data"""
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """Clean the dataset"""
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values - NOT SURE HOW TO DO THIS YET
    # Should I use mean? median? drop them?
    
    # TODO: normalize numerical columns
    
    return df

def analyze_data(df):
    """Perform basic analysis"""
    # Calculate summary statistics
    print(df.describe())
    
    # TODO: add correlation analysis
    # TODO: create visualizations
    

if __name__ == "__main__":
    # FIXME: hardcoded path, need to make this configurable
    data = load_data("data.csv")
    cleaned = clean_data(data)
    # analyze_data(cleaned)  # commented out because it crashes
