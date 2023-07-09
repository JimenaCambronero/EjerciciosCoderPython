mi_booleano = True
print(mi_booleano)

# negacion
print(not mi_booleano)

mi_booleano2 = False
print(mi_booleano2)

comparacion = mi_booleano == "Hola"
print(comparacion)

comparacion2 = 1+1 == 3
print(comparacion2)

comparacion3 = 1+1 == 2
print(comparacion3)

comparacion4 = comparacion2 != comparacion3
print(comparacion4)

mayor = 5 > 6
print(mayor)

mayor_igual = 6 >= 6
print(mayor_igual)

print("*"*60)

# comparar strings
comparar_string = "Jimena" == "Jimena"
print(comparar_string)

comparar_string1 = "Jimena" == "jimena"
print(comparar_string1)

comparar_string2 = "Jimena".lower() == "jimena"
print(comparar_string2)

print("*"*60)

# True es 1 False es 0
suma = True + 1
print(suma)

suma2 = False + 3
print(suma2)

multiplicar = True * 5
print(multiplicar)

mi_expresion_en_una_lista = [1 == 2]
print(mi_expresion_en_una_lista)

mi_expresion_en_una_lista = [1 == 2, "jimena" == "Gisele", False > True]
print(mi_expresion_en_una_lista)

#operador OR (alguna es verdadera?)
operador_or = True or False
print(operador_or)

operador_or = False or False
print(operador_or)

operador_or = 1==1 or 2==2
print(operador_or)

operador_or = 1==1 or 2==3
print(operador_or)

operador_or = 10==1 or 20==2
print(operador_or)

operador_or = 10==1 or not 20==2
print(operador_or)

#operador AND 
operador_or = True and False
print(operador_or)

operador_or = False and False
print(operador_or)

operador_or = 1==1 and 2==2
print(operador_or)

operador_or = 1==1 and 2==3
print(operador_or)

operador_or = 10==1 and 20==2
print(operador_or)

operador_or = 10==1 and not 20==2
print(operador_or)

#ejemplo ejerciocio. Sumar los elementos de una lista y agregarlo

datos = [
    [1,5,1],
    [2,1,2],
    [3,0,1],
    [1,4,4]
]

#solucion 1
#imprime la primera lista de la lista
#(datos[0].append("agrego la suma calculada en mi cerebro"))
#print(datos)

#solucion2
(datos[0]).append(sum(datos[0]))
print(datos)
(datos[1]).append(sum(datos[1]))
print(datos)
(datos[2]).append(sum(datos[2]))
print(datos)
(datos[3]).append(sum(datos[3]))
print(datos)

#otra solución
#Este programa agrega a la lista con listas anidadas, un cuarto elemento que es el resultado de sumar los tres primeros.
 
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
#Opción 1.
matriz[0] += [sum(matriz[0])]
matriz[1] += [sum(matriz[1])]
matriz[2] += [sum(matriz[2])]
matriz[3] += [sum(matriz[3])]

#Opción 2.

matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz)