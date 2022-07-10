import graphics
from random import choice
import os
from time import sleep

def gridprinter():
    graphics.print_centre("\nWorld Map:\n")
    if currentpos['grid'] == 'gridA':
        print(gridA[currentpos['pos']])
    elif currentpos['grid'] == 'gridB':
        print(gridB[currentpos['pos']])
    elif currentpos['grid'] == 'gridC':
        print(gridC[currentpos['pos']])


gridA = [
    0, '''[P][ ][ ]\n[ ][ ][ ]\n[ ][ ][ ]''',
    '''[ ][P][ ]\n[ ][ ][ ]\n[ ][ ][ ]''',
    '''[ ][ ][P]\n[ ][ ][ ]\n[ ][ ][ ]'''
]
gridB = [
    0, '''[ ][ ][ ]\n[P][ ][ ]\n[ ][ ][ ]''',
    '''[ ][ ][ ]\n[ ][P][ ]\n[ ][ ][ ]''',
    '''[ ][ ][ ]\n[ ][ ][P]\n[ ][ ][ ]'''
]
gridC = [
    0, '''[ ][ ][ ]\n[ ][ ][ ]\n[P][ ][ ]''',
    '''[ ][ ][ ]\n[ ][ ][ ]\n[ ][P][ ]''',
    '''[ ][ ][ ]\n[ ][ ][ ]\n[ ][ ][P]'''
]

currentpos = {'grid': 'gridB', 'pos': 2}


def mover(move):
    global currentpos
    from randomiser import randomiser
    graphics.clrscrn()
    graphics.dungeon()
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
