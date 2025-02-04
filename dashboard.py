import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 


day_df = pd.read_csv("day.csv")
day_df["season"] = day_df["season"].replace({1:"Spring", 2:"Summer",3:"Fall",4:"Winter"})
day_df["workingday"] = day_df["workingday"].replace({0 : "Weekend/Holiday", 1 : "Workday"})
st.title("Penyewaan Sepeda")

#Grafik Season
st.header("Penyewaan Sepeda berdasarkan season")
selected_season = st.multiselect("Pilih Season : ", ["Spring","Summer","Fall","Winter"], default=["Spring","Summer","Fall","Winter"])
filterseason_df = day_df[day_df["season"].isin(selected_season)]
season_order = ["Spring", "Summer", "Fall", "Winter"]
filterseason_df["season"] = pd.Categorical(filterseason_df['season'], categories=season_order, ordered=True)

plt.figure(figsize=(10,6))
fig, ax = plt.subplots()
season_total = filterseason_df.groupby(by="season", observed=True).agg({
    "casual" : "sum",
    "registered" : "sum",
    "cnt" : "sum"
}).reset_index()

sns.barplot(data=season_total, x="season", y="cnt", errorbar=None)
def format_func(value, tick_number):
        return f"{value:,.0f}"
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
plt.title("Jumlah Penyewa Setiap Season")
plt.xlabel("Season")
plt.ylabel("Jumlah Penyewa")
st.pyplot(fig)

#Grafik Workday
st.header("Penyewaan Sepeda ketika Holiday/Weekend atau Workday")
selected_day = st.multiselect("Pilih Tipe Hari : ", ["Weekend/Holiday","Workday"], default=["Weekend/Holiday","Workday"])
filterworkday_df = day_df[day_df["workingday"].isin(selected_day)]

plt.figure(figsize=(10,6))
fig, ax = plt.subplots()
workingday_total = filterworkday_df.groupby(by="workingday", observed=True).agg({ 
    "casual" :  "sum",
    "registered" : "sum",
    "cnt" : "sum",
})

sns.barplot(data=workingday_total, x="workingday", y="cnt", errorbar=None)
def format_func(value, tick_number):
    return f"{value:,.0f}"

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
plt.title("Jumlah Penyewa ")
plt.ylabel("Jumlah Penyewa")
st.pyplot(fig)
