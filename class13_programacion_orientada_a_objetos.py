
class Gata:
    def __init__(self, nombre, madre):
        self.nombre = nombre
        self.madre = madre
        self.patas = 4
      

aceituna = Gata("Aceituna", "Manuela")

print(aceituna.nombre)
print(aceituna.patas)
print(aceituna.madre)


class Gata2:
    
    patas = 4
    def __init__(self, nombre, madre):
        self.nombre = nombre
        self.madre = madre
    def mostrarse(self):
        print(self.nombre)
        print(self.madre)
        print(self.patas)
        print(type(self))
        
merlina= Gata2("Merlina", "Angelina")   
merlina.mostrarse()     
      

class Gata3:
    def __init__(self, nombre):
        self.nombre= nombre
    def decir_nombre (self):
        print(f"miau! soy {self.nombre}")
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
mirko = Gata3 ("Mirko")
mirko.decir_nombre()
mirko.cambiar_nombre("MirkoBello")
mirko.decir_nombre()

class Perro:
    
    #atributo e la clase
    especie = "mamifero"
    
    #constructor de la clase
    def __init__(self, nombre, raza):
        
        #atributos de la instancia
        self.nombre = nombre
        self.raza = raza
        
    #metodos
    def ladrar(self):
        print("Este perro ha ladrado")
    def caminar(self, pasos):
        print(f"Este perro ha caminado {pasos} pasos")

perro1 = Perro("sammy", "caniche")
print(f"Su nombre es: {perro1.nombre}")
print(f"Su raza es : {perro1.raza}")
print(f"Es un: {perro1.especie}")

perro1.ladrar()
perro1.caminar(5)

class Persona:
    #atributos de la clase
    reloj = "casio"
    sombra = True
    
    #atributos de instancia
    def __init__(self, nombre, segundo_nombre, pais):
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre
        self.pais = pais
    #metodos    
    def presentarse(self):
        print (f"Buenas noches, mi nombre es {self.nombre}, {self.segundo_nombre} y estoy en {self.pais}")  
    def cambiar_pais(self,pais):
        self.pais = pais
        print(f"he cambiado de pais, ahora estoy en {self.pais}")
        
persona1 = Persona("jimena", "gisele", "Puerto Rico")
persona2 = Persona ("Juan", "Roberto", "Argentina")      
        
persona1.presentarse()
persona2.presentarse()
persona2.cambiar_pais("España")
persona2.presentarse()
