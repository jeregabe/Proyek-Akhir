import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Baca data dari file CSV
df = pd.read_csv("dataset.csv")
st.sidebar.title('Jasa Sewa Sepeda JERE')

# side bar
st.sidebar.image("sepeda.png", caption='ig : sewasepeda_jere', use_column_width=True)

# Judul Dashboard
st.title('Dashboard Data Persewaan Sepeda')

# Visualisasi distribusi persewaan sepeda berdasarkan musim 
st.subheader('Distribusi Persewaan Sepeda berdasarkan Musim')
fig = px.histogram(df, x='cnt', color='season', 
                   facet_col='season', facet_col_wrap=2,
                   labels={'cnt': 'Jumlah Sewa Sepeda', 'season': 'Musim'})
                   
st.plotly_chart(fig)

# Keterangan
keterangan_musim = """
* Distribusi persewaan sepeda pada musim 1 (Semi) merupakan distribusi right skewness
* Distribusi persewaan sepeda pada musim 2 (Panas) mendekati distribusi normal
* Distribusi persewaan sepeda pada musim 3 (Gugur) adalah distribusi left skewness
* Distribusi persewaan sepeda pada musim 4 (Dingin) mendekati distribusi normal
"""

st.markdown(keterangan_musim)

# Perbandingan rata-rata persewaan sepeda antara hari libur dan hari kerja 
st.subheader('Perbandingan Rata-rata Persewaan Sepeda Antara Hari Libur dan Hari Kerja')
avg_rentals = df.groupby('workingday')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(data=avg_rentals, x='workingday', y='cnt', hue='workingday', ax=ax)
ax.set(xlabel='Hari Kerja', ylabel='Rata-rata Jumlah Sewa Sepeda',
       title='Rata-rata Jumlah Sewa Sepeda Berdasarkan Hari Libur dan Hari Kerja')
st.pyplot(fig)


df = pd.read_csv("dataset.csv")  

# Hitung rata-rata jumlah sewa sepeda per hari pada hari libur
avg_rentals_weekend = round(df[df['workingday'] == 0]['cnt'].mean(), 0)

# Hitung rata-rata jumlah sewa sepeda per hari pada hari kerja
avg_rentals_weekday = round(df[df['workingday'] == 1]['cnt'].mean(), 0)

# Tampilkan jumlah rata-rata sewa sepeda per hari pada hari libur
st.markdown(f"**Rata-rata Sewa Sepeda (Hari Libur):** {avg_rentals_weekend} sepeda/hari")

# Tampilkan jumlah rata-rata sewa sepeda per hari pada hari kerja
st.markdown(f"**Rata-rata Sewa Sepeda (Hari Kerja):** {avg_rentals_weekday} sepeda/hari")


# Keterangan Perbandingan Rata-rata Persewaan Sepeda Antara Hari Libur dan Hari Kerja
keterangan_hari = """
Dari gambar diatas, jumlah orang yang menyewa sepeda di hari kerja cenderung lebih tinggi pada hari libur dibandingkan dengan hari libur. Hal ini mungkin disebabkan oleh minat orang-orang untuk berolahraga saat berangkat kerja, dan pada hari libur orang-orang lebih memilih untuk tetap dirumah..
"""

st.markdown(keterangan_hari)

