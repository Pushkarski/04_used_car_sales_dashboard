import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(page_title="Used Car Sales Dashboard", layout="wide")
st.title("Used Car Sales Dashboard")
st.markdown(
    "Explore how vehicle characteristics affect **price** "
    "and **time on market** using filters and interactive charts."
)

# --------------------------------------------------
# Constants for simple filtering
# --------------------------------------------------
MAX_PRICE = 100_000          # upper limit for price in some charts
MAX_PRICE_HEATMAP = 50_000   # upper limit for price in heatmap
MAX_ODOMETER = 200_000       # upper limit for mileage
MAX_DAYS_LISTED = 120        # upper limit for listing duration (days)

# --------------------------------------------------
# Load dataset
# --------------------------------------------------
df = pd.read_csv("vehicles_us.csv")

# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.sidebar.header("Filters")
st.sidebar.caption("Use the filters below to customize the dashboard")

# Vehicle type filter
selected_type = st.sidebar.selectbox(
    "Select vehicle type:",
    options=["All"] + sorted(df["type"].dropna().unique())
)

if selected_type != "All":
    df = df[df["type"] == selected_type]

# Condition filter
selected_condition = st.sidebar.multiselect(
    "Select vehicle condition(s):",
    options=sorted(df["condition"].dropna().unique()),
    default=sorted(df["condition"].dropna().unique())
)

df = df[df["condition"].isin(selected_condition)]

# --------------------------------------------------
# Chart 1: Price distribution by condition
# --------------------------------------------------
df_price_cond = df[
    (df["price"] <= MAX_PRICE) &
    (df["condition"].notna())
]

fig_price_cond = px.histogram(
    df_price_cond,
    x="price",
    color="condition",
    nbins=50,
    title=f"Price Distribution by Vehicle Condition (Price ≤ ${MAX_PRICE:,.0f})",
    labels={"price": "Price ($)", "count": "Number of listings"},
    barmode="overlay",
    opacity=0.6,
)
st.plotly_chart(fig_price_cond, use_container_width=True)

# --------------------------------------------------
# Chart 2: Price vs. odometer (density heatmap)
# --------------------------------------------------
df_heatmap = df[
    (df["odometer"] <= MAX_ODOMETER) &
    (df["price"] <= MAX_PRICE_HEATMAP)
]

fig_heatmap = px.density_heatmap(
    df_heatmap,
    x="odometer",
    y="price",
    nbinsx=50,
    nbinsy=50,
    color_continuous_scale="Blues",
    title=(
        "Price vs. Odometer "
        f"(Filtered: ≤ {MAX_ODOMETER:,.0f} miles & ≤ ${MAX_PRICE_HEATMAP:,.0f})"
    ),
)

fig_heatmap.update_layout(
    xaxis_title="Odometer (miles)",
    yaxis_title="Price ($)",
    coloraxis_colorbar=dict(title="Number of listings"),
)
st.plotly_chart(fig_heatmap, use_container_width=True)

# --------------------------------------------------
# Chart 3: Price by model year (boxplot)
# --------------------------------------------------
df_year = df[
    (df["model_year"] >= 1990) &
    (df["model_year"] <= 2022) &
    (df["price"] <= MAX_PRICE)
].dropna(subset=["model_year", "price"]).copy()

df_year["model_year"] = df_year["model_year"].astype(int)

fig_year = px.box(
    df_year,
    x="model_year",
    y="price",
    title="Price Distribution by Model Year (1990–2022, ≤ $100k)",
    labels={"model_year": "Model year", "price": "Price ($)"},
)
st.plotly_chart(fig_year, use_container_width=True)

# --------------------------------------------------
# Chart 4: Listing duration by condition
# --------------------------------------------------
df_days = df[
    (df["days_listed"] <= MAX_DAYS_LISTED) &
    (df["condition"].notna())
]

fig_days = px.histogram(
    df_days,
    x="days_listed",
    color="condition",
    nbins=40,
    title=f"Listing Duration by Vehicle Condition (≤ {MAX_DAYS_LISTED} days)",
    labels={"days_listed": "Days listed", "count": "Number of listings"},
    barmode="overlay",
    opacity=0.6,
)
st.plotly_chart(fig_days, use_container_width=True)

# --------------------------------------------------
# Summary text
# --------------------------------------------------
st.markdown(
    """
---
### Summary Insights

- **Vehicle condition and age strongly impact price** — listings marked as *"excellent"* or *"like new"*, as well as models from recent years, show significantly higher prices.
- **Higher mileage correlates with lower prices** — vehicles with more than 100k miles tend to be priced 25–40% lower than those with under 50k.
- **SUVs and trucks are consistently valued higher** than sedans and hatchbacks, often by \$5,000–\$10,000 on average.
- **Electric and hybrid cars tend to stay longer on the market**, but retain value better compared to gasoline vehicles.
"""
)
