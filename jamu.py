# Daftar gejala dan rekomendasi jamu
gejala_jamu = {
    "batuk": ["Jamu Kunyit Asam", "Jamu Jahe"],
    "demam": ["Jamu Temulawak", "Jamu Brotowali"],
    "sakit kepala": ["Jamu Beras Kencur"],
    "masuk angin": ["Jamu Jahe", "Jamu Temulawak"],
    "nyeri otot": ["Jamu Kencur", "Jamu Brotowali"]
}

# Fungsi untuk rekomendasi jamu berdasarkan input gejala
def rekomendasi_jamu(gejala_input):
    rekomendasi = []
    gejala_input = gejala_input.lower()  # Mengubah input menjadi huruf kecil untuk pencocokan
    
    for gejala, jamu_list in gejala_jamu.items():
        # Memeriksa apakah gejala ada di dalam input pengguna
        if gejala in gejala_input:
            rekomendasi.extend(jamu_list)  # Menambahkan jamu yang direkomendasikan untuk gejala tersebut
    
    # Menghapus duplikat rekomendasi (jika ada) dan mengembalikan hasil
    return list(set(rekomendasi)) if rekomendasi else ["Jamu tidak ditemukan untuk gejala yang dimasukkan"]

# Contoh penggunaan fungsi
gejala_user = input("Masukkan gejala yang Anda alami: ")  # Meminta input gejala dari pengguna
hasil_rekomendasi = rekomendasi_jamu(gejala_user)

# Menampilkan rekomendasi
print("\nRekomendasi jamu untuk gejala Anda:")
for jamu in hasil_rekomendasi:
    print("- " + jamu)

