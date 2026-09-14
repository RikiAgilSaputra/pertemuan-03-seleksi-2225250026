#Memasukkan bilangan yang diinginkan
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))

#logika percabangan untuk membandingkan kedua bilangan
if a >= b:
    if a == b:

        #Menampilkan hasil jika kedua bilangan sama
        print("kedua bilangan sama")
    else:

        #Menampilkan hasil perbandingan bilangan pertama dan bilangan kedua
        print("bilangan pertama lebih besar")
else:
    
    #Menampilkan hasil perbandingan bilangan pertama dan bilangan kedua
    print("bilangan pertama lebih kecil")
