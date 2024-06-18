import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Data yang sudah ada
data = {
    "Tanggal": [
        "01/01/2023", "05/01/2023", "10/02/2023", "15/02/2023", "20/03/2023", "25/03/2023",
        "10/04/2023", "15/04/2023", "05/05/2023", "10/05/2023", "01/06/2023", "05/06/2023",
        "10/07/2023", "15/07/2023", "05/08/2023", "10/08/2023", "01/09/2023", "05/09/2023",
        "10/10/2023", "15/10/2023", "01/11/2023", "05/11/2023", "01/12/2023", "05/12/2023",
        "10/01/2023", "15/01/2023", "05/02/2023", "20/02/2023", "10/03/2023", "15/03/2023",
        "05/04/2023", "20/04/2023", "15/05/2023", "20/05/2023", "10/06/2023", "15/06/2023",
        "05/07/2023", "20/07/2023", "01/08/2023", "15/08/2023", "10/09/2023", "15/09/2023",
        "01/10/2023", "05/10/2023", "10/11/2023", "15/11/2023", "05/12/2023", "10/12/2023",
        "15/12/2023", "20/12/2023", "25/12/2023"
    ],
    "Nama Produk": [
        "Televisi", "Jaket", "Kulkas", "Kemeja", "Motor", "Microwave",
        "Celana", "Mobil", "AC", "Rok", "Helm", "Komputer",
        "Kaos", "Televisi", "Suku Cadang", "Jaket", "Kulkas", "Aksesoris",
        "Kemeja", "Microwave", "Motor", "AC", "Celana", "Mobil",
        "Komputer", "Kaos", "Helm", "Televisi", "Jaket", "Suku Cadang",
        "Kulkas", "Kemeja", "Aksesoris", "Microwave", "Rok", "Motor",
        "AC", "Celana", "Mobil", "Komputer", "Kaos", "Helm",
        "Televisi", "Jaket", "Suku Cadang", "Kulkas", "Kemeja", "Aksesoris",
        "Microwave", "Rok", "Mobil"
    ],
    "Kategori": [
        "Elektronik", "Fashion", "Elektronik", "Fashion", "Otomotif", "Elektronik",
        "Fashion", "Otomotif", "Elektronik", "Fashion", "Otomotif", "Elektronik",
        "Fashion", "Elektronik", "Otomotif", "Fashion", "Elektronik", "Otomotif",
        "Fashion", "Elektronik", "Otomotif", "Elektronik", "Fashion", "Otomotif",
        "Elektronik", "Fashion", "Otomotif", "Elektronik", "Fashion", "Otomotif",
        "Elektronik", "Fashion", "Otomotif", "Elektronik", "Fashion", "Otomotif",
        "Elektronik", "Fashion", "Otomotif", "Elektronik", "Fashion", "Otomotif",
        "Elektronik", "Fashion", "Otomotif", "Elektronik", "Fashion", "Otomotif",
        "Elektronik", "Fashion", "Otomotif"
    ],
    "Jumlah Unit Terjual": [
        10, 5, 2, 8, 3, 4,
        7, 6, 5, 4, 2, 3,
        6, 4, 1, 8, 5, 3,
        7, 4, 2, 3, 6, 4,
        3, 4, 5, 2, 6, 3,
        4, 7, 6, 5, 8, 4,
        3, 6, 2, 4, 5, 3,
        6, 7, 8, 5, 4, 3,
        2, 6, 5
    ],
    "Harga per Unit": [
        500, 300, 1500, 200, 1000, 750,
        250, 1200, 800, 300, 1100, 950,
        350, 900, 2000, 275, 1000, 1500,
        300, 1200, 1700, 800, 400, 1300,
        700, 400, 1400, 800, 350, 900,
        750, 320, 1100, 850, 280, 1300,
        1000, 360, 1500, 950, 400, 1600,
        1200, 330, 1400, 850, 300, 1700,
        1500, 340, 1300
    ],
    "Total Pendapatan": [
        5000, 1500, 3000, 1600, 3000, 3000,
        1750, 7200, 4000, 1200, 2200, 2850,
        2100, 3600, 2000, 2200, 5000, 4500,
        2100, 4800, 3400, 2400, 2400, 5200,
        2100, 1600, 7000, 1600, 2100, 2700,
        3000, 2240, 6600, 4250, 2240, 5200,
        3000, 2160, 3000, 3800, 2000, 4800,
        7200, 2310, 11200, 4250, 1200, 5100,
        3000, 2040, 6500
    ]
}

df = pd.DataFrame(data)

# Fungsi untuk menghasilkan data acak
def generate_random_data(num_entries, start_date, categories, products):
    dates = pd.date_range(start=start_date, periods=num_entries, freq='5D').strftime("%d/%m/%Y").tolist()
    category = np.random.choice(categories, num_entries)
    product = [np.random.choice(products[cat]) for cat in category]
    units_sold = np.random.randint(1, 10, num_entries)
    price_per_unit = np.random.randint(200, 2000, num_entries)
    total_revenue = units_sold * price_per_unit

    return pd.DataFrame({
        "Tanggal": dates,
        "Nama Produk": product,
        "Kategori": category,
        "Jumlah Unit Terjual": units_sold,
        "Harga per Unit": price_per_unit,
        "Total Pendapatan": total_revenue
    })

# Kategori dan produk
categories = ["Elektronik", "Fashion", "Otomotif"]
products = {
    "Elektronik": ["Televisi", "Kulkas", "Microwave", "AC", "Komputer"],
    "Fashion": ["Jaket", "Kemeja", "Celana", "Rok", "Kaos"],
    "Otomotif": ["Motor", "Mobil", "Helm", "Suku Cadang", "Aksesoris"]
}

# Menghasilkan 50 data acak tambahan
additional_df = generate_random_data(50, "01/01/2024", categories, products)

# Menggabungkan data lama dan baru
combined_df = pd.concat([df, additional_df], ignore_index=True)

# Menyimpan ke dalam file Excel
combined_df.to_excel("C:/UAS_Pengkodean/combined_data.xlsx", index=False)

combined_df.head(10)  # Menampilkan 10 baris pertama dari dataset yang digabungkan
