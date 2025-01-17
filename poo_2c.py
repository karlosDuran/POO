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
    #¿Que es polimorfismo ejemplo? un mismo metodo va a tener diferente comportamiento dependiendo de que objeto lo llame
    
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
            enemigo.defensa= enemigo.defensa *0
            if enemigo.vida<0:
                enemigo.morir()
            print(self.nombre,"Ha hecho",daño,"puntos de daño a",enemigo.nombre)
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
            
class Guerrero(personaje):
    #sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada=espada
        
    #sobreescribir imprecion de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-espada:",self.espada)
        
    #sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    #escoger espada
    def escoger_navaja(self):
        opcion= int(input("escoge la espada de energia: \n (1) Espada normal, daño 10, \n (2) Espada dañada, daño 6\n>>>>"))
        if opcion ==1 :
            self.espada= 10
        elif opcion == 2:
            self.espada= 6
        else:
            print("valor invalido, intente de nuevo")
            #vuelve a ejecutar el metodo
            self.escoger_navaja()

class Mago(personaje):
    #sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro=libro
        
    #sobreescribir imprecion de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-libro:",self.libro)
        
    #sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
    #escoger espada
    def escoger_libro(self):
        opcion= int(input("escoge el mejor libro: \n (1) libro de magia negra , daño 10, \n (2) libro normal, daño 6\n>>>>"))
        if opcion ==1 :
            self.libro= 10
        elif opcion == 2:
            self.libro= 6
        else:
            print("valor invalido, intente de nuevo")
            #vuelve a ejecutar el metodo
            self.escoger_libro()

mi_personaje= personaje("master chif",20,15,10,100)
arturoSuarez = Guerrero("Arutro",20,15,10,100, 5)
gandalf = Mago("gandalf",20,15,10,100, 5)

#atributos antes de la tragedia
mi_personaje.imprimir_atributos()
gandalf.imprimir_atributos()
arturoSuarez.imprimir_atributos()

#ataque a lo desgraciado
mi_personaje.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(mi_personaje)

#atributos despues del desmadre
mi_personaje.imprimir_atributos()
gandalf.imprimir_atributos()
arturoSuarez.imprimir_atributos()

#print(f"El valor de espada es: {arturoSuarez.espada}")
#variable del constructor 

#mi_personaje.imprimir_atributos()
mi_enemigo= personaje("El malo",10,50,45,100)
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()

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