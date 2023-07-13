# GAME (PIEDRA, PAPEL Y TIJERA) - Eliecer Conrado - Peaku 2023

from pyfiglet import Figlet
import random
import os
import sys
import time


# Esto es una Funcion que me ayuda para limpiar la consola
# Ojo solo funciona si lo ejecutas en terminal sea de Windows o Linux.
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clear()


# Animacion para que se vea chebre :)
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size - x), j, count))
        file.flush()
        file.write("\n")

    show(0)
    for lol, item in enumerate(it):
        yield item
        show(lol + 1)
        file.write("\n")
    file.flush()


for i in progressbar(range(10), "Cargando: ", 100):
    time.sleep(0.2)
    clear()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def inicio():
    global ronda
    ronda = 0
    clear()
    # Saludo de Bienvenida :)
    f: Figlet = Figlet(font='slant')
    print(f.renderText('ARCADE - EL MANCO'))
    print(" ")

    print("Escoge un Juego para jugar")
    print(" ")
    print(" ")

    print('Opcion 1: Piedra papel o tijeras')
    print('Opcion 2: Cartas')
    print("Opcion 3: Salir")

    print(" ")
    print(" ")
    print("Para mas informacion Correo: elieje13@gmail.com")
    print(" ")
    print(" ")

    gameOpcion: str = input("Escoge una Opcion (1, 2, 3). Escribe el numero de la Opcion : ")

    print(" ")
    print(" ")

    if gameOpcion == '1':
        # Se ejecuta el Game 1
        piedra_papel_tijeras()
    elif gameOpcion == '2':
        cartas()
    elif gameOpcion == '3':
        clear()
        print('Saliendo...')
        time.sleep(3)
        clear()
        exit()
    else:
        print("Escoge un Juego o dale Opcion 3 para salir")
        time.sleep(2)
        inicio()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# Aqui estan los Games


# Este es el Game n°1 - Piedra papel y tijeras

ronda = 0
cirtuitoA = None
counterPlayer1 = 0
counterPlayer2 = 0
seguir = None
mensajeFinal = None
text1 = "Empieza"


