# visualization.py
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import squarify
from pandas.plotting import scatter_matrix

output_dir = "assets"
os.makedirs(output_dir, exist_ok=True)

def plot_top_categories_treemap(df):
    category_sales = df.groupby("ITEM TYPE")["RETAIL SALES"].sum().sort_values(ascending=False)
    category_sales = category_sales[category_sales > 0]
    labels = [f"{cat}\n${val:,.0f}" for cat, val in zip(category_sales.index, category_sales.values)]
    cmap = plt.get_cmap('Set3')
    colors = [cmap(i / len(category_sales)) for i in range(len(category_sales))]

    plt.figure(figsize=(12, 7))
    squarify.plot(sizes=category_sales.values, label=labels, color=colors, alpha=0.8)
    plt.title("Top Product Categories by Retail Revenue")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_categories_by_revenue_treemap.png")
    plt.close()

def plot_sku_sales_distribution(df):
    sku_sales = df.groupby("ITEM CODE")["RETAIL SALES"].sum()
    plt.figure(figsize=(10, 6))
    sns.histplot(np.log1p(sku_sales), bins=50, kde=True)
    plt.title("Log Distribution of Retail Sales per SKU")
    plt.xlabel("Log(Retail Sales + 1)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/sku_sales_distribution.png")
    plt.close()

def plot_zero_sales_by_item_type(df):
    zero_sales = df[df['RETAIL SALES'] == 0]['ITEM TYPE'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=zero_sales.values, y=zero_sales.index, ax=ax)
    ax.set_title("Zero Retail Sales by Item Type")
    ax.set_xlabel("Count")
    ax.set_ylabel("Item Type")
    for i, v in enumerate(zero_sales.values):
        ax.text(v + 0.5, i, str(v), va='center')
    fig.tight_layout()
    fig.savefig(f"{output_dir}/zero_retail_by_type.png")
    plt.close()

def plot_boxplot_warehouse_sales(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="ITEM TYPE", y="WAREHOUSE SALES")
    plt.title("Warehouse Sales by Item Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/boxplot_warehouse_sales.png")
    plt.close()

def plot_retail_by_supplier(df):
    top_suppliers = df.groupby("SUPPLIER")["RETAIL SALES"].sum().sort_values(ascending=False).head(10).index
    top_df = df[df["SUPPLIER"].isin(top_suppliers)]
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="SUPPLIER", y="RETAIL SALES", data=top_df)
    plt.xticks(rotation=45)
    plt.title("Retail Sales by Top Suppliers")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/boxplot_retail_by_supplier.png")
    plt.close()

def plot_supplier_itemtype_bar(df):
    count = df.groupby("SUPPLIER")["ITEM TYPE"].nunique().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=count.values, y=count.index, palette="mako")
    plt.title("Top Suppliers by Item Type Diversity")
    plt.xlabel("Number of Unique Item Types")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/supplier_itemtype_bar_chart.png")
    plt.close()

def plot_supplier_itemtype_heatmap(df):
    pivot = df.pivot_table(index="SUPPLIER", columns="ITEM TYPE", values="RETAIL SALES", aggfunc="sum", fill_value=0)
    pivot = pivot.loc[pivot.sum(axis=1).sort_values(ascending=False).head(10).index]
    annot_data = pivot.applymap(lambda x: f"{int(x)}" if x > 0 else "")
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, cmap="YlGnBu", annot=annot_data, fmt="", linewidths=0.5)
    plt.title("Supplier vs Item Type Revenue Heatmap")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/supplier_itemtype_heatmap.png")
    plt.close()

def plot_retail_vs_warehouse_sales(df):
    monthly = df.groupby("MONTH")[["RETAIL SALES", "WAREHOUSE SALES"]].sum().reset_index()
    x = np.arange(len(monthly))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, monthly["RETAIL SALES"], width, label="Retail", color="skyblue")
    plt.bar(x + width/2, monthly["WAREHOUSE SALES"], width, label="Warehouse", color="orange")
    plt.xticks(ticks=x, labels=monthly["MONTH"])
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Retail vs Warehouse Sales by Month")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/retail_vs_warehouse_sales.png")
    plt.close()

def plot_transfer_ratio_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df["TRANSFER_RATIO"], bins=50, kde=True, color="purple")
    plt.title("Distribution of Transfer-to-Sales Ratio")
    plt.xlabel("Transfer Ratio")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/transfer_ratio_distribution.png")
    plt.close()

def plot_scatter_matrix(df):
    plt.figure(figsize=(8, 8))
    scatter_matrix(df[["RETAIL SALES", "RETAIL TRANSFERS", "WAREHOUSE SALES"]], alpha=0.5, figsize=(10, 10), diagonal='kde')
    plt.suptitle("Scatter Matrix of Sales Channels")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/scatter_matrix_sales.png")
    plt.close()

