#pregunta = input('ingrese su edad: ')
#print (type(pregunta))
#print (type(int(pregunta)))


mi_lista = [1,2,3,4]
print(type(mi_lista))
print (mi_lista)

mi_otra_lista = [5,6,7,8]
print (mi_otra_lista)

#juntar listas
sumar_lista = mi_lista + mi_otra_lista
print(sumar_lista)

#acceder a la posicion 0 = 1
print (mi_lista[0])
print (mi_lista[3])

#o recuerdo la longitud de mi lista
print (len(mi_lista))
print (mi_lista[3])

#reemplazar elemento (no se puede en un string)
mi_lista[3]=44
print(mi_lista)

#repetir listas
mi_lista_loca = [123]*3
print(mi_lista_loca)

mi_lista = [9,7,5]
conteo = mi_lista *4
print(conteo)
contar9=conteo.count(9)
print(contar9)
contar0=conteo.count(1)
print(contar0)

print("*"*60)

#funcion index (devuelve el indice de la posicion q le pasamos y sort (ordena)
mi_listita = [4,5,2,45,32]
indice_mi_listita= mi_listita.index(45)
print(indice_mi_listita)

mi_lista_a_ordenar = [34,24,54,76,12]
mi_lista_a_ordenar.sort()
print(mi_lista_a_ordenar)
mi_lista_a_ordenar.reverse()
print(mi_lista_a_ordenar)
#sorted permite guardar en una nueva variable el resultado
mi_lista_nueva_ordenada = sorted(mi_lista_a_ordenar)
print(mi_lista_nueva_ordenada)
print(mi_lista_a_ordenar)
#reverse
reversa = mi_lista_a_ordenar.reverse()
print(reversa)

print("*"*60)

#accceder a un elemento de un strig, en este caso posicion 5 = a
mi_string = 'abracabra'
print(type(mi_string))
print (mi_string[5])
#desde atras 
print(mi_string[-1])
#revanada de lista
print(mi_string[0:2])
#no trae la ultima posicion que se indica
rebanada = mi_string[1:4]
print(rebanada)

print("*"*60)

#tupla tipo de lista q no puede mutar. Se definen entre paréntesis
mi_tupla = (1,2,3,4)
mi_otra_tupla = (5,6,7,8)
print(type(mi_tupla))

sumar_tuplas = mi_tupla + mi_otra_tupla
print(sumar_tuplas)

print(len(mi_tupla))

#Puedo acceder a la posicion 3 que es la posicion 2 pero no modificarla
print(mi_tupla[2])

mi_lista_mixta = [1,33,"Juan",[2,3,4], ("aa","BB")]
print (type(mi_lista_mixta))
#accedemos a la tercera posicion
print(mi_lista_mixta[3])
#dentro de lo que me trae la tercera poscicion entro al indice 1
print(mi_lista_mixta[3][1])

print(mi_lista_mixta[3])
cambio = mi_lista_mixta[3][2]=44
print(cambio)

#agregar a la lista
mi_lista_a_rellenar = []
mi_lista_a_rellenar.append(22)
print(mi_lista_a_rellenar)

#sacar un elemento de la lista con pop
aca_mi_lista = [3,4,5,6,7]
el_ultimo_de_aca_mi_lista = aca_mi_lista.pop()
print(el_ultimo_de_aca_mi_lista)
print(aca_mi_lista)

#remove, saca la primera ocurrencia
mi_lista= [1,3,1,6,6,6]
mi_lista.remove(6)
print(mi_lista)

#transformar (casteo) una lista en una tupla, funciona a la inversa tambien
mi_lista = [1,2,3]
mi_tupla = tuple(mi_lista)
print (mi_tupla)

tupla =(1,2,3) 
print (2*tupla)






