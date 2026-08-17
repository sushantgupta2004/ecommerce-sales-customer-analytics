import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "ecommerce_sales.csv", parse_dates=["Order_Date"])

print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("\n--- KPIs ---")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order_ID"].nunique())
print("Total Customers:", df["Customer_ID"].nunique())
print("Average Order Value:", round(df["Sales"].mean(), 2))

print("\n--- Category Performance ---")
print(df.groupby("Category")[["Sales","Profit"]].sum().sort_values("Sales", ascending=False))

print("\n--- Regional Performance ---")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\n--- Top Products ---")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10))
