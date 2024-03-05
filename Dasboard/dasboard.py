import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

   
import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st
import pandas as pd
import plotly.express as px

# Baca data dari file CSV
df = pd.read_csv("dataset.csv")

# Judul Dashboard
st.title('Dashboard Data Persewaan Sepeda')

# Visualisasi distribusi persewaan sepeda berdasarkan musim menggunakan Plotly Express
st.subheader('Distribusi Persewaan Sepeda berdasarkan Musim')
fig = px.histogram(df, x='cnt', color='season', 
                   facet_col='season', facet_col_wrap=2,
                   labels={'cnt': 'Jumlah Sewa Sepeda', 'season': 'Musim'},
                   title='Distribusi Jumlah Sewa Sepeda Berdasarkan Musim')
st.plotly_chart(fig)
# Keterangan
keterangan = """
* Distribusi persewaan sepeda pada musim 1 (Musim Semi) merupakan distribusi right skewness
* Distribusi persewaan sepeda pada musim 2 (Musim Panas) mendekati distribusi normal
* Distribusi persewaan sepeda pada musim 3 (Musim Gugur) adalah distribusi left skewness
* Distribusi persewaan sepeda pada musim 4 (Musim Dingin) mendekati distribusi normal
"""
st.markdown(keterangan)




# Perbandingan rata-rata persewaan sepeda antara hari libur dan hari kerja menggunakan Matplotlib
st.subheader('Perbandingan Rata-rata Persewaan Sepeda Antara Hari Libur dan Hari Kerja')
avg_rentals = df.groupby('workingday')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(data=avg_rentals, x='workingday', y='cnt', hue='workingday', ax=ax)
ax.set(xlabel='Hari Kerja', ylabel='Rata-rata Jumlah Sewa Sepeda',
       title='Rata-rata Jumlah Sewa Sepeda Berdasarkan Hari Libur dan Hari Kerja')
st.pyplot(fig)

# Keterangan Perbandingan Rata-rata Persewaan Sepeda Antara Hari Libur dan Hari Kerja
keterangan_hari = """
* Rata-rata jumlah sepeda yang disewa pada hari libur lebih banyak daripada hari kerja.
"""

st.markdown(keterangan_hari)


