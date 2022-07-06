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
    print('''  _____       _                 _            _   _             
 |_   _|     | |               | |          | | (_)            
   | |  _ __ | |_ _ __ ___   __| |_   _  ___| |_ _  ___  _ __  
   | | | '_ \| __| '__/ _ \ / _` | | | |/ __| __| |/ _ \| '_ \ 
  _| |_| | | | |_| | | (_) | (_| | |_| | (__| |_| | (_) | | | |
 |_____|_| |_|\__|_|  \___/ \__,_|\__,_|\___|\__|_|\___/|_| |_|
                                                               
                                                               ''')
    print("--- Enter you Gender (this affects choices and obtainable gear) ---  ")
    x=input(f'Choosable Genders: {variables.genlist}\n: ')
    if x == None:
      print(f"You have to choose a Gender!")
      sleep(1)
    if x.lower() == 'female':
      variables.gender = 'female'
      print(f"You have chosen {variables.gender}! You cannot change this manually again!")
      sleep(1)
      break
    elif x.lower() == 'male':
      variables.gender = 'male'
      print(f"You have chosen {variables.gender}! You cannot change this manually again!")
      sleep(1)
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
    
      
def story():
  storylst = ["Tullius: Hey, you. You're finally awake",
              "Player: Who are you?",
              "Tullius: I am Tullius! Your guide through this wonderful enchanted land!",
              "Player: Oh nice! I have a guide!",
              "Tullius: Damn kobolds keep robbing innocent travelers right? Here have some berries!",
              "Player: Thanks!",
              "Tullius: By the way , are you a rogue or even a warrior perhaps?",
              "Player: Well yes I am a warrior! , How did you find that out?",
              "Tullius: You have armor stowed away in your bag! I can sense anything hidden!",
              "Player: ... Damm, Thats a neat trick! No use hiding it once it's found out!",
              "Tullius: I know right! Looks like we can get started!",
              "Tullius: Press 'WASD' to move (Thats how you get around)",
              "Tullius: Press 'I' to access your inventory (Thats how you store and use consumables!)",
              "Tullius: Press 'V' to view your stats (A regular health check is good!)",
              "Tullius: Press 'M' if you want to open the pause menu! (You'll need it)",
              "Tullius: Press 'Z' if you want to open the Armory! (You can view and equip Armor and Weapons!)",
              "Tullius: Press 'B' if you want to open the Shop! (You can buy armor pieces here!)",
              "Tullius: Press 'T' for summoning me! I'll give you tips that are useful for your journey!",
              "Player: Thanks for the starting tips! I'm sure that is helpful!",
              "Tullius: Well then, off you go. Slay monsters and bring peace to this once peaceful land!",
              "*distant growling and destruction can be heard in the background"]
  
  for i in range(0,len(storylst)):
    print('''  _____       _                 _            _   _             
 |_   _|     | |               | |          | | (_)            
   | |  _ __ | |_ _ __ ___   __| |_   _  ___| |_ _  ___  _ __  
   | | | '_ \| __| '__/ _ \ / _` | | | |/ __| __| |/ _ \| '_ \ 
  _| |_| | | | |_| | | (_) | (_| | |_| | (__| |_| | (_) | | | |
 |_____|_| |_|\__|_|  \___/ \__,_|\__,_|\___|\__|_|\___/|_| |_|
                                                               
                                                               ''')
    for j in storylst[i]:     
      print(j,end='')
    print()
    input("\nPress any key to continue")
    os.system('cls' if os.name == 'nt' else 'clear')
  

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
        cho = input("-- SAVE MANAGER -- \n1: load save\n2: list saves\n3: Exit Menu\nEnter choice: ")
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
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif cho == '2':
          print('-- Save List --')
          for i in files:
            print(i[:-4:])
          input("Press any key to go back to save menu!")
          os.system('cls' if os.name == 'nt' else 'clear')
          
        elif cho == '3':
          os.system('cls' if os.name == 'nt' else 'clear')
          break

        else:
          print("Invalid Choice!")
          sleep(1)
          os.system('cls' if os.name == 'nt' else 'clear')
      
#######################################################################################################################  
#######################################################################################################################
          
def startmenu():
    while True:
      graphics.logo()
      x=input("\n1) New Game\n2) Load Game\n3) Quit Game\n: ")
      if x=='1':
        os.system('cls' if os.name == 'nt' else 'clear')
        story()
        charpicker()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice(graphics.list_of_graphics)()
        from grid import gridB,currentpos
        print(gridB[currentpos['pos']])
        break
        
      elif x=='2':
        os.system('cls' if os.name == 'nt' else 'clear')
        savepicker()
        if key == 1:
          break

      elif x=='3':
        os.system('cls' if os.name == 'nt' else 'clear')
        os._exit(0)
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        
def pausemenu():
    while True:
      graphics.logo()
      x=input("-- PAUSE MENU --\n\n1) New Game\n2) Load Game\n3) Save Game\n4) Back to Game\n5) Quit Game\n: ")
      if x=='1':
        os.system('cls' if os.name == 'nt' else 'clear')
        story()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice(graphics.list_of_graphics)()
        from grid import gridB,currentpos
        print(gridB[currentpos['pos']])
        break
        
      elif x=='2':
        os.system('cls' if os.name == 'nt' else 'clear')
        savepicker()
        if key == 1:
          break

      elif x=='5':
        os.system('cls' if os.name == 'nt' else 'clear')
        os._exit(0)
      elif x=='4':
        break
      elif x=='3':
        import variables
        variables.save()
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
      else:
        print("Invalid Choice!")
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
def startsequence():
    graphics.logo()
    input("\nPress any button except the power off button to start!\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    startmenu()
    os.system('cls' if os.name == 'nt' else 'clear')
    choice(graphics.list_of_graphics)()
    from grid import gridB,currentpos
    print("\nCurrent Position:\n")
    print(gridB[currentpos['pos']])
        

