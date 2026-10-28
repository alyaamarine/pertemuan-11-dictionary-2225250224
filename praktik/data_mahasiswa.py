def cari_mahasiswa(data, nim):
    # lengkapi
    return data.get(nim, "Data tidak ditemukan")

def rata_rata_nilai(data):
    # lengkapi
    if not data:
        return 0
    total_nilai = 0
    for mhs in data.values():
        total_nilai += mhs["nilai"]
    return total_nilai / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# lengkapi operasi pencarian, penambahan, pembaruan, dan rekap

# [Test Case 1] Pencarian tersedia (A003) -> Menampilkan data Citra
print(cari_mahasiswa(data_mahasiswa, "A003"))

# [Test Case 2] Pencarian tidak tersedia (A999) -> Menampilkan 'Data tidak ditemukan'
print(cari_mahasiswa(data_mahasiswa, "A999"))

# [Test Case 3] Pembaruan nilai (A002 menjadi 82)
if "A002" in data_mahasiswa:
    data_mahasiswa["A002"]["nilai"] = 82

# [Test Case 4] Penambahan data (A006)
data_mahasiswa["A006"] = {"nama": "Fahmi", "kelas": "B", "nilai": 90}

# [Test Case 5] Rekap menggunakan items() -> Semua NIM dan data tampil
for nim, detail in data_mahasiswa.items():
    print(f"NIM: {nim}, Data: {detail}")

# Perhitungan tambahan sesuai spesifikasi: Hitung rata-rata nilai seluruh mahasiswa
rata_rata = rata_rata_nilai(data_mahasiswa)
print(f"Rata-rata nilai: {rata_rata}")