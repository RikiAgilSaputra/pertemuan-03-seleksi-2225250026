# Pertemuan 03 Seleksi Python
Nama :  RIKI AGIL SAPUTRA
NIM  :  2225250026
Kelas:  3A

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
Langkah keputusan program tugas:
1.	Masukkan nilai koefisien a, b, dan c
2.	Membandingkan nilai a dengan 0 (a==0)
3.	Menghitung diskriminan jika a tidak sama dengan 0 (a!=0)
4.	Menentukan dua akar real berbeda jika diskriminan lebih    dari 0 (D>0)
5.	Menentukan akar kembar jika diskriminan sama dengan 0 (D=0)
6.	Menentukan hasil jika diskriminan kurang dari 0 (D<0)

## Hasil Pengujian
## Hasil Pengujian

| a | b | c | d | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|---|---|
| 1 | -5 | 6 | 1 | Dua akar real: 3 dan 2 | Dua akar real: 3 dan 2 | Success |
| 1 | 2 | 1 | 0 | Akar kembar: -1 | Akar kembar: -1 | Success |
| 1 | 0 | 1 | -4 | Tidak ada akar real | Tidak ada akar real | Success |
| 0 | 2 | 3 | - | Bukan persamaan kuadrat | Bukan persamaan kuadrat | Success |
| 3 | 4 | 1 | 4 | Dua akar real: -0.33 dan -1 | Dua akar real: -0.33 dan -1 | Success |
| 0 | 1 | 9 | - | Bukan persamaan kuadrat | Bukan persamaan kuadrat | Success |

## Refleksi
Satu kesalahan logika yang saya temukan bahwasannya if dapat dipakai untuk beberapa else, sedangkan if dan else harus selalu sepasang. Kemudian saya memperbaiki kesalahan tersebut dengan penggunaan nested if dengan penggunaan if dan else bersarang, di mana saya menggunakan if-else di dalam blok if ataupun else.