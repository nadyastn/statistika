import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.sidebar.header("Menu")
    task = st.sidebar.selectbox("Pilih Menu", ("Apa itu Pengolahan Data Tunggal dalam Statistika?", "Kalkulator Pengolahan Data Tunggal Statistika"))

    if task == "Apa itu Pengolahan Data Tunggal dalam Statistika?":
        penjelasan_materi()
    elif task == "Kalkulator Pengolahan Data Tunggal Statistika":
        masukkan_dan_pengolahan_data()

def masukkan_dan_pengolahan_data():
    st.header(":green[Aplikasi Pengolahan Data Tunggal dalam Statistika]")
    st.subheader("Kalkulator Pengolahan Data Tunggal Statistika")

    # Masukkan Data
    st.subheader("Masukkan Data!")
    rows = st.number_input("Jumlah Data:", min_value=1, value=1)

    data = []
    for i in range(rows):
        value = st.number_input(f"Data {i+1}", value=0.00)
        data.append(value)

    df = pd.DataFrame(data)
    st.write("Data yang Dimasukkan:")
    st.write(df)

    # Pengolahan Data
    st.subheader("Hasil Pengolahan Data:memo:")
    st.write("Rata-rata: ", np.mean(data))
    st.write("Median: ", np.median(data))
    st.write("Range/Jangkauan: ", np.round(np.max(data) - np.min(data), 2))
    st.write("Simpangan Rata-rata: ", np.round(np.mean(np.abs(data - np.mean(data))), 2))
    st.write("Ragam/Variasi: ", np.round(np.var(data), 2))
    st.write("Simpangan Baku/Standar Deviasi: ", np.round(np.std(data), 2))

def penjelasan_materi():
    st.header(":green[Aplikasi Pengolahan Data Tunggal dalam Statistika]")
    st.subheader("Apa itu Pengolahan Data Tunggal dalam Statistika?")
    st.write("Pengolahan data tunggal adalah proses pengumpulan, pengorganisasian, dan analisis data tunggal untuk memahami karakteristik dan informasi yang terkandung dalam data tersebut.")
    st.write("Dalam statistika, terdapat beberapa metode pengolahan data tunggal yang umum digunakan seperti menghitung nilai rata-rata, median, modus, simpangan baku, dan lain sebagainya. Tapi, dalam aplikasi ini hanya tersedia 6 output pengolahan data tunggal yang akan ditampilkan yaitu rata-rata, median, range/jangkauan, simpangan rata-rata, ragam/variasi, dan simpangan baku/standar deviasi.")
    st.write("1. Rata-rata")
    st.write ("Rata-rata adalah suatu bilangan yang mewakili keseluruhan data pengamatan. Artinya, rata-rata merupakan perwakilan kuantitas dari sekelompok data. Besar kecilnya nilai rata-rata dipengaruhi oleh jumlah semua data dan banyaknya data. Nilai rata-rata yang diperoleh dari pembagian antara jumlah nilai keseluruhan dengan banyak data.")
    st.write("Rumus rata-rata : x̄ = ∑x / n")
    st.write("2. Median")
    st.write("Median atau nilai tengah adalah pemusatan data yang membagi suatu data menjadi setengah (50%) data terkecil dan terbesarnya.Median adalah bilangan sentral dari suatu kumpulan dalam ukuran pemusatan data. Dimana, pertengahan data dari yang terkecil hingga terbesar. Akan tetapi jika ada 2 angka di tengah, median adalah rata-rata dari 2 angka tersebut.")
    st.write("Rumus median data tunggal ganjil : X( n+1)/2")
    st.write("Rumus median data genap : X n/2 + X (n/2 + 1 ) / 2")
    st.write("3. Range/Jangkauan")
    st.write("Rentang (range) atau disebut juga dengan jangkauan adalah selisih antara data dengan nilai yang terbesar dengan data denga nilai yang terkecil tersebut.")
    st.write("Rumus range/jangkauan : R = Xmax - Xmin")
    st.write("4. Simpangan Rata-rata")
    st.write("Simpangan Rata-rata adalah jumlah semua nilai mutlak selisih setiap nilai (xi) dengan nilai rata-rata (x̄) dibagi dengan banyak data (n).")
    st.write("Rumus simpangan rata-rata : SR = Σ| xi - x̄ | / n")
    st.write("5. Ragam/Variasi")
    st.write("Ragam Varians adalah nilai yang menunjukkan seberapa jauh sebuah kumpulan bilangan tersebar dari suatu data. Nilai ragam diperoleh dari pembagian antara jumlah masing-masing kuadrat selisih data xi dikurang dengan rata rata terhadap banyak data.")
    st.write("Rumus ragam/variasi : S²  = ∑( xi - x̄ )² ∕ n")
    st.write("6. Simpangan Baku/Standar Deviasi")
    st.write("Standar deviasi adalah nilai akar kuadrat dari suatu varians yang menunjukkan tingkat penyebaran data terhadap nilai rata-rata data tersebut. Nilai simpangan baku dari kumpulan data bisa = 0, lebih besar, maupun lebih kecil dari nol. Jika sama dengan nol, maka semua nilai dalam himpunan tersebut adalah sama. Sementara itu,nilai simpangan baku yang lebih besar atau kecil dari nol menandakan bahwa titik data individu jauh dari nilai rata-rata.")
    st.write("Rumus simpangan baku : S = √(∑( xi - x̄ ) ∕ n-1)")
    
if __name__ == '__main__':
    main()