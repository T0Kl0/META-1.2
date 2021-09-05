from random import randint

escoger=["piedra","papel","tijeras"]
comp=escoger[randint(0,2)]
print ("BIENVENIDO AL JUEGO PIEDRA PAPEL O TIJERA")
jug = input ("ESCOGE ALGUNA OPCION ").lower()
print("LA COMPUTADORA ESCOGIO: " + comp)

if jug == comp:print("Empate")
elif jug=="piedra" and comp=="papel":print ("Gano la maquina")
elif jug=="piedra" and comp=="tijeras":print ("Gano el jugador")
elif jug=="papel" and comp=="piedra":print ("Gano el jugador")
elif jug=="papel" and comp=="tijeras":print ("Gano la maquina")
elif jug=="tijeras" and comp=="piedra":print ("Gano la maquina")
elif jug=="tijeras" and comp=="papel":print ("Gano el jugador")

