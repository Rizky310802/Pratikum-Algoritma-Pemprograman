print("----------------- Rizky Soto Bogor-Tambun -----------------")
print("------------------Tambun Utara Kab Bekasi---------------")
print("-----------------------08832839227-------------------")
import datetime
x=datetime.datetime.now()
print(x)
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Soto Babat - Rp 15000")
   print("2. Soto Mie Bogor - Rp 12000")
   print("3. Soto Iga Sapi - Rp 17000")
   print("4. Soto Lamongan - Rp 18000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," Porsi Soto Babat = Rp", totalmkn)
       mkn=("Soto Babat")
   elif nomor==2:
       totalmkn=porsi*12000
       print (porsi," Porsi Soto Mie Bogor  = Rp", totalmkn)
       mkn=("Soto Mie Bogor")
   elif nomor==3:
       totalmkn=porsi*17000
       print (porsi, " Porsi Soto Iga Sapi  = Rp", totalmkn)
       mkn=("Soto Iga Sapi")
   elif nomor==4:
        totalmkn=porsi*18000
        print (porsi," Porsi Soto Lamongan = Rp", totalmkn)
        mkn=("Soto Lamongan")
    
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es Teh Manis - Rp 5000")
   print("2. Es Jeruk - Rp 7000")
   print("3. Es Teajus - Rp 3000")

   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*5000
       print (gelas," Es Teh Manis = Rp", totalmnm)
       mnm=(" Gelas Es Teh Manis")
   elif nomor==2:
       totalmnm=gelas*7000
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*3000
       print (gelas, " Es Teajus = Rp", totalmnm)
       mnm=("Es Teajus")
    
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")
