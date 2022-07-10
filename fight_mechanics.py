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
            graphics.print_centre("  You have gained 20 xp")
        elif index == 2:
            variables.xp['xp'] += 40
            graphics.print_centre("  You have gained 40 xp")
        elif index == 3:
            variables.xp['xp'] += 60
            graphics.print_centre("  You have gained 60 xp")
        elif index == 4:
            variables.xp['xp'] += 80
            graphics.print_centre("  You have gained 80 xp")
        elif index == 5:
            variables.xp['xp'] += 100
            graphics.print_centre("  You have gained 100 xp")     
        if variables.xp['xp'] >=variables.xp['lvlnext']:
          variables.xp['level']+=1
          variables.xp['xp']=variables.xp['xp']-variables.xp['lvlnext']
          variables.xp['lvlnext']=round(variables.xp['lvlnext']*variables.xp['modifier'])
          graphics.print_centre(f"  You have levelled up to level {variables.xp['level']}")
          if variables.xp['level'] %10 == 0:
            variables.bonus['bonushp']+=10
            graphics.print_centre(f"  You have levelled up to level {variables.xp['level']} and gained 10 bonus hp")
  
def villain():
    global enemyhp, enemyname
    global fight_switch
    loss = random.choice(variables.attackrange[index])
    variables.health['hp'] = variables.health['hp'] - loss
    return f"{enemyname} attacked you! You lost {loss} hp!"
    
