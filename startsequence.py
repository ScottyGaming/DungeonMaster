import graphics
import os
from os.path import exists
from random import choice
from variables import load
from time import sleep
key = 0


#---Start---#
def charpicker():
  import variables
  
  while True:
    graphics.introduction()
    graphics.print_centre("--- Enter you Gender (this affects choices and obtainable gear) ---  ")
    for i in variables.genlist:
      graphics.print_centre(i)
    x=input(f'Choice: ')
    if x == None:
      print(f"You have to choose a Gender!")
    if x.lower() == 'female':
      variables.gender = 'Female'
      print(f"You have chosen {variables.gender}!")
      sleep(1)
      break
    elif x.lower() == 'male':
      variables.gender = 'Male'
      print(f"You have chosen {variables.gender}!")
      sleep(1)
      break
    else:
      graphics.clrscrn()
def story():
  import messages
  storylst = messages.storylst
  for j in storylst:     
      graphics.introduction()
      graphics.print_centre(j)
      input("\nPress any key to continue")
      graphics.clrscrn()
  

#######################################################################################################################
# SAVE GAME CHECKER #
#######################################################################################################################
def savepicker():
    pat = os.listdir()
    files = []
    for i in pat:
        if i.endswith(".dat"):
          files.append(i)
          
    while True:
        graphics.floppy()
        graphics.print_centre("-- SAVE MANAGER --")
        graphics.print_centre("1: load save")
        graphics.print_centre(" 2: list saves")
        graphics.print_centre("3: Exit Menu")
        cho = input("Enter choice: ")
        graphics.spacer()
      
        if cho == '1':
          filename = input("Enter save name: ")
          filename = filename+'.dat'
          if filename in files:
            print(f"Loading {filename}...")
            sleep(1)
            load(filename)
            global key
            key = 1
            break
            
          else:
            print("Invalid Save!")
            sleep(1)
            graphics.clrscrn()
            
        elif cho == '2':
          print('-- Save List --')
          for i in files:
            print(i[:-4:])
          input("Press any key to go back to save menu!")
          graphics.clrscrn()
          
        elif cho == '3':
          graphics.clrscrn()
          break

        else:
          print("Invalid Choice!")
          sleep(1)
          graphics.clrscrn()
      
#######################################################################################################################  
#######################################################################################################################
          
def startmenu():
    while True:
      graphics.logo()
      graphics.print_centre("|  1) New Game   |")
      graphics.print_centre("|  2) Load Game  |")
      graphics.print_centre("|  3) Quit Game  |")
      x=input(": ")
      if x=='1':
        graphics.clrscrn()
        story()
        charpicker()
        graphics.clrscrn()
        graphics.dungeon()
        from grid import gridB,currentpos
        print(gridB[currentpos['pos']])
        break
        
      elif x=='2':
        graphics.clrscrn()
        savepicker()
        if key == 1:
          break

      elif x=='3':
        graphics.clrscrn()
        os._exit(0)
      else:
        graphics.clrscrn()
        
def pausemenu():
    while True:
      graphics.logo()
      x=input("-- PAUSE MENU --\n\n1) New Game\n2) Load Game\n3) Save Game\n4) Back to Game\n5) Quit Game\n: ")
      if x=='1':
        graphics.clrscrn()
        story()
        graphics.clrscrn()
        graphics.dungeon()
        from grid import gridB,currentpos
        print(gridB[currentpos['pos']])
        break
        
      elif x=='2':
        graphics.clrscrn()
        savepicker()
        if key == 1:
          break

      elif x=='5':
        graphics.clrscrn()
        os._exit(0)
      elif x=='4':
        break
      elif x=='3':
        import variables
        variables.save()
        sleep(1)
        graphics.clrscrn()
        
      else:
        print("Invalid Choice!")
        sleep(1)
        graphics.clrscrn()
        
def startsequence():
    graphics.logo()
    print()
    graphics.print_centre("Credits: Scottminer22 Gaming#2306")
    graphics.print_centre("Press any key to start!")
    input()
    graphics.clrscrn()
    startmenu()
    graphics.clrscrn()
    graphics.dungeon()
    from grid import gridB,currentpos
    print("\nCurrent Position:\n")
    print(gridB[currentpos['pos']])
        

