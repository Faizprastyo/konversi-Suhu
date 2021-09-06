def konversiSuhu():
    
    temp = int(suhu [:-1])
    satuan = suhu[-1]
##############################
    print(40*"=")

# CELCIUS
    if satuan.upper () == "C":
    	hasil1 = float( (9/5) * temp + 32)
    	hasil2 = float(temp + 273)
    	hasil3 = float( (4/5) * temp)
    	print (suhu, "=", hasil1, "Fahrenheit")
    	print (suhu, "=", hasil2, "Kelvin")
    	print (suhu, "=", hasil3, "Reamur")
	
# ==========FAHRENHEIT==========
    elif satuan.upper () == "F":
    	hasil1 = float(( temp-32 ) * 5/9  )
    	hasil2 = float(temp + 273 )
    	hasil3 = float(4/9 * (temp-32 ))
    	print (suhu, "=", hasil1, "Celcius")
    	print (suhu, "=", hasil2, "Kelvin")
    	print (suhu, "=", hasil3, "Reamur")
	
# ==========KELVIN==========
    elif satuan.upper () == "K":
    	hasil1 = float( temp - 273)
    	hasil2 = float( ( temp - 273) * 9/5 + 32 )
    	hasil3 = float( 4/5 * (temp-273) )
    	print (suhu, "=", hasil1, "Celcius")
    	print (suhu, "=", hasil2, "Fahrenheit")
    	print (suhu, "=", hasil3, "Reamur")
	
# ==========REAMUR==========*
    elif satuan.upper () == "R":
    	hasil1 = float( (5/4) * temp )
    	hasil2 = float( (9/4 * temp) + 32 )
    	hasil3 = float( (5/4 * temp) + 273 )
    	print (suhu, "=", hasil1, "Celcius")
    	print (suhu, "=", hasil2, "Fahrenheit")
    	print (suhu, "=", hasil3, "Kelvin")
	
    else :
       print("Ada yang salah nih, masukan input dengan benar")
       
i=0
print(10*"=", "PROGRAM KONVERSI SUHU", 10*"=")
while (i==0):
    suhu = input("masukan suhu. contoh 10C, 10K, 10F, 10R :" )
    konversiSuhu()
    
    print (40*"=")
    lagi=int(input("coba lagi?. 1=ya, 0=berhenti"))
    if (lagi==1):
    	i=0
    elif (lagi!=1):
    	i=1