def plot_pareto_distribution(df):
    sku_sales = df.groupby("ITEM CODE")["RETAIL SALES"].sum().sort_values(ascending=False)
    cum_sales = sku_sales.cumsum() / sku_sales.sum()
    plt.figure(figsize=(10, 6))
    plt.plot(cum_sales.values, label="Cumulative Share")
    plt.axhline(0.8, color="r", linestyle="--", label="80% Threshold")
    plt.title("Pareto Distribution of Retail Sales by SKU")
    plt.xlabel("SKU Rank")
    plt.ylabel("Cumulative Sales Share")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/pareto_distribution.png")
    plt.close()

def plot_monthly_retail_sales(df):
    monthly = df.groupby("MONTH")["RETAIL SALES"].sum()
    plt.figure(figsize=(10, 6))
    bars = plt.bar(monthly.index.astype(str), monthly.values, color="teal")
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{int(height)}", ha='center', va='bottom')
    plt.title("Monthly Retail Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Retail Sales")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/monthly_retail_sales.png")
    plt.close()

def plot_top_supplier_trend(df):
    top_suppliers = df.groupby("SUPPLIER")["RETAIL SALES"].sum().sort_values(ascending=False).head(5).index
    subset = df[df["SUPPLIER"].isin(top_suppliers)]
    monthly = subset.groupby(["MONTH", "SUPPLIER"])[["RETAIL SALES", "WAREHOUSE SALES"]].sum().reset_index()
    pivot = monthly.pivot(index="MONTH", columns="SUPPLIER")[["RETAIL SALES", "WAREHOUSE SALES"]]

    months = pivot.index
    suppliers = top_suppliers

    bar_width = 0.08
    x = np.arange(len(months))

    plt.figure(figsize=(14, 7))
    for i, supplier in enumerate(suppliers):
        retail_vals = pivot["RETAIL SALES"][supplier].values
        warehouse_vals = pivot["WAREHOUSE SALES"][supplier].values

        plt.bar(x + i * 2 * bar_width, retail_vals, width=bar_width, label=f"{supplier} (Retail)")
        plt.bar(x + (i * 2 + 1) * bar_width, warehouse_vals, width=bar_width, label=f"{supplier} (Warehouse)", alpha=0.7)

    plt.xticks(x + bar_width * len(suppliers), months)
    plt.title("Supplier Sales Trend Comparison")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_supplier_sales_comparison_bar.png")
    plt.close()

def plot_average_transfers_by_item_type(df):
    transfer_avg = df.groupby("ITEM TYPE")["RETAIL TRANSFERS"].mean().sort_values()
    plt.figure(figsize=(10, 6))
    transfer_avg.plot(kind='barh', color='orchid')
    plt.title("Average Transfers by Item Type")
    plt.xlabel("Average Transfers")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/average_transfers_by_item_type.png")
    plt.close()

def plot_supplier_performance(df):
    supplier_perf = df.groupby("SUPPLIER").agg({
        "RETAIL SALES": "sum",
        "ITEM CODE": "count"
    }).rename(columns={"ITEM CODE": "ITEM COUNT"}).reset_index()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=supplier_perf, x="ITEM COUNT", y="RETAIL SALES", hue="RETAIL SALES",
                    size="RETAIL SALES", palette="viridis", legend=False)
    plt.title("Supplier Performance Overview")
    plt.xlabel("Number of Items Supplied")
    plt.ylabel("Total Retail Sales")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/supplier_performance.png")
    plt.close()

def plot_underperforming_products(df):
    underperforming = df[(df["RETAIL SALES"] < df["RETAIL SALES"].median()) &
                         (df["RETAIL TRANSFERS"] > df["RETAIL TRANSFERS"].median())]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="RETAIL SALES", y="RETAIL TRANSFERS", alpha=0.3, label="All Products")
    sns.scatterplot(data=underperforming, x="RETAIL SALES", y="RETAIL TRANSFERS", color="red", label="Underperformers")
    plt.axvline(df["RETAIL SALES"].median(), color="green", linestyle="--", label="Median Retail Sales")
    plt.axhline(df["RETAIL TRANSFERS"].median(), color="blue", linestyle="--", label="Median Transfers")
    plt.title("Underperforming Products: Low Sales, High Transfers")
    plt.xlabel("Retail Sales")
    plt.ylabel("Retail Transfers")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/underperforming_products.png")
    plt.close()

def generate_all_insights(df):
    plot_top_categories_treemap(df)
    plot_sku_sales_distribution(df)
    plot_zero_sales_by_item_type(df)
    plot_boxplot_warehouse_sales(df)
    plot_retail_by_supplier(df)
    plot_supplier_itemtype_bar(df)
    plot_supplier_itemtype_heatmap(df)
    plot_top_supplier_trend(df)
    plot_retail_vs_warehouse_sales(df)
    plot_transfer_ratio_distribution(df)
    plot_scatter_matrix(df)
    plot_pareto_distribution(df)
    plot_monthly_retail_sales(df)
    plot_average_transfers_by_item_type(df)
    plot_supplier_performance(df)
    plot_underperforming_products(df)
