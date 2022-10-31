"""
La computadora asignar una palabra para tratar de ser descubierta => obtenido de un txt con muchas palabras
Mostrar cantidad de guiones por igual cantidad de letras de la palabra seleccionada  => lambda
Dar opcion al jugador de ingresar una letra y verificar si es correcta, agregarla en lugar de un guion o si no, lanzar error y descontar una vida

Opcional = dibujo con el personaje
"""
import random

# Abrimos el documento txt con las palabras y tomamos sus lineas
with open('palabras.txt', 'r') as palabras:
    listaPalabras = palabras.readlines()

# Enprolijamos las lineas dejando una lista unica con valores para tomar
listaPalabras = [l.replace('\n', '') for l in listaPalabras]

# Esta variable guardara la palabra que sera la que el usuario deba adivinar
palabraRandom = random.choice(listaPalabras)

# Formato inicial en que se mostraran las palabras al usuario
espaciosPalabra = ((len(palabraRandom)) * '_')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Cantidad de vidas que tiene el jugador
counterLife = 6

# Funcion que en base a la cantidad de vidas imprime un dibujo del muñeco


def printHangmanMan():
    if counterLife == 6:
        print(HANGMANPICS[0])
    elif counterLife == 5:
        print(HANGMANPICS[1])
    elif counterLife == 4:
        print(HANGMANPICS[2])
    elif counterLife == 3:
        print(HANGMANPICS[3])
    elif counterLife == 2:
        print(HANGMANPICS[4])
    elif counterLife == 1:
        print(HANGMANPICS[5])
    else:
        print(HANGMANPICS[6])


def juego():
    global counterLife
    palabraDef = []
    for l in palabraRandom:
        palabraDef.append(l)

    espaciosDef = []
    for e in espaciosPalabra:
        espaciosDef.append(e)

    while True:
        printHangmanMan()
        # Ingreso de letra del usuario
        letra = input('Ingrese una letra para saber si está ')

        # Verificacion de que la letra este
        if letra not in palabraDef:
            print('La letra ' + str(letra) + ' no está')
            counterLife -= 1
            print('Usted tiene ' + str(counterLife) + ' vidas')
            # letra = input('Ingrese una letra para saber si está ')

        # Evalua la cantidad de vidas que tenes, al llegar a 0 da la partida por perdida
        if counterLife == 0:
            print('Perdiste')
            print('La palabra era ' + palabraRandom)
            break
        elif counterLife < 0:
            break

        # Toma los indices de la letra dada, en cada aparición, para luego trabajar con ellos
        indexes = [i for i in range(len(palabraDef)) if palabraDef[i] == letra]

        # Recorre la lista de indices y va limpiando el '-' en su lugar e insertado la letra correspondiente hasta formar la palabra
        for i in range(len(indexes)):
            index = indexes[i]
            espaciosDef.pop(index)
            espaciosDef.insert(index, str(letra))

        # Imprime el estado de la palabra en el juego
        palabraFinal = "".join(espaciosDef)
        for l in palabraFinal:
            print(l, end=' ')

        # Analiza la cantidad de guiones tras todo el recorrido, si es 0, ganaste, sino sigue el bucle.
        if espaciosDef.count('_') == 0:
            print('Felicitaciones ganaste')
            break


def inicio():
    print('Comienza el juego, a continuación se muestra la palabra ')
    for e in espaciosPalabra:
        print(e, end=' ')
    juego()


inicio()
