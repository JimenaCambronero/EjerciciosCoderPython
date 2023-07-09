#test casos de prueba par mayor a 18 imprimir A, impar y multiplo de 3 imprimi b otro caso imprimir valos no reconocido

from cgitb import text
from unittest import result


mi_numero = 0
valor_esperado = "valor no reconocido"

mi_numero = 1
valor_esperado = "valor no reconocido"

mi_numero = 35
valor_esperado = "valor no reconocido"

mi_numero = 2
valor_esperado = "valor no reconocido"

mi_numero = 20
valor_esperado = "A"

mi_numero = 9
valor_esperado = "B"

mi_numero = 6
valor_esperado = "valor no reconocido"


#mi programa

if (mi_numero % 2 == 0 and mi_numero > 18):
    print(".....1.....")
    resultado = "A"
elif (mi_numero %2 !=0) and (mi_numero %3 == 0):
    print(".....2.....")
    resultado = "B"
else: 
    print(".....3.....")
    resultado = "valor no reconocido"


#test
print("mi numero es: " + str(mi_numero))
print("mi valor esperado es: " + str
(valor_esperado))
assert resultado == valor_esperado

print ("termine OK")


#while (mientras- acccion que se deja de ejecutar cuando se cumple determinada condicion, pero no sabemos cuando va a suceder)y for (para-sabemos la cantidad de elementos ej el 5to en la lista)

mi_numero = 0
mi_numero += 1
print(mi_numero)

while mi_numero < 10:
    print("********", mi_numero)
    mi_numero += 1
#el else no es necesario
else:
    print ("soy el ciclo while y mi numero es: " + str(mi_numero))
    
#while con breack   
while mi_numero < 10:
    print("********", mi_numero)
    mi_numero += 1
    if mi_numero == 4:
        print ("soy el ciclo while y mi numero es: " + str(mi_numero)) 
 
print("*" *30)          
#while con input
intento1 = 1
while intento1 >= 3:
    input ("escribi cualquier cosa : ")  
    print(intento1)
    intento1 += 1
else:
    print("no hay mas posibilidad de intentos")
    
print("*" *30)  

#for
mi_lista = [1, "a", 3, True, "Jimena"]
for elemento in mi_lista:
    print(elemento)
    if elemento == 3:
        break
    
print("*" *30)  
 
#enumerate trae el indice del elemento    
mi_lista = [1, "a", 3, True, "Jimena"]
for indice, elemento in enumerate(mi_lista):
    print (indice,elemento )
    
print("*" *30) 
  
#trae el indice y devuelve una tupla
mi_lista2 = [1, "a", 3, True, "Jimena"]
for elemento in enumerate(mi_lista2):
    print (elemento )
    
#continue
mi_lista3 = [1, "a", 3, True, "Jimena"]
for elemento in mi_lista3:
    print (elemento )  
    if elemento == 3:
        print("soy un mensajito")  
    else:
        continue
    print("termino el bloque")
    
intento = 1
while intento <= 3:
    texto = input("escribe si: ")
    if texto == "SI":
        print("ok, lo conseguiste en el intento: ", intento)
        break
    intento += 1
else:
        print("Agostaste intentos")
        
texto1= "Hola Mundo, estoy usando un for en Python"
texto2 = ""
for letra in texto1:
    print(texto2)
    texto2 = letra * 2
    
print(texto2)

print("*" *30) 

#range generar rangos
#de 0 hasta el final -1
for numero in range(10):
    print(numero)

print("*" *30) 

for numero1 in range(11):
    print(numero1)  
    
print("*" *30)      

#range con (inicio, fin) desde el numero que se le indica hasta fin -1
for numero2 in range(11,22):
    print(numero2) 
    
print("*" *30)   
 
#range(inicio, fin, paso)
for numero3 in range(33,44,2):
    print(numero3)    


