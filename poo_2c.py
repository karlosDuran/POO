class personaje:
    #atributos de la clase
    #nombre="Default"
    #fuerza=0
    #inteligencia=0
    #defensa=0
    #vida=0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
    #¿Qué es self? es una referencia al mismo objeto
    #que el el metodo init? constructor que inicializa los atributos de un objeto
    #pq se usa doble guion bajo? Dunder. porque es un metodo magico.
    #cuando se ejecuta el metodo init? Autom. al crear una nueva instacia u objeto
    def imprimir_atributos(self):
        print(self.nombre)
        print("-fuerza:",self.fuerza)
        print("-inteligencia:",self.inteligencia)
        print("-defensa:",self.defensa)
        print("-vida:",self.vida)
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def está_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida=0
        print(self.nombre,"ha muerto")
        
    def dañar(self,enemigo):
        return self.fuerza - enemigo.defensa 
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if daño<0:
            enemigo.defensa=enemigo.defensa-self.fuerza
            print(self.nombre,"Ha hecho",self.fuerza,"puntos de daño a la defensa a",enemigo.nombre)
            print("la defensa de", enemigo.nombre, "es", enemigo.defensa)
        else:
            enemigo.vida = enemigo.vida- daño
            if enemigo.vida<0:
                enemigo.morir()
            print(self.nombre,"Ha hecho",daño,"puntos de daño a",enemigo.nombre)
            print("Vida de", enemigo.nombre, "es", enemigo.vida)

#variable del constructor 
mi_personaje= personaje("master chif",150,50,45,100)
mi_personaje.imprimir_atributos()
mi_enemigo= personaje("El malo",10,50,45,100)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()

# mi_personaje.subir_nivel(15,20,30)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()
#modificando valores de los atributos
#mi_personaje.nombre="jhon 117"
#mi_personaje.fuerza=200000
#mi_personaje.inteligencia=44
#mi_personaje.defensa=44
#mi_personaje.vida=1

#print("El nombre de mi personaje es: ",mi_personaje.nombre)
#print("La fuerza mi personaje es: ",mi_personaje.fuerza)
#print("La inteligencia de mi personaje es: ",mi_personaje.inteligencia)
#print("La defensa de mi personaje es: ",mi_personaje.defensa)
#print("La vida de mi personaje es: ",mi_personaje.vida)