#Memasukkan panjang sisi segitiga 
a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

#Logika percabangan untuk menentukan jenis segitiga
if a + b > c and a + c > b and b + c > a:
    #Menentukan jenis segitiga sama sisi
    if a == b and b == c:
        print("Segitiga sama sisi")
    else:
        #Menentukan jenis segitiga sama kaki
        if a == b or a == c or b == c:
            print("Segitiga sama kaki")
        else:
            #Menampilkan hasil segitiga sembarang
            print("Segitiga sembarang")
else:
    #Menampilkan hasil jika ketiga sisi tidak membentuk segitiga
    print("Ketiga sisi tidak membentuk segitiga")
