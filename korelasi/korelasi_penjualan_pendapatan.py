import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Data yang diambil dari dua visualisasi di atas
penjualan_per_kategori = {
    'Bulan': list(range(1, 13)),
    'Elektronik': [15, 7, 8, 10, 12, 5, 10, 11, 6, 8, 9, 4],
    'Fashion': [11, 10, 9, 8, 11, 7, 22, 11, 10, 13, 15, 17],
    'Otomotif': [14, 5, 18, 10, 9, 3, 12, 8, 10, 11, 12, 14]
}

pendapatan_per_kategori = {
    'Bulan': list(range(1, 13)),
    'Elektronik': [20000, 8000, 10000, 15000, 22000, 4000, 13000, 12000, 7000, 14000, 11000, 3000],
    'Fashion': [12000, 9000, 7000, 6000, 8000, 5000, 21000, 14000, 10000, 11000, 12000, 14000],
    'Otomotif': [10000, 5000, 15000, 8000, 7000, 4000, 11000, 10000, 9000, 12000, 14000, 16000]
}

# Konversi ke DataFrame
df_penjualan = pd.DataFrame(penjualan_per_kategori)
df_pendapatan = pd.DataFrame(pendapatan_per_kategori)

# Menggabungkan data berdasarkan Bulan
df_merged = pd.merge(df_penjualan, df_pendapatan, on='Bulan', suffixes=('_Penjualan', '_Pendapatan'))

# Menghapus kolom Bulan untuk perhitungan korelasi
df_merged_without_bulan = df_merged.drop(columns=['Bulan'])

# Hitung korelasi
correlation_matrix = df_merged_without_bulan.corr()

# Buat folder untuk menyimpan visualisasi
save_path = 'C:/UAS_Pengkodean/korelasi'
os.makedirs(save_path, exist_ok=True)

# Visualisasi korelasi menggunakan heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap Korelasi antara Penjualan dan Pendapatan')
plt.savefig(os.path.join(save_path, 'heatmap_korelasi.png'))
plt.show()

# Visualisasi scatter plot untuk korelasi
categories = ['Elektronik', 'Fashion', 'Otomotif']
plt.figure(figsize=(15, 5))
for i, category in enumerate(categories):
    plt.subplot(1, 3, i+1)
    plt.scatter(df_merged[f'{category}_Penjualan'], df_merged[f'{category}_Pendapatan'])
    plt.title(f'Korelasi {category}')
    plt.xlabel('Penjualan')
    plt.ylabel('Pendapatan')

plt.tight_layout()
plt.savefig(os.path.join(save_path, 'scatter_korelasi.png'))
plt.show()
