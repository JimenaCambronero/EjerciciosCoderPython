#try

def dividir(dividendo, divisor):
    a = dividendo
    b = divisor
    
    try:
        resultado = a/b
    except:
        print("me forzaste a dividir por 0. devuelvo none")
        resultado = None
    return resultado

res = dividir(divisor = 0, dividendo = 2)
print("-"*30)
print("resultado de la ejecucion: ",res)
print("resultado de la ejecucion: ",dividir(divisor = 10, dividendo = 200))

while(True):
    try:
        n = float(input("ingrese numero: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
        break
    except:
        print("por favor ingresar un numero: ")
    
print ("__________________ejercicio after___________________")

mi_dict = {
    int:"un valor numerico",
    list:"una lista",
    str:"un texto"
}

def imprimir(valor):
    tipo = mi_dict[type(valor)]
    print(f"He recibido como parametro: {tipo}")
    
imprimir("mensaje")
imprimir(1234)
imprimir([1,2,3])

print("__________ ejercicio 2 del after___________")
def mi_funcion (valor_1, valor2):
    tipo_1 = type(valor_1)
    tipo_2 = type(valor2)
    if tipo_1 != str or tipo_2 != str:
        return False
    else: 
        set_1 = set(valor_1)
        set_2 = set(valor2)
        return set_1.union(set_2)
    
print(mi_funcion(1, "dos")== False)
print(mi_funcion("texto", [])== False)
print(mi_funcion([], [1,2,3])== False)

print(mi_funcion("a","b") == set(["a","b"]))
print(mi_funcion ("caca", "coco")== {"c","a","o"})
