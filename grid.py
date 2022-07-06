import graphics
from random import choice
import os
from time import sleep

def gridprinter():
    print("\nCurrent Position:\n")
    if currentpos['grid'] == 'gridA':
        print(gridA[currentpos['pos']])
    elif currentpos['grid'] == 'gridB':
        print(gridB[currentpos['pos']])
    elif currentpos['grid'] == 'gridC':
        print(gridC[currentpos['pos']])


gridA = [
    0, '''[A][ ][ ]\n[ ][ ][ ]\n[ ][ ][ ]''',
    '''[ ][A][ ]\n[ ][ ][ ]\n[ ][ ][ ]''',
    '''[ ][ ][A]\n[ ][ ][ ]\n[ ][ ][ ]'''
]
gridB = [
    0, '''[ ][ ][ ]\n[A][ ][ ]\n[ ][ ][ ]''',
    '''[ ][ ][ ]\n[ ][A][ ]\n[ ][ ][ ]''',
    '''[ ][ ][ ]\n[ ][ ][A]\n[ ][ ][ ]'''
]
gridC = [
    0, '''[ ][ ][ ]\n[ ][ ][ ]\n[A][ ][ ]''',
    '''[ ][ ][ ]\n[ ][ ][ ]\n[ ][A][ ]''',
    '''[ ][ ][ ]\n[ ][ ][ ]\n[ ][ ][A]'''
]

currentpos = {'grid': 'gridB', 'pos': 2}


def mover(move):
    global currentpos
    from randomiser import randomiser
    os.system('cls' if os.name == 'nt' else 'clear')
    choice(graphics.list_of_graphics)()
    if move.lower() == 'w':
        print("\nCurrent Position:\n")
        if currentpos['grid'] == 'gridA':
            print(gridC[currentpos['pos']])

            currentpos['grid'] = 'gridC'
        elif currentpos['grid'] == 'gridB':
            print(gridA[currentpos['pos']])

            currentpos['grid'] = 'gridA'
        elif currentpos['grid'] == 'gridC':
            print(gridB[currentpos['pos']])

            currentpos['grid'] = 'gridB'
        sleep(1)
        randomiser()
    elif move.lower() == 's':
        print("\nCurrent Position:\n")
        if currentpos['grid'] == 'gridA':
            print(gridB[currentpos['pos']])

            currentpos['grid'] = 'gridB'
        elif currentpos['grid'] == 'gridB':
            print(gridC[currentpos['pos']])

            currentpos['grid'] = 'gridC'
        elif currentpos['grid'] == 'gridC':
            print(gridA[currentpos['pos']])

            currentpos['grid'] = 'gridA'
        sleep(1)
        randomiser()
    elif move.lower() == 'a':
        print("\nCurrent Position:\n")
        if currentpos['grid'] == 'gridA':
            if currentpos['pos'] == 1:
                print(gridA[3])

                currentpos['pos'] = 3
            elif currentpos['pos'] == 2:
                print(gridA[1])

                currentpos['pos'] = 1
            elif currentpos['pos'] == 3:
                print(gridA[2])

                currentpos['pos'] = 2

        elif currentpos['grid'] == 'gridB':
            if currentpos['pos'] == 1:
                print(gridB[3])

                currentpos['pos'] = 3
            elif currentpos['pos'] == 2:
                print(gridB[1])

                currentpos['pos'] = 1
            elif currentpos['pos'] == 3:
                print(gridB[2])

                currentpos['pos'] = 2

        elif currentpos['grid'] == 'gridC':
            if currentpos['pos'] == 1:
                print(gridC[3])

                currentpos['pos'] = 3
            elif currentpos['pos'] == 2:
                print(gridC[1])

                currentpos['pos'] = 1
            elif currentpos['pos'] == 3:
                print(gridC[2])

                currentpos['pos'] = 2
        sleep(1)
        randomiser()
    elif move.lower() == 'd':
        print("\nCurrent Position:\n")
        if currentpos['grid'] == 'gridA':
            if currentpos['pos'] == 1:
                print(gridA[2])

                currentpos['pos'] = 2
            elif currentpos['pos'] == 2:
                print(gridA[3])

                currentpos['pos'] = 3
            elif currentpos['pos'] == 3:
                print(gridA[1])

                currentpos['pos'] = 1

        elif currentpos['grid'] == 'gridB':
            if currentpos['pos'] == 1:
                print(gridB[2])

                currentpos['pos'] = 2
            elif currentpos['pos'] == 2:
                print(gridB[3])

                currentpos['pos'] = 3
            elif currentpos['pos'] == 3:
                print(gridB[1])

                currentpos['pos'] = 1

        elif currentpos['grid'] == 'gridC':
            if currentpos['pos'] == 1:
                print(gridC[2])

                currentpos['pos'] = 2
            elif currentpos['pos'] == 2:
                print(gridC[3])

                currentpos['pos'] = 3
            elif currentpos['pos'] == 3:
                print(gridC[1])

                currentpos['pos'] = 1
        sleep(1)
        randomiser()
    else:
        gridprinter()
        print("Enter A Proper Movement Key!")
        graphics.spacer()
