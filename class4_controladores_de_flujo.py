#devuelve error
mi_variable = False 
#assert mi_variable

print("*" *40)

#no devuelve nada
mi_variable = True
assert mi_variable

mi_numero = 5
mi_variable = mi_numero >4
assert mi_variable

print("*"*60)

nombre = "Jimena" 
edad = 40

cond_1 = nombre != "****"
cond_2 = edad > 10 and edad < 18
cond_3 = len(nombre) >= 3 and len(nombre)< 10
cond_4 = edad * 4 > 40

mi_variable = cond_1 and cond_2 and cond_3 and cond_4
print("cond 1: " + str(cond_1))
print("cond 1: " + str(cond_2))
print("cond 1: " + str(cond_3))
print("cond 1: " + str(cond_4))

print("Mi variable es: " + str(mi_variable))

print("*"*60)

#else if
mi_edad = 19
mi_variable = mi_edad >= 18
tipo_de_entrada = "Es mayor" if mi_variable else "Es menor"
print(tipo_de_entrada)

print("*"*60)

if 3 > 2:
    print("se cumple")
    print("imprimo todos los prints de la condicion q se cumple")
else: 
    print("no se cumple")
    
print("*"*60)    

if 1 > 2:
    print("se cumple")
else: 
    print("no se cumple")
    
print("*"*60)

#elif
mi_edad = 17

if mi_edad <= 6:
    print("Nivel inicial")
else:
    if mi_edad > 5 and mi_edad <=12:
        print("Nivel primario")
    else:
        if mi_edad >12 and mi_edad <=17:
            print("Nivel secuendario")
        else: 
            if mi_edad > 17:
                    print("Nivel universitario")
    
print("*"*60)   

if mi_edad <= 18:
    print("Nivel inicial")
elif mi_edad > 5 and mi_edad <=12:
    print("Nivel primario")
elif mi_edad >12 and mi_edad <=17:
    print("Nivel secuendario")
elif mi_edad > 17:
    print("Nivel universitario")
    
mi_variable = 20 > 150
mi_otra_variable = "jimena" == "jimena"

#imprimir para saber si es True o False
print("mi variable es: " + str(mi_variable))
print("mi otra variable es: " + str(mi_otra_variable))

if mi_variable and mi_otra_variable:
    print("ambas son verdaderas")
else:
    print("al menos una no es verdadera")