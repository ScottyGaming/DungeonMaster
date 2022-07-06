import random
import variables
from variables import *
import graphics
from time import sleep
import os

def xperience():
    if variables.enemyhp <= 0:
        if index == 1:
            variables.xp['xp'] += 20
            print("You have gained 20 xp")
        elif index == 2:
            variables.xp['xp'] += 40
            print("You have gained 40 xp")
        elif index == 3:
            variables.xp['xp'] += 60
            print("You have gained 60 xp")
        elif index == 4:
            variables.xp['xp'] += 80
            print("You have gained 80 xp")
        elif index == 5:
            variables.xp['xp'] += 100
            print("You have gained 100 xp")     
        if variables.xp['xp'] >=variables.xp['lvlnext']:
          variables.xp['level']+=1
          variables.xp['xp']=variables.xp['xp']-variables.xp['lvlnext']
          variables.xp['lvlnext']=round(variables.xp['lvlnext']*variables.xp['modifier'])
          print(f"You have levelled up to level {variables.xp['level']}")
          if variables.xp['level'] %10 == 0:
            variables.bonus['bonushp']+=10
            print(f"You have levelled up to level {variables.xp['level']} and gained 10 bonus hp")
  
def villain():
    global enemyhp, enemyname
    global fight_switch
    if index == 1:
      loss = random.choice(variables.attackrange[1])
    elif index == 2:
      loss = random.choice(variables.attackrange[2])
    elif index == 3:
      loss = random.choice(variables.attackrange[3])
    elif index == 4:
      loss = random.choice(variables.attackrange[4])
    elif index == 5:
      loss = random.choice(variables.attackrange[5])
      
    variables.health['hp'] = variables.health['hp'] - loss
    print(f"\n--- ENEMY LOG ---\n{enemyname} attacked you! You lost {loss} hp!\n--- --- -- --- --- --- --- ---")
    fight_switch = 1


def hero():
    global enemyhp, enemyname
    global fight_switch
    global run_switch
    print("  ______ _       _     _   ")
    print(" |  ____(_)     | |   | |  ")
    print(" | |__   _  __ _| |__ | |_ ")
    print(" |  __| | |/ _` | '_ \| __|")
    print(" | |    | | (_| | | | | |_ ")
    print(" |_|    |_|\__, |_| |_|\__|")
    print("            __/ |          ")
    print("           |___/           ")

    print(f"\nPlayer HP = {variables.health['hp']}\t\t\t{enemyname} HP = {enemyhp}\n")
    try:
        inp = int(
            input(
                "-- FIGHT --\n1)Attack 2)Defend 3)Use consumables 4)Run Away\n: "
            ))
        if inp == 4:
            run_switch = 1

        elif inp == 3:
            if len(variables.consumables) > 0:
                for item in variables.consumables:
                    print(f'{item} : {variables.consumables[item]}')
                from consumeitem import useitemduringfight
                useitemduringfight()
            else:
                print("\n--- PLAYER LOG ---\nYou have no consumables you can use!\n--- --- -- --- --- --- --- ---")
                graphics.spacer()

        elif inp == 2:
            parryvalues = choice(variables.armordict['helm'][variables.equipped['helm']][0])            +choice(variables.armordict['chestplate'][variables.equipped['chestplate']][0])+choice(variables.armordict['leggings'][variables.equipped['leggings']][0])+choice(variables.armordict['boots'][variables.equipped['boots']][0])+choice(variables.armordict['vambraces'][variables.equipped['vambraces']][0])+choice(variables.armordict['shield'][variables.equipped['shield']][0])
            if parryvalues == 0:
              parryvalues = choice(range(1,11))
            if variables.health['hp'] + parryvalues < variables.health['hplimit']:
                variables.health['hp'] += parryvalues
                print(f"\n--- PLAYER LOG ---\nYou parried and regained {parryvalues} hp\n--- --- -- --- --- --- --- ---")
                graphics.spacer()
            else:
                variables.health['hp'] = variables.health['hplimit']
                print(f"\n--- PLAYER LOG ---\nYou parried and regained all of your hp\n--- --- -- --- --- --- --- ---")
                graphics.spacer()

        elif inp == 1:
            e = random.randint(10,50)
            if enemyhp - e > 0:
                enemyhp -= e
                print(
                    f"\n--- PLAYER LOG ---\nYou attacked the {enemyname}! {enemyname} lost {e} hp\n--- --- -- --- --- --- --- ---")
                graphics.spacer()
            else:
                enemyhp = 0
                print(
                    f"\n--- PLAYER LOG ---\nYou attacked the {enemyname}! {enemyname} lost all of their hp\n--- --- -- --- --- --- --- ---"
                )
                graphics.spacer()
        fight_switch = 0
    except ValueError as ve:
        print("Invalid option! Choose again!")


