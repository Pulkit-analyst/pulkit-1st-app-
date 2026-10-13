
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AlphaPulse",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AlphaPulse")
st.subheader("Stock Market Dashboard")
st.write("Explore a sample stock price trend.")

# Sample data for demonstration
df = pd.DataFrame({
    "Date": pd.date_range("2026-01-01", periods=10),
    "Price": [100, 103, 101, 106, 109, 107, 112, 115, 113, 120]
})

latest_price = df["Price"].iloc[-1]
first_price = df["Price"].iloc[0]
change = latest_price - first_price

col1, col2, col3 = st.columns(3)

col1.metric("Latest Sample Price", f"${latest_price:.2f}")
col2.metric("Sample Price Change", f"${change:.2f}")
col3.metric(
    "Sample Change %",
    f"{change / first_price * 100:.2f}%"
)

fig = px.line(
    df,
    x="Date",
    y="Price",
    markers=True,
    title="Sample Stock Price Trend"
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "Educational demo using sample data, not live market prices "
    "or investment advice."
)
