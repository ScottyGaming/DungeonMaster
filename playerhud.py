import graphics
import os
from random import choice
from time import sleep

def tullius():
  from messages import tulliusdialogue
  graphics.clrscrn()
  print("  _______    _ _ _            ")
  print(" |__   __|  | | (_)           ")
  print("    | |_   _| | |_ _   _ ___  ")
  print("    | | | | | | | | | | / __| ")
  print("    | | |_| | | | | |_| \__ \ ")
  print("    |_|\__,_|_|_|_|\__,_|___/ ")
  print()
  print('Tullius: '+f'{choice(tulliusdialogue)}')
  input("Return to menu")
  graphics.clrscrn()
  
def gridprinter():
    from grid import mover, currentpos, gridA, gridB, gridC
    graphics.dungeon()
    print("\nCurrent Position:\n")
    if currentpos['grid'] == 'gridA':
        print(gridA[currentpos['pos']])
    elif currentpos['grid'] == 'gridB':
        print(gridB[currentpos['pos']])
    elif currentpos['grid'] == 'gridC':
        print(gridC[currentpos['pos']])


def stats():
    graphics.clrscrn()
    graphics.stat_ascii()
    import variables
    from variables import armordict,equipped
    graphics.print_centre(f"HP = {variables.health['hp']}")
    graphics.print_centre(f"Gold = {variables.money['gold']}")
    graphics.print_centre(f"Silver = {variables.money['silver']}")
    graphics.print_centre(f"Enemies defeated = {variables.stats['enemies']}")
    graphics.print_centre(f"XP = {variables.xp['xp']}")
    graphics.print_centre(f"Level = {variables.xp['level']}")
    graphics.print_centre(f"XP need to levelup = {variables.xp['lvlnext']}")
    graphics.print_centre(f"Max Parry: {armordict['helm'][equipped['helm']][1]+armordict['chestplate'][equipped['chestplate']][1]+armordict['leggings'][equipped['leggings']][1]+armordict['boots'][equipped['boots']][1]+armordict['vambraces'][equipped['vambraces']][1]+armordict['shield'][equipped['shield']][1]}")
    graphics.print_centre("Return to menu")
    input()
    graphics.clrscrn()
    

  
def inventory():
    graphics.clrscrn()
    print('''  _____                      _                   
 |_   _|                    | |                  
   | |  _ ____   _____ _ __ | |_ ___  _ __ _   _ 
   | | | '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
  _| |_| | | \ V /  __/ | | | || (_) | |  | |_| |
 |_____|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                            __/ |
                                           |___/ ''')
    import variables
    for item in variables.consumables:
        print(f'{item} : {variables.consumables[item]}')
    from consumeitem import useitem
    useitem()
    input("Return to menu")
    graphics.clrscrn()

def shop():
    import variables
    while True:
      graphics.clrscrn()
      
      print('''   _____ _                 
  / ____| |                
 | (___ | |__   ___  _ __  
  \___ \| '_ \ / _ \| '_ \ 
  ____) | | | | (_) | |_) |
 |_____/|_| |_|\___/| .__/ 
                    | |    
                    |_|    ''')
      print()
      x=input("1) Helm 2) ChestPlate 3) Leggings\n4) Boots 5) Vambraces 6) Shield 7) Exit\n: ")
      print()
      if x=='1':
        unbought = []
        for i in variables.armordict['helm']:
          if i in variables.armory['helm'] or i == 'nothing':
            pass
          else:
            unbought.append(i)
            print(f'{unbought.index(i)}) ' + i + f'  Cost: {variables.armordict["helm"][i][2]}')
        try:
          if len(unbought)>0:
            y=input("Enter armorpiece no to buy: ")
            if int(y) <=len(unbought):
              if variables.money['silver']>=variables.armordict['helm'][unbought[int(y)]][2]:
                variables.money['silver'] -= variables.armordict['helm'][unbought[int(y)]][2]
                variables.armory['helm'].append(unbought[int(y)])
                print(f"{unbought[int(y)]} bought!")
                sleep(1)
              else:
                print("Low Funds!")
                sleep(1)
            else:
              pass
          else:
            print("We are out of stock!")
            sleep(1)
        except (ValueError,IndexError) as DONTTYPEENTERFORGODSSAKEARGH:
          pass
      elif x=='2':
        unbought = []
        for i in variables.armordict['chestplate']:
          if i in variables.armory['chestplate'] or i == 'nothing':
            pass
          else:
            unbought.append(i)
            print(f'{unbought.index(i)}) ' + i + f'  Cost: {variables.armordict["chestplate"][i][2]}')
        try:
          if len(unbought)>0:
            y=input("Enter armorpiece no to buy: ")
            if int(y) <=len(unbought):
              if variables.money['silver']>=variables.armordict['chestplate'][unbought[int(y)]][2]:
                variables.money['silver'] -= variables.armordict['chestplate'][unbought[int(y)]][2]
                variables.armory['chestplate'].append(unbought[int(y)])
                print(f"{unbought[int(y)]} bought!")
                sleep(1)
              else:
                print("Low Funds!")
                sleep(1)
            else:
              pass
          else:
            print("We are out of stock!")
            sleep(1)
        except (ValueError,IndexError) as DONTTYPEENTERFORGODSSAKEARGH:
          pass
          
      elif x=='3':
        unbought = []
        for i in variables.armordict['leggings']:
          if i in variables.armory['leggings'] or i == 'nothing':
            pass
          else:
            unbought.append(i)
            print(f'{unbought.index(i)}) ' + i + f'  Cost: {variables.armordict["leggings"][i][2]}')
        try:    
          if len(unbought)>0:
            y=input("Enter armorpiece no to buy: ")
            if int(y) <=len(unbought):
              if variables.money['silver']>=variables.armordict['leggings'][unbought[int(y)]][2]:
                variables.money['silver'] -= variables.armordict['leggings'][unbought[int(y)]][2]
                variables.armory['leggings'].append(unbought[int(y)])
                print(f"{unbought[int(y)]} bought!")
                sleep(1)
              else:
                print("Low Funds!")
                sleep(1)
            else:
              pass
          else:
            print("We are out of stock!")
            sleep(1)
        except (ValueError,IndexError) as DONTTYPEENTERFORGODSSAKEARGH:
          pass
          
      elif x=='4':
        unbought = []
        for i in variables.armordict['boots']:
          if i in variables.armory['boots'] or i == 'nothing':
            pass
          else:
            unbought.append(i)
            print(f'{unbought.index(i)}) ' + i + f'  Cost: {variables.armordict["boots"][i][2]}')
        try:    
          if len(unbought)>0:
            y=input("Enter armorpiece no to buy: ")
            if int(y) <=len(unbought):
              if variables.money['silver']>=variables.armordict['boots'][unbought[int(y)]][2]:
                variables.money['silver'] -= variables.armordict['boots'][unbought[int(y)]][2]
                variables.armory['boots'].append(unbought[int(y)])
                print(f"{unbought[int(y)]} bought!")
                sleep(1)
              else:
                print("Low Funds!")
                sleep(1)
            else:
              pass
          else:
            print("We are out of stock!")
            sleep(1)
        except (ValueError,IndexError) as DONTTYPEENTERFORGODSSAKEARGH:
          pass
          
      elif x=='5':
        unbought = []
        for i in variables.armordict['vambraces']:
          if i in variables.armory['vambraces'] or i == 'nothing':
            pass
          else:
            unbought.append(i)
            print(f'{unbought.index(i)}) ' + i + f'  Cost: {variables.armordict["vambraces"][i][2]}')
        try:
          if len(unbought)>0:
            y=input("Enter armorpiece no to buy: ")
            if int(y) <=len(unbought):
              if variables.money['silver']>=variables.armordict['vambraces'][unbought[int(y)]][2]:
                variables.money['silver'] -= variables.armordict['vambraces'][unbought[int(y)]][2]
                variables.armory['vambraces'].append(unbought[int(y)])
                print(f"{unbought[int(y)]} bought!")
                sleep(1)
              else:
                print("Low Funds!")
                sleep(1)
            else:
              pass
          else:
            print("We are out of stock!")
            sleep(1)
        except (ValueError,IndexError) as DONTTYPEENTERFORGODSSAKEARGH:
          pass
          
      elif x=='6':
        unbought = []
        for i in variables.armordict['shield']:
          if i in variables.armory['shield'] or i == 'nothing':
            pass
          else:
            unbought.append(i)
            print(f'{unbought.index(i)}) ' + i + f'  Cost: {variables.armordict["shield"][i][2]}')
        try:
          if len(unbought)>0:
            y=input("Enter armorpiece no to buy: ")
            if int(y) <=len(unbought):
              if variables.money['silver']>=variables.armordict['shield'][unbought[int(y)]][2]:
                variables.money['silver'] -= variables.armordict['shield'][unbought[int(y)]][2]
                variables.armory['shield'].append(unbought[int(y)])
                print(f"{unbought[int(y)]} bought!")
                sleep(1)
              else:
                print("Low Funds!")
                sleep(1)
            else:
              pass
          else:
            print("We are out of stock!")
            sleep(1)
        except (ValueError,IndexError) as DONTTYPEENTERFORGODSSAKEARGH:
          pass
          
      elif x=='7':
        break

def menu():
    graphics.spacer()
    graphics.print_centre(f"--- [WASD] Move [I] Inventory [V] Stats [M] Menu [Z] Armor [T] Tullius [B] Shop ---")
    cho=input(": ")
    if cho == "W" or cho == "w":
        from grid import mover
        mover(cho)
    elif cho == "A" or cho == "a":
        from grid import mover
        mover(cho)
    elif cho == "S" or cho == "s":
        from grid import mover
        mover(cho)
    elif cho == "D" or cho == "d":
        from grid import mover
        mover(cho)
    elif cho == "I" or cho == "i":
        inventory()
        gridprinter()
    elif cho == "V" or cho == "v":
        stats()
        gridprinter()
    elif cho == 'alohomora':
        from debug import debugmenu
        debugmenu()
    elif cho == "M" or cho == "m":
        import startsequence
        graphics.clrscrn()
        startsequence.pausemenu()
        sleep(1)
        graphics.clrscrn()
        gridprinter()
    elif cho == 'Z' or cho == 'z':
        from armory import equippedarmor
        equippedarmor()
        gridprinter()
    elif cho == 'T' or cho == 't':
        tullius()
        gridprinter()
    elif cho == 'B' or cho == 'b':
        shop()
        graphics.clrscrn()
        gridprinter()
    elif cho == 'makemetherichestbch':
      import variables
      variables.money["silver"] += 10000
      variables.money["gold"]+=10000
      graphics.clrscrn()
      gridprinter()
    else:
        graphics.clrscrn()
        gridprinter()
