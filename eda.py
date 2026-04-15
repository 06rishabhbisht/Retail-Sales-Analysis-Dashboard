import pandas as pd
import numpy as np

def get_summary_statistics(df):
    return df.describe(include='all')

def count_missing_values(df):
    return df.isnull().sum()

def identify_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers.index.tolist()

def calculate_pareto_distribution(df, sales_col='TOTAL SALES'):
    sales = df.groupby('ITEM CODE')[sales_col].sum().sort_values(ascending=False)
    cumulative_share = sales.cumsum() / sales.sum()
    return cumulative_share

def sku_sales_distribution(df):
    return np.log1p(df['TOTAL SALES'])

def transfer_ratio_analysis(df):
    return df['TRANSFER_RATIO'].describe()

def category_sales_summary(df):
    return df.groupby('ITEM TYPE')['TOTAL SALES'].sum().sort_values(ascending=False)

def supplier_itemtype_matrix(df):
    return df.groupby(['SUPPLIER', 'ITEM TYPE']).size().unstack(fill_value=0)

def monthly_sales_summary(df):
    return df.groupby('MONTH')['RETAIL SALES'].sum().sort_index()
