import datetime

# --- Database Simulasi ---
# Menggunakan dictionary untuk menyimpan data. 
# Dalam aplikasi nyata, ini akan diganti dengan database seperti SQL atau file (CSV/JSON).

# Daftar peraturan sekolah beserta poin penalti
PERATURAN_SEKOLAH = {
    "P1": {"deskripsi": "Terlambat masuk sekolah", "ket": 1},
    "P2": {"deskripsi": "Seragam tidak lengkap atau tidak rapi", "ket": 1},
    "P3": {"deskripsi": "ke kantin saat jam pelajaran", "ket": 1},
    "P4": {"deskripsi": "Merusak fasilitas sekolah", "ket": 1},
    "P5": {"deskripsi": "Merokok di lingkungan sekolah", "ket": 1},
    "P6": {"deskripsi": "Berkelahi atau melakukan perundungan", "ket": 1},
}

# Data siswa dan riwayat pelanggarannya
DATA_SISWA = {
    "S101": {"nama": "Budi Hartono", "kelas": "XI IPA 1", "pelanggaran": []},
    "S102": {"nama": "Citra Amelia", "kelas": "X IPS 2", "pelanggaran": []},
    "S103": {"nama": "Doni Saputra", "kelas": "XII Bahasa", "pelanggaran": []},
}

# --- Fungsi-Fungsi Aplikasi ---

def tampilkan_peraturan():
    """Menampilkan semua daftar peraturan sekolah dan keterangannya."""
    print("\n--- DAFTAR TATA TERTIB SEKOLAH ---")
    print("-" * 40)
    print(f"{'Kode':<6} | {'Deskripsi Pelanggaran':<30} | {'ket':<5}")
    print("-" * 40)
    for kode, detail in PERATURAN_SEKOLAH.items():
        print(f"{kode:<6} | {detail['deskripsi']:<30} | {detail['ket']:<5}")
    print("-" * 40)

def catat_pelanggaran():
    """Mencatat pelanggaran baru untuk seorang siswa."""
    print("\n--- CATAT PELANGGARAN SISWA ---")
    id_siswa = input("Masukkan ID Siswa (contoh: S101): ").strip().upper()

    if id_siswa not in DATA_SISWA:
        print(f"Error: Siswa dengan ID '{id_siswa}' tidak ditemukan.")
        return

    print(f"Mencatat pelanggaran untuk: {DATA_SISWA[id_siswa]['nama']} ({DATA_SISWA[id_siswa]['kelas']})")
    tampilkan_peraturan()
    kode_pelanggaran = input("Masukkan Kode Pelanggaran (contoh: P1): ").strip()

    if kode_pelanggaran not in PERATURAN_SEKOLAH:
        print(f"Error: Kode pelanggaran '{kode_pelanggaran}' tidak valid.")
        return

    # Membuat catatan pelanggaran
    pelanggaran = {
        "kode": kode_pelanggaran,
        "deskripsi": PERATURAN_SEKOLAH[kode_pelanggaran]["deskripsi"],
        "ket": PERATURAN_SEKOLAH[kode_pelanggaran]["ket"],
        "tanggal": datetime.date.today().isoformat()
    }

    # Menambahkan catatan ke data siswa
    DATA_SISWA[id_siswa]["pelanggaran"].append(pelanggaran)
    print("\n>> Pelanggaran berhasil dicatat! <<")

def lihat_riwayat_siswa():
    """Menampilkan riwayat pelanggaran dan total keterangan seorang siswa."""
    print("\n--- LIHAT RIWAYAT PELANGGARAN ---")
    id_siswa = input("Masukkan ID Siswa (contoh: S101): ").strip().upper()

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
        total_ket = 0
        print(f"{'Tanggal':<12} | {'Deskripsi Pelanggaran':<30} | {'ket':<5}")
        print("-" * 50)
        for pelanggaran in siswa["pelanggaran"]:
            print(f"{pelanggaran['tanggal']:<12} | {pelanggaran['deskripsi']:<30} | {pelanggaran['ket']:<5}")
            total_ket += pelanggaran['ket']
        print("-" * 50)
        print(f"{'Total ket Pelanggaran:':<45}{total_ket}")

        # Menambahkan pengecekan konsekuensi berdasarkan jumlah pelanggaran
        jumlah_pelanggaran = len(siswa["pelanggaran"])
        if jumlah_pelanggaran >= 3:
            print("\nKONSEKUENSI: Siswa telah melakukan lebih dari 2 pelanggaran, perlu Pemanggilan Orang Tua!")
 
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
