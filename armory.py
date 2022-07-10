import graphics
import os
from random import choice
from time import sleep
def armoreq():
  import variables
  check = variables.equipped['helm'] == 'nothing' or variables.equipped['chestplate'] == 'nothing' or variables.equipped['vambraces'] == 'nothing' or variables.equipped['shield'] == 'nothing' or  variables.equipped['leggings'] == 'nothing' or variables.equipped['boots'] == 'nothing'
  if check == True:
    print(" __          __           _           _          ")
    print(" \ \        / /          | |         | |         ")
    print("  \ \  /\  / /_ _ _ __ __| |_ __ ___ | |__   ___ ")
    print("   \ \/  \/ / _` | '__/ _` | '__/ _ \| '_ \ / _ \ ")
    print("    \  /\  / (_| | | | (_| | | | (_) | |_) |  __/ ")
    print("     \/  \/ \__,_|_|  \__,_|_|  \___/|_.__/ \___|")
    print()
    print("-- Armor Station --")
    z=input("1) Equip Helm\n2) Equip Chestplate\n3) Equip Vambraces\n4) Equip Shield\n5) Equip Leggings\n6) Equip Boots\n: ")
    if z == '1':
      if variables.equipped['helm'] == 'nothing':
        count=0
        for i in variables.armory['helm']:
          print(f'{count}) {i}')
          count+=1
        try:
          x = input("Enter Helm to Equip: ")
          variables.equipped['helm'] = variables.armory['helm'][int(x)]
          print(f"You equipped {variables.equipped['helm']}")
          sleep(1)
        except IndexError as IE:
          print("Helm isn't present in your armory!")
          sleep(1)
      else:
        print("A helm is already equipped! Please De-equip it to equip another helm!")
        sleep(1)
    elif z == '2':
      if variables.equipped['chestplate'] == 'nothing':
        count=0
        for i in variables.armory['chestplate']:
          print(f'{count}) {i}')
          count+=1
        try:
          x = input("Enter Chestplate to Equip: ")
          variables.equipped['chestplate'] = variables.armory['chestplate'][int(x)]
          print(f"You equipped {variables.equipped['chestplate']}")
          sleep(1)
        except IndexError as IE:
          print("Chestplate isn't present in your armory!")
          sleep(1)
      else:
        print("A chestplate is already equipped! Please De-equip it to equip another chestplate!")
        sleep(1)
    elif z == '3':
      if variables.equipped['vambraces'] == 'nothing':
        count=0
        for i in variables.armory['vambraces']:
          print(f'{count}) {i}')
          count+=1
        try:
          x = input("Enter Vambraces to Equip: ")
          variables.equipped['vambraces'] = variables.armory['vambraces'][int(x)]
          print(f"You equipped {variables.equipped['vambraces']}")
          sleep(1)
        except IndexError as IE:
          print("Vambraces isn't present in your armory!")
          sleep(1)
      else:
        print("A set of vambraces is already equipped! Please De-equip it to equip another set of vambraces!")
        sleep(1)
    elif z == '4':
      if variables.equipped['shield'] == 'nothing':
        count=0
        for i in variables.armory['shield']:
          print(f'{count}) {i}')
          count+=1
        try:
          x = input("Enter Shield to Equip: ")
          variables.equipped['shield'] = variables.armory['shield'][int(x)]
          print(f"You equipped {variables.equipped['shield']}")
          sleep(1)
        except IndexError as IE:
          print("Shield isn't present in your armory!")
          sleep(1)
      else:
        print("A shield is already equipped! Please De-equip it to equip another shield!")
        sleep(1)
    elif z == '5':
      if variables.equipped['leggings'] == 'nothing':
        count=0
        for i in variables.armory['leggings']:
          print(f'{count}) {i}')
          count+=1
        try:
          x = input("Enter Leggings to Equip: ")
          variables.equipped['leggings'] = variables.armory['leggings'][int(x)]
          print(f"You equipped {variables.equipped['leggings']}")
          sleep(1)
        except IndexError as IE:
          print("Leggings isn't present in your armory!")
          sleep(1)
      else:
        print("A pair of leggings is already equipped! Please De-equip it to equip another pair of leggings!")
        sleep(1)
    elif z == '6':
      if variables.equipped['boots'] == 'nothing':
        count=0
        for i in variables.armory['boots']:
          print(f'{count}) {i}')
          count+=1
        try:
          x = input("Enter Boots to Equip: ")
          variables.equipped['boots'] = variables.armory['boots'][int(x)]
          print(f"You equipped {variables.equipped['boots']}")
          sleep(1)
        except IndexError as IE:
          print("Boots isn't present in your armory!")
          sleep(1)
      else:
        print("A pair of boots is already equipped! Please De-equip it to equip another pair of boots!")
        sleep(1)
    else:
      print("Invalid Choice")
      sleep(1)
  else:
    print("You are fully kitted out! Un-equip a piece of armor to equip another!")
    sleep(1)
    
