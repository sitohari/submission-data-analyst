import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

st.title("Dashboard Penyewaan Sepeda")
st.write("Analisis data penyewaan sepeda source ")

main_df = pd.read_csv("main_df.xls")

# Membuat subplot dengan ukuran yang lebih sesuai
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))


# Grafik batang: Jumlah penyewaan per hari
daily_counts = main_df.groupby('weekday')['cnt'].sum()
sns.barplot(x=daily_counts.index, y=daily_counts.values, ax=axes[0])
axes[0].set_xlabel('Hari dalam Seminggu')
axes[0].set_ylabel('Jumlah Sepeda Disewa')
axes[0].set_title('Jumlah Penyewaan Sepeda per Hari')

# Grafik garis: Perkembangan jumlah penyewaan per tahun
yearly_counts = main_df.groupby('year')['cnt'].sum()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, ax=axes[1])
axes[1].set_xlabel('Tahun')
axes[1].set_ylabel('Total Penyewaan Sepeda')
axes[1].set_title('Perkembangan Jumlah Penyewaan Sepeda per Tahun')

st.pyplot(fig)

st.caption('Copyright © sitohari 2024')