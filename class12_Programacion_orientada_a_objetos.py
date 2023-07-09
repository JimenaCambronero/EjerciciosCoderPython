class Animal:
 
    def __init__(self,nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"miau! mi nombre es {self.nombre}")


mi_gata = Animal("Merlina")
mi_gato = Animal ("Mirko")
print(type(mi_gata))

mi_gata.hablar()

mi_gato.hablar()
