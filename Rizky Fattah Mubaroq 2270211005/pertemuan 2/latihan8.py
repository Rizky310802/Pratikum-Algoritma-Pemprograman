#Latihan konversi satuan temperature
#program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius=float(input('masukan suhu dalam celcius:'))
print("suhu adalah",celcius,"Celcius")
#reamur
reamur=(4/5)*celcius
print("suhu dalam reamur adalah", reamur,"Reamur")
#fahrenheit
fahrenheit=((9/5)*celcius)+32
print("suhu dalam fahtrenheit adalah", fahrenheit, "fahrenheit")
#kelvin
kelvin=celcius+273
print("suhu dalam kelvin",kelvin,"kelvin")