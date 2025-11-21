import datetime

# --- Database Simulasi ---
# Menggunakan dictionary untuk menyimpan data. 
# Dalam aplikasi nyata, ini akan diganti dengan database seperti SQL atau file (CSV/JSON).

# Daftar peraturan sekolah beserta poin penalti
PERATURAN_SEKOLAH = {
    "P01": {"deskripsi": "Terlambat masuk sekolah", "poin": 5},
    "P02": {"deskripsi": "Seragam tidak lengkap atau tidak rapi", "poin": 10},
    "P03": {"deskripsi": "Meninggalkan kelas tanpa izin guru", "poin": 15},
    "P04": {"deskripsi": "Merusak fasilitas sekolah", "poin": 30},
    "P05": {"deskripsi": "Merokok di lingkungan sekolah", "poin": 50},
    "P06": {"deskripsi": "Berkelahi atau melakukan perundungan", "poin": 75},
}

# Data siswa dan riwayat pelanggarannya
DATA_SISWA = {
    "S1001": {"nama": "Budi Hartono", "kelas": "XI IPA 1", "pelanggaran": []},
    "S1002": {"nama": "Citra Amelia", "kelas": "X IPS 2", "pelanggaran": []},
    "S1003": {"nama": "Doni Saputra", "kelas": "XII Bahasa", "pelanggaran": []},
}

# --- Fungsi-Fungsi Aplikasi ---

def tampilkan_peraturan():
    """Menampilkan semua daftar peraturan sekolah dan poinnya."""
    print("\n--- DAFTAR TATA TERTIB SEKOLAH ---")
    print("-" * 40)
    print(f"{'Kode':<6} | {'Deskripsi Pelanggaran':<30} | {'Poin':<5}")
    print("-" * 40)
    for kode, detail in PERATURAN_SEKOLAH.items():
        print(f"{kode:<6} | {detail['deskripsi']:<30} | {detail['poin']:<5}")
    print("-" * 40)

def catat_pelanggaran():
    """Mencatat pelanggaran baru untuk seorang siswa."""
    print("\n--- CATAT PELANGGARAN SISWA ---")
    id_siswa = input("Masukkan ID Siswa (contoh: S1001): ").strip().upper()

    if id_siswa not in DATA_SISWA:
        print(f"Error: Siswa dengan ID '{id_siswa}' tidak ditemukan.")
        return

    print(f"Mencatat pelanggaran untuk: {DATA_SISWA[id_siswa]['nama']} ({DATA_SISWA[id_siswa]['kelas']})")
    tampilkan_peraturan()
    kode_pelanggaran = input("Masukkan Kode Pelanggaran (contoh: P01): ").strip().upper()

    if kode_pelanggaran not in PERATURAN_SEKOLAH:
        print(f"Error: Kode pelanggaran '{kode_pelanggaran}' tidak valid.")
        return

    # Membuat catatan pelanggaran
    pelanggaran = {
        "kode": kode_pelanggaran,
        "deskripsi": PERATURAN_SEKOLAH[kode_pelanggaran]["deskripsi"],
        "poin": PERATURAN_SEKOLAH[kode_pelanggaran]["poin"],
        "tanggal": datetime.date.today().isoformat()
    }

    # Menambahkan catatan ke data siswa
    DATA_SISWA[id_siswa]["pelanggaran"].append(pelanggaran)
    print("\n>> Pelanggaran berhasil dicatat! <<")

def lihat_riwayat_siswa():
    """Menampilkan riwayat pelanggaran dan total poin seorang siswa."""
    print("\n--- LIHAT RIWAYAT PELANGGARAN ---")
    id_siswa = input("Masukkan ID Siswa (contoh: S1001): ").strip().upper()

    if id_siswa not in DATA_SISWA:
        print(f"Error: Siswa dengan ID '{id_siswa}' tidak ditemukan.")
        return

    siswa = DATA_SISWA[id_siswa]
    print(f"\nNama  : {siswa['nama']}")
    print(f"Kelas : {siswa['kelas']}")
    print("-" * 50)

    if not siswa["pelanggaran"]:
        print("Siswa ini tidak memiliki catatan pelanggaran. Bersih!")
    else:
        total_poin = 0
        print(f"{'Tanggal':<12} | {'Deskripsi Pelanggaran':<30} | {'Poin':<5}")
        print("-" * 50)
        for pelanggaran in siswa["pelanggaran"]:
            print(f"{pelanggaran['tanggal']:<12} | {pelanggaran['deskripsi']:<30} | {pelanggaran['poin']:<5}")
            total_poin += pelanggaran['poin']
        print("-" * 50)
        print(f"{'Total Poin Pelanggaran:':<45}{total_poin}")

    print("-" * 50)


def main():
    """Fungsi utama untuk menjalankan aplikasi."""
    while True:
        print("\n===== APLIKASI TATA TERTIB SEKOLAH =====")
        print("1. Lihat Daftar Tata Tertib")
        print("2. Catat Pelanggaran Siswa")
        print("3. Lihat Riwayat Pelanggaran Siswa")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda (1-4): ")

        if pilihan == '1':
            tampilkan_peraturan()
        elif pilihan == '2':
            catat_pelanggaran()
        elif pilihan == '3':
            lihat_riwayat_siswa()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka dari 1 hingga 4.")
        
        input("\nTekan Enter untuk kembali ke menu utama...")


if __name__ == "__main__":
    main()
