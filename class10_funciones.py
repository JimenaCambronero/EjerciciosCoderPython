#ejemplo se scope

xx= 200

def mi_otra_funcion(a):
    return a +1

def my_function():
    mi_variable = 100
    mi_variable = mi_otra_funcion(mi_variable)
    print(mi_variable)
    print(xx)
    
#p imprimirla hay q llamarla
my_function()

mi_variable= 10

def my_function():
    mi_variable = 100
    print(f"dentro de la funcion vale: {mi_variable}")
    
#p imprimirla hay q llamarla
my_function()
print(f"fuera de la funcion vale: {mi_variable}")

#mutables
mi_lista = []
def mi_func(lis):
    lis.append(1)
   
print(mi_lista)    
mi_func(mi_lista)  
print(mi_lista)
mi_func(mi_lista)  
print(mi_lista)

#inmutables
mi_variable = 0
def mi_funcion (a):
    a = 10
print(mi_variable)
mi_funcion(mi_variable)
print(mi_variable)

print("_______q retorne________")

# para q afecte a mi variable debo return y guardarlo
mi_variable = 0

def mi_funcion(a):
    a = 10
    return a

print(mi_variable)
mi_variable= mi_funcion(mi_variable)
print(mi_variable)

print("__________devolver dos cosas____________")
def mi_funcion_devuelve_dos_cosas():
    return "elemento 1", "elemento 2"

mi_variable= mi_funcion_devuelve_dos_cosas()
print(mi_variable)
print(type(mi_variable))
#devuelve una tupla y asi puedo acceder a los elemtos por la posicion
elemento1 = mi_variable[0]
elemento2= mi_variable[1]

print(f"al principio fue creado el {elemento1} y luego el {elemento2}")

print("________ cual es el parametro y cual el argumento en el ejemplo el (9)______")
def calcular_par(parametro):
    return parametro %2 == 0

es_par = calcular_par(9)
print(es_par)

#el orden importa al momento de invocar a la funcion
def mi_funcion(primero="un valor", segundo="otro valor"):
    print(f"el primero es {primero}")
    print("el segundo es: {}".format(segundo))
    
mi_funcion(9,34)
mi_funcion(34,9)

print("."*10)

mi_funcion(primero=9, segundo=34)
mi_funcion(segundo=34, primero=9)
    
print("..........parametro por defecto.........")
mi_funcion()