def encounter():
    global enemyhp, enemyname
    global fight_switch
    global run_switch
    global index

    if variables.xp['level'] >= 0 and variables.xp['level'] < 10:
        index = 1
    elif variables.xp['level'] >= 10 and variables.xp['level'] < 30:
        index = random.choice([1,2])
    elif variables.xp['level'] >= 30 and variables.xp['level'] < 50:
        index = random.choice([1,2,3])
    else:
        index = random.choice([1,2,3,4,5])
      
    if variables.stats["enemies"] !=0 and variables.stats['enemies'] % 30 == 0:
      index = 6
      
    enemyname = random.choice(variables.enemies[index])
    enemyhp = variables.loot[index][0]
    coin = variables.loot[index][2]
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{enemyname}\nHP:{enemyhp}")
    print("        __      _______ ")     
    print("        \ \    / / ____|")
    print("         \ \  / / (___  ")
    print("          \ \/ / \___ \ ")
    print("           \  /  ____) |")       
    print("            \/  |_____/ ")
    print("                          Player")
    print(f"                          HP:{variables.health['hp']}")
    sleep(2)
    if fight_switch == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
    

    while enemyhp > 0 and variables.health['hp'] > 0:
        global run_switch
        if run_switch == 0:
            if fight_switch == 0:
                villain()
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif fight_switch == 1:
                hero()
                sleep(2)
        else:
            print(f"You have escaped from {enemyname}")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            from playerhud import gridprinter
            gridprinter()
            run_switch = 0
            break

        if enemyhp <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(''' __     __          __          ___       
 \ \   / /          \ \        / (_)      
  \ \_/ /__  _   _   \ \  /\  / / _ _ __  
   \   / _ \| | | |   \ \/  \/ / | | '_ \ 
    | | (_) | |_| |    \  /\  /  | | | | |
    |_|\___/ \__,_|     \/  \/   |_|_| |_|
                                          
                                          ''')
            print(f"You have successfully defeated {enemyname}")
            print("-------------------------------------------")
            if index != 6:
              variables.stats['enemies'] += 1
              variables.money['silver'] = variables.money['silver'] + coin
              print(f"You gained {coin} Silver!")
            else:
              variables.stats['enemies'] += 1
              variables.stats['bosses'] += 1
              variables.money['silver'] = variables.money['silver'] + coin
              variables.money['gold'] = variables.money['gold'] + 10
              print(f"You gained {coin} Silver and 10 Gold!")
              
            xperience()
            print("-------------------------------------------")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            from playerhud import gridprinter
            gridprinter()
            break

        elif variables.health['hp'] <= 0:
            print(f"You have been killed by {enemyname}")
            coinlose = random.choice(list(range(1,16)))
            variables.money['silver'] = variables.money['silver'] - coinlose
            
            variables.health['hp'] = variables.health['hplimit']
            print("-----------------------------------------------------------------")
            print(
                f"You were slain by {enemyname} ! You take cover to heal completely!"
            )
            print(f"You lost {coinlose} coins!")
            print("-----------------------------------------------------------------")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            from playerhud import gridprinter
            gridprinter()
            break
