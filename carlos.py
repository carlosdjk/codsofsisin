#conversor de divisas
 
#calcular en base a un valor dado por el usuario
#su equivalencia en las diferentes divisas definidas 

#china
yuan=2.81
#japon
yen=0.14
#estados unidos
dolar=20.49
#union
euro=21.28
#reino unido
libra=25.5

pesos =input("ingresa la cantidad de pesos a convertir")
peso=int(pesos)
print("los pesos equivalen a")
 
print("son %.2f yuanes" %(peso/yuan))
print("son %.2f jenes " %(peso/yen))
print("son %.2f dolares" %(peso/dolar))
print("son %.2f euros" %(peso/euro))
print("son %.2f libras" %(peso/libra))
 
