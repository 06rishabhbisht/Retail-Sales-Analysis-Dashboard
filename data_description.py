import pandas as pd
import numpy as np

# Load dataset
def load_data(filepath):
    return pd.read_csv(filepath)

# Show basic statistics
def dataset_statistics(df):
    print("\nDataset Info")
    print(df.info())
    print("\nDescriptive Statistics")
    print(df.describe(include='all'))

# Check missing values
def check_missing_values(df):
    print("\nMissing Values")
    print(df.isnull().sum())

# Check duplicates
def check_duplicates(df):
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")
    return duplicates

# Full report pipeline
def dataset_description(filepath):
    df = load_data(filepath)
    dataset_statistics(df)
    check_missing_values(df)
    check_duplicates(df)
    return df;


filepath = "data\Retail and wherehouse Sale.csv"
dataset_description(filepath)