def piedra_papel_tijeras():
    clear()
    global ronda
    resul = ronda + 0
    # Aqui empieza el Game #1
    f: Figlet = Figlet(font='slant')
    print(f.renderText('Piedra Papel y Tijeras'))
    print(" ")
    time.sleep(0.1)
    clear()

    print(f.renderText('Piedra Papel y Tijeras'))
    global counterPlayer1
    global counterPlayer2
    global text1
    # Ejecuto def rondas @@@@@@@@@@@@@@@@@@@@@@@@@@
    print(f" {text1} - RONDA {resul}  ////  Puntos : Maquina({counterPlayer2}) - Tu({counterPlayer1}) ")
    print(" ")
    print(" ")
    print(" ")

    # Opciones para jugar
    opciones: list[str] = ["piedra", "papel", "tijeras"]

    # Le mostramos las opciones que tenemos
    print(f"Opciones : Piedra, Papel y Tijeras")
    print(" ")
    print(" ")

    # Jugadores
    player1 = input("Escribe una Opcion: ").lower()
    player2 = random.choice(opciones)

    global cirtuitoA

    # Codicionales
    if player1 == opciones[0]:
        cirtuitoA = True
    elif player1 == opciones[1]:
        cirtuitoA = True
    elif player1 == opciones[2]:
        cirtuitoA = True
    else:
        cirtuitoA = False

    # Bucle While
    while not cirtuitoA:
        print(" ")
        print(" ")
        print("Seleciona una de las Opciones: Piedra, Papel o Tijeras ")
        player1 = input("Escoge para empezar a Jugar: ").lower()
        # Codicionales de nuevo
        if player1 == opciones[0]:
            cirtuitoA = True
        elif player1 == opciones[1]:
            cirtuitoA = True
        elif player1 == opciones[2]:
            cirtuitoA = True
        else:
            cirtuitoA = False


    # Resultado de Juego

    if (player1 == opciones[0] and player2 == opciones[2]) or (player1 == opciones[1] and player2 == opciones[0]) or (
            player1 == opciones[2] and player2 == opciones[1]):
        counterPlayer1 += 1
        clear()
        f: Figlet = Figlet(font='slant')
        print(f.renderText('Piedra Papel y Tijeras'))

        print(f" RONDA {resul}  ////  Puntos : Maquina({counterPlayer2}) - Tu({counterPlayer1}) ")
        print(" ")
        print(" ")
        print(" ")

        print(f"@@@@ Ganastes, {player1} le gana a {player2} @@@")
        print(f"SUMAS PUNTO, Llevas : {counterPlayer1}")
        print(" ")
        print(" ")
        print(f"Escogistes : {player1}")
        print(f"Maquina : {player2}")
        time.sleep(2)

    elif (player1 == opciones[0] and player2 == opciones[1]) or (player1 == opciones[1] and player2 == opciones[2]) or (
            player1 == opciones[2] and player2 == opciones[0]):
        counterPlayer2 += 1
        clear()
        f: Figlet = Figlet(font='slant')
        print(f.renderText('Piedra Papel y Tijeras'))

        print(f" RONDA {resul}  ////  Puntos : Maquina({counterPlayer2}) - Tu({counterPlayer1}) ")
        print(" ")
        print(" ")
        print(" ")

        print(f"@@@ Perdistes, {player2} le gana a {player1} @@@")
        print(f"LA MAQUINA SUMA PUNTO, Maquina : {counterPlayer2}")
        print(" ")
        print(" ")
        print(f"Escogistes : {player1}")
        print(f"Maquina : {player2}")
        text1 = "Seguimos"
        time.sleep(2)

    elif (player1 == opciones[0] and player2 == opciones[0]) or (player1 == opciones[1] and player2 == opciones[1]) or (
            player1 == opciones[2] and player2 == opciones[2]):
        clear()
        f: Figlet = Figlet(font='slant')
        print(f.renderText('Piedra Papel y Tijeras'))

        print(f" RONDA {resul}  ////  Puntos : Maquina({counterPlayer2}) - Tu({counterPlayer1}) ")
        print(" ")
        print(" ")
        print(" ")
        print(f"@@@ Empate, {player2} es lo mismo a {player1}@@@")
        print("NADIEN SUMA PUNTOS")
        print(" ")
        print(" ")
        print(f"Escogistes : {player1}")
        print(f"Maquina : {player2}")
        text1 = "Seguimos"
        time.sleep(2)

    else:
        counterPlayer2 += 1
        print(" ")
        print(" ")
        print(f"Perdistes, {player2} le gana a {player1}")
        print(" ")
        print(" ")
        text1 = "Seguimos"
        time.sleep(2)

    print(" ")
    print(" ")
    global seguir
    # Opcion de seguir o retirarse
    seguir = input("Siguiente Ronda? (s/n) ").lower()

    global mensajeFinal
    if counterPlayer1 > counterPlayer2:
        mensajeFinal = "Ganastes las numero de rondas ganadoras"
    elif counterPlayer1 < counterPlayer2:
        mensajeFinal = "Perdiste, Nunca me Ganaras Viejo"



    # Codicionales
    if seguir == 's':
        ronda = resul + 1
        piedra_papel_tijeras()
        clear()
        f: Figlet = Figlet(font='slant')
        print(f.renderText('Juego Terminado'))
        print(" ")
        print(f"Rondas Terminadas - Resultado Final - {resul}")
        print(" ")
        print(f" NUmero de ROndas : {resul}  ////  Puntos : Maquina({counterPlayer2}) - Tu({counterPlayer1}) ")
        print(mensajeFinal)
        print(" ")
        time.sleep(10)
    elif seguir == 'n':
        ronda = 0
        cirtuitoA = None
        counterPlayer1 = 0
        counterPlayer2 = 0
        seguir = None
        mensajeFinal = None
        print("Si te divertistes... escibeme al correo para mas Games")
        time.sleep(3)
        text1 = "Seguimos"
        inicio()
    else:
        text1 = "Seguimos, te demoras en contestar..."
        seguir = input("Siguiente Ronda? (s/n) ").lower()
        piedra_papel_tijeras()


# FIN DEL GAME N° 1
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# Este es el Game n°2 - Cartas

def cartas():
    # Aqui empieza el Game #2
    clear()
    f: Figlet = Figlet(font='slant')
    print(f.renderText('Cartas'))
    print(" ")
    time.sleep(1)
    print(" ")
    print(" ")
    print("Le voy a ser sincero no hay otro game toca que me escribas al correo:")
    print('Correo es: elieje13@gmail.com')
    print("Si de verdad quieres el game y otros mas escribeme, enserio los hare :)")
    time.sleep(10)
    inicio()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Inicio
inicio()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


clear()
print('Saliendo...')
time.sleep(5)
clear()