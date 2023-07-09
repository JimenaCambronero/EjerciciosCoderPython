import random 
import json

#inicializar una agenda con contenido
mi_agenda = {"juan" : "juan@gmail.com"}

#inicializar una agenda vacia y agregar contenido
mi_otra_agenda = dict()

mi_otra_agenda ["juan"] = "juan@gmail.com"
mi_otra_agenda ["juanito"] = "juanito@gmail.com"
mi_otra_agenda ["maria"] = "maria@gmail.com"

print(mi_otra_agenda)

#borro un contacto
del mi_otra_agenda["juanito"]
print(mi_otra_agenda)

#pop guarda en una variable el elemento eliminado
guardo_maria = mi_otra_agenda.pop("maria")
print(guardo_maria)

def guardar_contacto_agenda(nombre, email, agenda):
    agenda[nombre]= email
    return agenda

mi_agenda = dict()
nombre = "arya"
email = "aria@gmail.com"
print("primera version: ", mi_agenda)

mi_agenda = guardar_contacto_agenda (nombre, email, mi_agenda)
print("segunda version: ", mi_agenda)

print("---"*10)

#ejemplo crear y escribir archivo
mi_variable_aleatoria = random.random()
print(mi_variable_aleatoria)

mi_archivo = open("mi_archivo_test.py","w")

mi_archivo.write(str(mi_variable_aleatoria))

#como leer
mi_archivo = open("mi_archivo_test.py","r")

lineas_archivo = mi_archivo.read()

# breakpoint() comandos l y c para continuar

print("el contenido del archivo es: ", lineas_archivo)
mi_archivo.close()

print("________________con json _______________")
mi_agenda = {"bruce":"bruce@gmail.com", "michael": "michael@gmail.com" }
mi_archivo = open("cantantes.txt", "w")
mi_archivo.write(json.dumps(mi_agenda))
mi_archivo.close()
mi_archivo = open ("cantantes.txt","r")
mi_agenda_recuperada = json.loads(mi_archivo.read())

print(mi_agenda_recuperada)
print(type(mi_agenda_recuperada))