def hero():
    global enemyhp, enemyname
    global fight_switch
    global run_switch
    graphics.print_centre("  ______ _       _     _   ")
    graphics.print_centre(" |  ____(_)     | |   | |  ")
    graphics.print_centre(" | |__   _  __ _| |__ | |_ ")
    graphics.print_centre(" |  __| | |/ _` | '_ \| __|")
    graphics.print_centre(" | |    | | (_| | | | | |_ ")
    graphics.print_centre(" |_|    |_|\__, |_| |_|\__|")
    graphics.print_centre("            __/ |          ")
    graphics.print_centre("           |___/           ")
    print()
    graphics.print_centre(f"Player HP = {variables.health['hp']}\t{enemyname} HP = {enemyhp}")
    print()
    try:
        graphics.print_centre("-- FIGHT --")
        graphics.print_centre("| 1)Attack 2)Defend 3)Use consumables 4)Run Away |")
        graphics.print_centre("--------------------------------------------------")
        inp = int(input(": "))
        if inp == 4:
            run_switch = 1
            graphics.print_centre("--------- LOG ---------")
            return f"You have escaped from {enemyname}"
        elif inp == 3:
            print("--- Fight Inventory --")
            if len(variables.consumables) > 0:
                for item in variables.consumables:
                    print(f'{item} : {variables.consumables[item]}')
                from consumeitem import useitemduringfight
                return useitemduringfight()
            else:
                graphics.print_centre("--------- LOG ---------")
                return "You have no consumables you can use!"
        elif inp == 2:
            parryvalues = choice(variables.armordict['helm'][variables.equipped['helm']][0])+choice(variables.armordict['chestplate'][variables.equipped['chestplate']][0])+choice(variables.armordict['leggings'][variables.equipped['leggings']][0])+choice(variables.armordict['boots'][variables.equipped['boots']][0])+choice(variables.armordict['vambraces'][variables.equipped['vambraces']][0])+choice(variables.armordict['shield'][variables.equipped['shield']][0])
            if parryvalues == 0:
              parryvalues = choice(range(1,11))
            if variables.health['hp'] + parryvalues < variables.health['hplimit']:
                variables.health['hp'] += parryvalues
                graphics.print_centre("--------- LOG ---------")
                return f"You parried and regained {parryvalues} hp"
            else:
                variables.health['hp'] = variables.health['hplimit']
                graphics.print_centre("--------- LOG ---------")
                return f"You parried and regained all of your hp"

        elif inp == 1:
            e = random.randint(10,50)
            if enemyhp - e > 0:
                enemyhp -= e
                graphics.print_centre("--------- LOG ---------")
                return f"You attacked the {enemyname}! {enemyname} lost {e} hp"
            else:
                enemyhp = 0
                graphics.print_centre("--------- LOG ---------")
                return f"You attacked the {enemyname}! {enemyname} lost all of their hp"
        fight_switch = 0
    except ValueError as ve:
        print("Invalid option! Choose again!")
        sleep(1)
        graphics.clrscrn()
        hero()

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
    graphics.clrscrn()
    graphics.print_centre(f"        __      _______     {enemyname}")     
    graphics.print_centre(f"        \ \    / / ____|    HP:{enemyhp}")
    graphics.print_centre(f"    \ \  / / (___      ")
    graphics.print_centre(f"     \ \/ / \___ \     ")
    graphics.print_centre(f"           \  /  ____) |    Player")       
    graphics.print_centre(f"            \/  |_____/     HP:{variables.health['hp']}")

    sleep(2)
    if fight_switch == 1:
      graphics.clrscrn()
    elif fight_switch == 0:
        print()
        graphics.print_centre('--------- LOG ---------')
    while enemyhp > 0 and variables.health['hp'] > 0:
        global run_switch
        if run_switch == 0:
            if fight_switch == 0:
                graphics.print_centre(f'Enemy: {villain()}')
                graphics.print_centre("-------------------")
                fight_switch = 1
                sleep(2)
                graphics.clrscrn()
            elif fight_switch == 1:
                graphics.print_centre(f'Player: {hero()}')
                fight_switch = 0
                sleep(2)
            
        else:
            sleep(2)
            graphics.clrscrn()
            from playerhud import gridprinter
            gridprinter()
            run_switch = 0
            break

        if enemyhp <= 0:
            graphics.clrscrn()
            graphics.print_centre("__     __          __          ___ ")
            graphics.print_centre("\ \   / /          \ \        / (_) ")     
            graphics.print_centre("      \ \_/ /__  _   _   \ \  /\  / / _ _ __ ")  
            graphics.print_centre("       \   / _ \| | | |   \ \/  \/ / | | '_ \ ")
            graphics.print_centre("         | | (_) | |_| |    \  /\  /  | | | | | ")
            graphics.print_centre("         |_|\___/ \__,_|     \/  \/   |_|_| |_| ")
            print()
            graphics.print_centre(f"  You have successfully defeated {enemyname}")
            graphics.print_centre("  -------------------------------------------")
            if index != 6:
              variables.stats['enemies'] += 1
              variables.money['silver'] = variables.money['silver'] + coin
              graphics.print_centre(f"  You gained {coin} Silver!")
            else:
              variables.stats['enemies'] += 1
              variables.stats['bosses'] += 1
              variables.money['silver'] = variables.money['silver'] + coin
              variables.money['gold'] = variables.money['gold'] + 10
              graphics.print_centre(f"  You gained {coin} Silver and 10 Gold!")
              
            xperience()
            graphics.print_centre("  -------------------------------------------")
            sleep(2)
            graphics.clrscrn()
            from playerhud import gridprinter
            gridprinter()
            break

        elif variables.health['hp'] <= 0:
            graphics.print_centre(f"You have been killed by {enemyname}")
            coinlose = random.choice(list(range(1,16)))
            variables.money['silver'] = variables.money['silver'] - coinlose
            
            variables.health['hp'] = variables.health['hplimit']
            graphics.print_centre("-----------------------------------------------------------------")
            graphics.print_centre(
                f"You were slain by {enemyname} ! You take cover to heal completely!"
            )
            graphics.print_centre(f"You lost {coinlose} coins!")
            graphics.print_centre("-----------------------------------------------------------------")
            sleep(2)
            graphics.clrscrn()
            from playerhud import gridprinter
            gridprinter()
            break
