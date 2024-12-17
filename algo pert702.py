# Fungsi untuk menentukan grade berdasarkan nilai
def tentukan_grade(nilai):
    if 86 <= nilai <= 100:
        return 'A'
    elif 76 <= nilai <= 85:
        return 'B'
    elif 61 <= nilai <= 75:
        return 'C'
    elif 41 <= nilai <= 60:
        return 'D'
    elif 0 <= nilai <= 40:
        return 'E'
    else:
        return 'Nilai tidak valid'

# Input nilai dari pengguna
try:
    nilai = int(input("Masukkan nilai (0-100): "))
    # Menentukan grade
    grade = tentukan_grade(nilai)
    # Menampilkan hasil
    print(f"Nilai Anda: {nilai}")
    print(f"Grade Anda: {grade}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka bulat antara 0-100.")
