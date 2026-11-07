PROJECT: Aplikasi Ekstraksi Fitur Warna Citra (HSV)

TUJUAN
Membuat aplikasi mudah yang menerima gambar, menampilkan histogram RGB, menghitung statistik HSV dan rata-rata RGB, serta mengunduh hasil ke CSV.

CARA MENJALANKAN
1. Instal Python 3.10 atau yang lebih baru.
2. Buka terminal di folder project.
3. Jalankan: pip install -r requirements.txt
4. Jalankan: streamlit run app.py
5. Unggah gambar pada halaman browser.

METODE
- RGB: format kanal gambar awal.
- HSV: menghitung mean dan standar deviasi Hue, Saturation, dan Value.
- Histogram RGB: visualisasi distribusi intensitas kanal merah, hijau, biru.
- Rata-rata RGB: ringkasan warna global sederhana; bukan algoritma pencarian cluster warna dominan seperti K-Means.

STRUKTUR
app.py            : source code aplikasi
requirements.txt  : pustaka yang diperlukan
README.txt        : petunjuk penggunaan
Laporan_Project.docx : laporan rancangan dan teori
