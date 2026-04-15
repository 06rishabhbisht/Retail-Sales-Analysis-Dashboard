import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    return pd.read_csv('Retail and wherehouse Sale.csv')

def clean_data(df):
    # Drop rows with missing critical values (if any)
    df = df.dropna(subset=['RETAIL SALES'], how='any')

    # Fill missing values in non-critical columns
    df.loc[:, 'SUPPLIER'] = df['SUPPLIER'].fillna('Unknown')
    df.loc[:, 'ITEM TYPE'] = df['ITEM TYPE'].fillna('Unknown')

    df = df.drop_duplicates()

    for col in ['RETAIL SALES', 'RETAIL TRANSFERS', 'WAREHOUSE SALES']:
        df[col] = df[col].apply(lambda x: max(x, 0))

    return df

def engineer_features(df, standardize=False):
    # Add total sales if not already present
    if 'TOTAL SALES' not in df.columns:
        df['TOTAL SALES'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

    # Add log-transformed sales for distribution plot
    df['LOG_TOTAL_SALES'] = np.log1p(df['TOTAL SALES'])

    # Create transfer ratio feature
    df['TRANSFER_RATIO'] = (df['RETAIL TRANSFERS'] + 1) / (df['RETAIL SALES'] + 1)

    # Optional: Standardize numeric features
    if standardize:
        scaler = StandardScaler()
        cols_to_scale = ['RETAIL SALES', 'RETAIL TRANSFERS', 'WAREHOUSE SALES', 'TOTAL SALES']
        df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    return df

def preprocess(filepath, standardize=False):
    df = load_data(filepath)
    df = clean_data(df)
    df = engineer_features(df, standardize)
    return df


