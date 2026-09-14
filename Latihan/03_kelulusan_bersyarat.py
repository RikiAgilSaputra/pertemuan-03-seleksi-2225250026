#Memasukkan nilai dan persentase kehadiran
nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

#Logika percabangan untuk menentukan kelulusan bersyarat
if nilai >= 60 and kehadiran >= 80:
    
    #Menampilkan hasil kelulusan bersyarat
    print("Lulus")
else:

    #Menampilkan hasil kelulusan bersyarat
    print("Tidak lulus")
