#funciones, encapsular codigo y repetirlo
mi_numero = 15
if mi_numero % 5 == 0:
    print("Soy multiplo de 5")
else:
    print("No soy multiplo de 5")
    
print("_______________con funcion_________________")
# como probarlo con todos los numeros
def mi_funcion(mi_numero):
    if mi_numero % 5 == 0:
        print("Soy multiplo de 5")
    else:
        print("No soy multiplo de 5")
        
#llamo a la funcion
mi_funcion(15)
mi_funcion(8)
mi_funcion(150)
mi_funcion(22)


print("_______________misma funcion con return_________________")
# como probarlo con todos los numeros
def mi_funcion(mi_numero):
    if mi_numero % 5 == 0:
        return "Soy multiplo de 5"
    else:
        return "No soy multiplo de 5"
        
#llamo a la funcion
retorno1  = mi_funcion(15)
retorno2 = mi_funcion(8)
retorno3  = mi_funcion(150)
retorno4  = mi_funcion(22)
print(retorno1)
print(retorno2)
print(retorno3)
print(retorno4)

print("_______________contar letras con una funcion_________________")

#calcular si una palabra tiene mas de 10 letras

def calcular_letras(palabra):
    longitud=len(palabra)
    if longitud >10:
        return True
    else:
        return False

retorno9= calcular_letras("casa")
retorno8= calcular_letras("tremendacasa")
print(retorno9)
print(retorno8)
