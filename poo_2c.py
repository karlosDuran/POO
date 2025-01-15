class personaje:
    #atributos de la clase
    #nombre="Default"
    #fuerza=0
    #inteligencia=0
    #defensa=0
    #vida=0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre=nombre
        self.__fuerza=fuerza
        self.__inteligencia=inteligencia
        self.__defensa=defensa
        self.__vida=vida
    #¿Qué es self? es una referencia al mismo objeto
    #que el el metodo init? constructor que inicializa los atributos de un objeto
    #pq se usa doble guion bajo? Dunder. porque es un metodo magico.
    #cuando se ejecuta el metodo init? Autom. al crear una nueva instacia u objeto
    def imprimir_atributos(self):
        print(self.__nombre)
        print("-fuerza:",self.__fuerza)
        print("-inteligencia:",self.__inteligencia)
        print("-defensa:",self.__defensa)
        print("-vida:",self.__vida)
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def está_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida=0
        print(self.__nombre,"ha muerto")
        
    def dañar(self,enemigo):
        return self.__fuerza - enemigo.__defensa 
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if daño<0:
            enemigo.__defensa=enemigo.__defensa-self.__fuerza
            print(self.__nombre,"Ha hecho",self.__fuerza,"puntos de daño a la defensa a",enemigo.__nombre)
            print("la defensa de", enemigo.__nombre, "es", enemigo.__defensa)
        else:
            enemigo.__vida = enemigo.__vida- daño
            if enemigo.__vida<0:
                enemigo.morir()
            print(self.__nombre,"Ha hecho",daño,"puntos de daño a",enemigo.__nombre)
            print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
    
    def get_vida(self):
        return self.__vida
    
    def set_vida(self, vida_extra):
        self.__vida=vida_extra
        #self.__vida=vida_extra if vida_extra>0 else self.morir()

#variable del constructor 
mi_personaje= personaje("master chif",15,50,45,100)
mi_enemigo= personaje("El inquisidor",10,50,45,100)

print(mi_personaje.get_vida())
#mi_personaje.set_vida(-5)
print(mi_personaje.get_vida())
mi_personaje._personaje__vida= -50
mi_personaje.imprimir_atributos()



# mi_personaje.imprimir_atributos()

#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()

# mi_personaje.subir_nivel(15,20,30)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()
#modificando valores de los atributos
#mi_personaje.__nombre="jhon 117"
#mi_personaje.__fuerza=200000
#mi_personaje.__inteligencia=44
#mi_personaje.__defensa=44
#mi_personaje.__vida=1

#print("El nombre de mi personaje es: ",mi_personaje.__nombre)
#print("La fuerza mi personaje es: ",mi_personaje.__fuerza)
#print("La inteligencia de mi personaje es: ",mi_personaje.__inteligencia)
#print("La defensa de mi personaje es: ",mi_personaje.__defensa)
#print("La vida de mi personaje es: ",mi_personaje.__vida)