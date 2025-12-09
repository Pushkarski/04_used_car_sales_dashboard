# Used Car Sales Dashboard

This project explores used car sales data from the US and turns it into an **interactive analytical dashboard**.  
Built with **Python**, **Plotly**, and **Streamlit**, the app helps users understand how vehicle characteristics affect **price** and **time on market**.

> *Completed as part of the TripleTen Data Analysis Bootcamp.*

---

## 🚗 Project Goals  

- Identify key factors that influence used car prices  
- Explore how **condition**, **type**, **mileage**, and **fuel type** affect market behavior  
- Provide actionable insights for **buyers** and **sellers**

---

## 🔍 Hypotheses Tested  

Using exploratory data analysis (EDA), the following hypotheses were tested:

1. **Higher mileage** leads to lower vehicle prices.  
2. **Newer vehicles** (recent model years) are generally more expensive.  
3. **Better vehicle condition** is associated with both higher prices and faster sales.  
4. **Vehicle type** (SUV, truck, sedan, etc.) affects pricing — SUVs and trucks tend to cost more.  
5. **Fuel type** influences both **price** and **listing duration** — electric and hybrid vehicles show distinct patterns.

Each hypothesis was evaluated and visualized in [`notebooks/EDA.ipynb`](notebooks/EDA.ipynb) using boxplots, histograms, scatter plots, and density heatmaps.

---

## 🧰 Tech Stack  

- **Python**: `pandas`, `plotly`, `streamlit`  
- **Jupyter Notebook** for EDA  
- **Git / GitHub** for version control  
- **Streamlit Cloud / Render** for app deployment  

---

## 📊 Key Insights  

- **Newer and better-condition vehicles** are priced significantly higher.  
- **Mileage above 100,000 miles** reduces price roughly by **25–40%**.  
- **SUVs and trucks** are on average **$5,000–10,000** more expensive than sedans.  
- **Electric and hybrid cars** tend to stay on the market longer but **retain value better**.

---

## 🚀 How to Use the Dashboard  

1. Open the live dashboard:  
   👉 [**Launch Streamlit App**](https://car-sales-dashboard-cakl.onrender.com)  
2. Use the filters in the sidebar to choose **vehicle condition**, **type**, and other parameters.  
3. Explore interactive charts to analyze **price** and **time on market** for different car segments.

> The dashboard focuses on the most interactive and decision-relevant insights.  
> For a full review of all hypotheses and visualizations, see `notebooks/EDA.ipynb`.

---

## 📁 Repository Structure  

```
04_used_car_sales_dashboard/
├── app.py                  # Streamlit app script
├── vehicles_us.csv         # Dataset
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── README.md               # Project overview
└── notebooks/
    └── EDA.ipynb           # Exploratory data analysis (EDA)
