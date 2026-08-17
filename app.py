import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "ecommerce_sales.csv", parse_dates=["Order_Date"])

st.set_page_config(page_title="E-Commerce Analytics", page_icon="📊", layout="wide")
st.title("📊 E-Commerce Sales & Customer Analytics")
st.caption("Interactive portfolio dashboard built with Python and Streamlit.")

with st.sidebar:
    st.header("Filters")
    categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    regions = st.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))

filtered = df[df["Category"].isin(categories) & df["Region"].isin(regions)].copy()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Sales", f"₹{filtered['Sales'].sum():,.0f}")
c2.metric("Total Profit", f"₹{filtered['Profit'].sum():,.0f}")
c3.metric("Orders", f"{filtered['Order_ID'].nunique():,}")
c4.metric("Customers", f"{filtered['Customer_ID'].nunique():,}")

st.subheader("Monthly Sales")
monthly = filtered.assign(Month=filtered["Order_Date"].dt.to_period("M").astype(str)).groupby("Month")["Sales"].sum()
st.line_chart(monthly)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Sales by Category")
    st.bar_chart(filtered.groupby("Category")["Sales"].sum().sort_values(ascending=False))
with col2:
    st.subheader("Sales by Region")
    st.bar_chart(filtered.groupby("Region")["Sales"].sum().sort_values(ascending=False))

st.subheader("Top 10 Products")
st.dataframe(
    filtered.groupby("Product").agg(
        Sales=("Sales","sum"),
        Profit=("Profit","sum"),
        Orders=("Order_ID","nunique")
    ).sort_values("Sales", ascending=False).head(10),
    use_container_width=True
)
