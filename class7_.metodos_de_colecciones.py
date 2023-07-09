#construir una agenda desde un diccionario. Ejercicio Práctico

from os import PRIO_PGRP


def test(un_valor,otro_valor):
    print("Ejecutando funcion de test, los valores pasados fueron: ", un_valor, otro_valor)
#invoco la funcion y la ejecuto las veces que se quiera

test("jimena", "jimena@hotmail.com")
test("juan", "juan@hotmail.com")

print("*"*30)

def mi_funcion(el_mensaje, el_numero):
    print(el_mensaje,el_numero)
    
print("*"*30)

def agregar_contacto(nombre, e_mail, una_agenda):
    una_agenda[nombre] = e_mail      #clave,valor
    return una_agenda                #devuelve una agenda que agrego a agenda

agenda = dict()
print(agenda)        #esta vacia
agenda = agregar_contacto ("jimena", "jimena@gmail.com", agenda)        #agrego a la agenda pisandola

#como agrego un nuevo contacto?
agenda = agregar_contacto ("juan", "juan@gmail.com", agenda)

print(agenda)
print(agenda.get("juan"))

print("*"*30)
#metodos y colecciones
mi_string = "juan".lower()
print(mi_string)

mi_string2 = "Pepito".upper()
print(mi_string2)

mi_string3 = "pedro y juan".title()
print(mi_string3)

mi_string4 = "Roma y Tremendo".count("e")
print(mi_string4)

mi_string4 = "Roma y Tremendo".count("em")
print(mi_string4)

mi_string4 = "Roma y Tremendo".count("eM")
print(mi_string4)

mi_string4 = "Roma y Tremendo".count("eM".lower())
print(mi_string4)

mi_string4 = "Roma y Tremendo".find("o")
print(mi_string4) #vevuelve posicion es como el index para las listas

mi_string4 = "Roma y Tremendo".find("ma")
print(mi_string4)

mi_string4 = "Roma y Tremendo".rfind("d")
print(mi_string4)

mi_string4 = "Roma y Tremendo".split()
print(mi_string4) #OJO devuele lista

mi_string4 = "Roma y Tremendo".split("y") #usa la y como tijera
print(mi_string4)

print("*"*30)

#borrar caracter
espacios = "---hola---"
espacios2= espacios.strip("-")
print(espacios2)

#replace
remplazo = "jimena@hotmail.com"
remplazo = "jimena@hotmail.com".replace("jimena", "juan")
print(remplazo)
remplazo = "jimena@hotmail.com".replace("a","soy el remplazo")
print(remplazo)

print("*"*30)

#extend
mi_primera_lista = [1,2,3]
mi_primera_lista.append(99)
mi_segunda_lista = ["hola", "como","estas"]
mi_primera_lista.extend(mi_segunda_lista)
print(mi_primera_lista)

print("*"*30)

#insert
mi_primera_lista.insert(3,"Me insertaron!!!")
print(mi_primera_lista)

#reverse
print("*"*30)
mi_primera_lista.reverse()
print (mi_primera_lista)

#sort
mi_lista_ = ["a", "j", "perro", "alma"]
mi_lista_.sort()
print(mi_lista_)
mi_lista_.sort(reverse=True) #ordena al reves
print(mi_lista_)

print("*"*30)

#conjuntos
#isdistjoint en conjuntos
set1 = {1,2,3}
set2 = {3,4,5}
resultado = set1.isdisjoint(set2)
print(resultado)
set1 = {1,2,3}
set2 = {4,5}
resultado = set1.isdisjoint(set2)
print(resultado)

print("*"*30)

#issubset
print({3}.issubset(set1))
print({3, "a"}.issubset(set1))

print("*"*30)

#issuperset
print((set1).issuperset({3}))
print((set1).issuperset({3, "w"}))

print("*"*30)

#unir dos conjuntos
print(set1.union(set2))

print("*"*30)

#intersection
a = {1,2,3,4,5,6,89}
b = {5,9,12,56,89}
print(a.intersection(b))

print("*"*30)

#keys diccionarios
diccionario = {1:"juan", 2:"pedro", 3:"emilia"}
print(diccionario.keys())
print("-"*10)   

#values
print(diccionario.values())
print("-"*10)   

#items
for elemento in diccionario:
    print(elemento)
 
print("-"*10)  
 
for elemento in diccionario.items():
    print(elemento) 

print("-"*10)   
    
for clave, valor in diccionario.items():
    print("la clave es: " + str(clave))
    print("el valor es: " + str(valor))
    

print("--------------AFTER AGENDA-------------------")      
#after agenda
mi_agenda = {}
mi_agenda ["nombre"] = "joaquin"
     
#buscar por valor
print(mi_agenda.get("nombre"))
print(mi_agenda.get("jijijiji","no lo encuentro"))

#eliminar
#del mi_agenda["nombre"]
#print(mi_agenda)

dato_borrado = mi_agenda.pop("nombre") #pop devuelve
print(f"el dato borrado es: {dato_borrado} y te lo guarde en la variable")

#consultar mail solo sabiendo su nombre (clave)
def consulta_agenda(nombre, agenda = {}):
    return agenda.get(nombre, False)
 
print(consulta_agenda(agenda = mi_agenda, nombre = "Joaquin"))  
def agregar_contacto(agenda, nombre, email):
    agenda[nombre]= email #clave valor
    return agenda

mi_agenda = agregar_contacto (mi_agenda, "Joaquin", "joaco@gmail.com") 
print(mi_agenda)

def borrar_contacto (agenda, nombre):
    dato_borradito = agenda.pop(nombre)
    print(f"borre correctamente el dato: {dato_borradito} que corresponde a la clave {nombre}")
    return agenda

mi_agenda = borrar_contacto(mi_agenda,"Joaquin")
print(mi_agenda)

#modificar el emal
def modifica_contacto(agenda, nombre, nuevo_email):
    agenda[nombre]=nuevo_email
    return agenda

mi_agenda = agregar_contacto (mi_agenda, "Marco", "Marco@gmail.com") 
mi_agenda = agregar_contacto (mi_agenda, "Mariana", "mari@gmail.com") 

print(mi_agenda)
mi_agenda = modifica_contacto (mi_agenda, "Marco", "MarcoTieneNuevo@gmail.com")
print(consulta_agenda("Marco", mi_agenda))

#modificar la clave
def modicar_clave_agenda(agenda, nombre, nuevo_nombre):
    dato = agenda.pop(nombre)
    agenda[nuevo_nombre]=dato
    return agenda
mi_agenda = modicar_clave_agenda(mi_agenda, "Marco", "MarcosSoyElNuevoNombre")
print(mi_agenda)







    