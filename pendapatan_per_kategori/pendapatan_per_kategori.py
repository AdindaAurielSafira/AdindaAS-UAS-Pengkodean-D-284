import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file CSV
df = pd.read_csv('C:/UAS_Pengkodean/step_awal/combined_data.csv', delimiter=';')

# Menentukan format tanggal yang sesuai
date_format = "%d/%m/%Y"

# Konversi kolom Tanggal ke format datetime dengan format yang ditentukan
df['Tanggal'] = pd.to_datetime(df['Tanggal'], format=date_format)

# Membuat kolom baru untuk Total Pendapatan per bulan
df['Bulan'] = df['Tanggal'].dt.month
df['Tahun'] = df['Tanggal'].dt.year
df['Total_Pendapatan'] = df['Jumlah Unit Terjual'] * df['Harga per Unit']

# Agregasi data per kategori dan bulan
df_agg = df.groupby(['Kategori', 'Tahun', 'Bulan']).agg({'Jumlah Unit Terjual': 'sum', 'Total_Pendapatan': 'sum'}).reset_index()

# Visualisasi pendapatan per kategori
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_agg, x='Bulan', y='Total_Pendapatan', hue='Kategori', marker='o')
plt.title('Pendapatan per Kategori per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Pendapatan')
plt.legend(title='Kategori')
plt.xticks(range(1, 13))
plt.grid(True)

# Simpan visualisasi dalam format PNG
plt.savefig('C:/UAS_Pengkodean/pendapatan_per_kategori/pendapatan_per_kategori.png')

# Tampilkan visualisasi
plt.show()