def equippedarmor():
  while True:
    import variables
    graphics.clrscrn()
    print(f"Gender : {variables.gender}")
    print("-- Equipped Armor -- \n")
    print(f"                     _A_")
    print(f"                    / | \ ")
    print(f"                   |.-=-.|          Helm: {variables.equipped['helm']}")
    print(f"                   )\_|_/(")
    print(f"                .=='\   /`==.")
    print(f"              .'\   (`:')   /`.")
    print(f"            _/_ |_.-' : `-._|__\_   Chestplate: {variables.equipped['chestplate']}")
    print(f"           <___>'\    :   / `<___>") 
    print(f"           /  /   >=======<  /  /   Vambraces: {variables.equipped['vambraces']}")
    print(f"         _/ .'   /  ,-:-.  \/=,'")
    print(f"        / _/    |__/v^v^v\__) \     Shield: {variables.equipped['shield']}")
    print(f"        \(\)     |V^V^V^V^V|\_/ ")
    print(f"         (\\\     \\`---|---'/")
    print(f"           \\\     \\-._|_,-/         Leggings: {variables.equipped['leggings']}")
    print(f"            \\\     |__|__|")
    print(f"             \\\   <___X___>")
    print(f"              \\\   \..|../")
    print(f"               \\\   \ | /")
    print(f"                \\\  /V|V\           Boots: {variables.equipped['boots']}")
    print(f"                 \|/  |  \ ")
    print(f"                  '--' `--` ")
    from variables import equipped
    print("-- Armor Station --")
    x=input("1) Equip Armor\n2) De-Equip Armor\n3) Exit\n: ")
    graphics.clrscrn()
    if x=='2':
      print(" __          __           _           _          ")
      print(" \ \        / /          | |         | |         ")
      print("  \ \  /\  / /_ _ _ __ __| |_ __ ___ | |__   ___ ")
      print("   \ \/  \/ / _` | '__/ _` | '__/ _ \| '_ \ / _ \ ")
      print("    \  /\  / (_| | | | (_| | | | (_) | |_) |  __/ ")
      print("     \/  \/ \__,_|_|  \__,_|_|  \___/|_.__/ \___|")
      print()
      print("-- Armor Station --")
      y=input("1) De-Equip Helm\n2) De-Equip Chestplate\n3) De-Equip Vambraces\n4) De-Equip Shield\n5) De-Equip Leggings\n6) De-Equip Boots\n: ")
      lst = [equipped['helm'],equipped['chestplate'],equipped['vambraces'],equipped['shield'],equipped['leggings'],equipped['boots']]
      try:
        if lst[int(y)-1]!='nothing':
          if y == '1':
            print(f"You de-equipped {equipped['helm']}")
            sleep(1)
            graphics.clrscrn()
            equipped['helm'] = 'nothing'
          elif y == '2':
            print(f"You de-equipped {equipped['chestplate']}")
            sleep(1)
            graphics.clrscrn()
            equipped['chestplate'] = 'nothing'
          elif y == '3':
            print(f"You de-equipped {equipped['vambraces']}")
            sleep(1)
            graphics.clrscrn()
            equipped['vambraces'] = 'nothing'
          elif y == '4':
            print(f"You de-equipped {equipped['shield']}")
            sleep(1)
            graphics.clrscrn()
            equipped['shield'] = 'nothing'
          elif y == '5':
            print(f"You de-equipped {equipped['leggings']}")
            sleep(1)
            graphics.clrscrn()
            equipped['leggings'] = 'nothing'
          elif y == '6':
            print(f"You de-equipped {equipped['boots']}")
            sleep(1)
            graphics.clrscrn()
            equipped['boots'] = 'nothing'
          else:
            print("Invalid Option!")
            break
        else:
          print("You have nothing equipped already!")
      except ValueError as INPUT_THE_NUMBER_DAMMIT:
        print("Invalid Option!")
        sleep(1)
    elif x=='3':
        break
    elif x == '1':
        armoreq()
    else:
        print("Invalid Option!")
    
  graphics.clrscrn()

