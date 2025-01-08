class personaje:
    #atributos de la clase
    nombre="Default"
    fuerza=0
    inteligencia=0
    defensa=0
    vida=0

#variable del constructor vacio 
mi_personaje= personaje()
#modificando valores de los atributos
mi_personaje.nombre="jhon 117"
mi_personaje.fuerza=200000
mi_personaje.inteligencia=44
mi_personaje.defensa=44
mi_personaje.vida=1

print("El nombre de mi personaje es: ",mi_personaje.nombre)
print("La fuerza mi personaje es: ",mi_personaje.fuerza)
print("La inteligencia de mi personaje es: ",mi_personaje.inteligencia)
print("La defensa de mi personaje es: ",mi_personaje.defensa)
print("La vida de mi personaje es: ",mi_personaje.vida)