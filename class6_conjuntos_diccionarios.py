#como contruimo suna funcion
#numero_1 y numero_2 solo viven dentro de la funcion

def mi_funcion(numero_1,numero_2):
    resultado = numero_1 + numero_2
    return resultado 
el_resultado = mi_funcion(9,10)
print(el_resultado)

caso_1 = mi_funcion(0,0)
caso_2 = mi_funcion(9,8)
caso_3 = mi_funcion(-4,-10)

print("caso 1: ",caso_1)
print("caso 2: ",caso_2)
print("caso 3: ",caso_3)

print("*"*30)

def par_o_impar(un_numero):
    if un_numero %2 == 0:
        print("soy numero par")
    else:
        print("soy un numero impar")

caso_a = par_o_impar(4)
caso_b = par_o_impar(12)
caso_c = par_o_impar(5)

print("*"*30)

#f string
un_string = "Mi arbol es un roble"
otro_string = f"La viariable un_string dice: {un_string}"

print(un_string)
print(otro_string)

print("*"*30)

#diccionarios (clave:valor)
mi_diccionario = {1:90, 2:"dos", "tres":"un helado"}

print(mi_diccionario["tres"])
print(mi_diccionario.get("tres")) #get nunca da falla
print(mi_diccionario[1])
print(mi_diccionario.keys())

print("*"*30)

#agregar al diccionario
mi_dict = dict()
print(mi_dict)

mi_dict["uno"] = "el primer valor"
print(mi_dict)

mi_dict["dos"] = "otro valor"
print(mi_dict)

mi_dict["uno"] = [1,2,3,4]
print(mi_dict)

print("*"*30)

#pop saca una clave y la guarda en una variable
guardarlo_aca= mi_diccionario.pop("tres")
print("mi key tres se guardo aca: " + str(guardarlo_aca))

print("*"*30)

#borra diccionario
mi_dict.clear()
print(mi_dict)
print("se borro")

print("*"*30)

#asignacion
edades = {"juan": 31, "maria": 19}
edades["juan"]+=10
print(edades["juan"])

#como agregar clave valor en un diccionario (no existe el add en diccionarios si en conjuntos)
numeros = {"uno":1, "dos":2}
numeros ["tres"]=3
print (numeros)

print("*"*30)

#funciones integradas (= metodos)en diccionarios
#update

mi_dict_2 = {"queso_1": "roque", "queso_2":"brie", "queso_3": "gruyere"}
mi_dict_3 = {"fruta_1":"uva","fruta_2": "datiles"}
mi_dict_2.update(mi_dict_3)
print(mi_dict_2)
print(mi_dict_3)

print(f"el diccionario combinado tiene {len(mi_dict_2)} elementos")

print(f"el diccionario 3 tiene {len(mi_dict_3)} elementos")

print("*"*30)

#in
if "queso_1" in mi_dict_2:
    print("si!!!! es una clave en el diccionario")
else:
    print("no esta")
    
if "botella" in mi_dict_2:
    print(" es una clave")
else:
    print("nop !!! no es una clave")
 
print("*"*30) 
  
#conjuntos, no admiten elementos repetidos
mi_conjunto = set()
mi_otro_conjunto = {}
#llaves con elementos se entiende como conjunto
mi_otro_conjunto2 = {1,2,3,4}
mi_conjuntos_dsd_una_lista = set([1,2,3,4,5])
print(type(mi_conjunto))
print(type(mi_otro_conjunto))
print(type(mi_otro_conjunto2))
print(type(mi_conjuntos_dsd_una_lista))

print("*"*30)

#conjunto a partir de lista
mi_conjunto2 = set([1,2,3,1,2,3])
print(mi_conjunto2)
print(len(mi_conjunto2))
mi_conjunto2.add(90)
print(mi_conjunto2)
print(90 in mi_conjunto2)
print(80 in mi_conjunto2)

mi_conjunto2.update([1,2,3,44,5,65,7,8,9,1,2,4,3,2,4])
print(mi_conjunto2)

#discard y remove remueven un numero, en caso de no encontrarlo solo remove dara error

mi_conjunto2.discard(4)
print(mi_conjunto2)

mi_conjunto2.remove(65)
print(mi_conjunto2)

mi_conjunto2.clear()
print(mi_conjunto2)

