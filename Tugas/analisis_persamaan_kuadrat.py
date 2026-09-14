print("Analisis Persamaan Kudarat")

#Memasukkan nilai koefisien a, b, dan c
a = float(input("Koefisisen a:"))
b = float(input("Koefisisen b:"))
c = float(input("Koefisisen c:"))

#Logika percabangan untuk menentukan jenis akar persamaan kuadrat
if a== 0:
    print("Bukan Persamaan Kuadrat")
else:

    #Menghitung nilai diskriminan
    diskriminan = D = b**2-4*a*c 
    print(f"Diskriminan = {diskriminan:.2f}")

    #Logika percabangan untuk menentukan jenis akar persamaan kuadrat
    if diskriminan > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)

        #Menampilkan hasil jenis akar persamaan kuadrat
        print("Jenis akar : Dua akar real berbeda")
        print(f"Akar x1 = {x1:.2f}")
        print(f"Akar x2 = {x2:.2f}")

    #Logika percabangan untuk menentukan jenis akar persamaan kuadrat
    if diskriminan == 0:
        x = -b / (2 * a)

        #Menampilkan hasil jenis akar persamaan kuadrat
        print("Jenis akar : Satu akar real kembar")
        print(f"Akar x = {x:.2f}")

    #Logika percabangan untuk menentukan jenis akar persamaan kuadrat
    if diskriminan < 0: 
        
        #Menampilkan hasil jenis akar persamaan kuadrat
        print("tidak ada akar real")
