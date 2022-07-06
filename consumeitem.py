import graphics

def useitem():
  try:
    from variables import consumabledict,consumables,health,bonus,enemyname,enemyhp
    from random import choice
    inp = input("Enter name of item you want to use: ")
    if consumables[inp] > 0:
        if inp == 'potion':
          if health['hp']!=health['hplimit']:
                if health['hp']+consumabledict['potion'] <= health['hplimit']:
                  health['hp']+=consumabledict['potion']
                  print(f"You have regained {consumabledict['potion']} HP!")
                  graphics.spacer()
                else:
                  health['hp']=health['hplimit']
                  print("You have been healed completely")
                  graphics.spacer()
                consumables['potion']-=1
          else:
            print("Your HP is already full!")
        elif inp == "berry":
          if health['hp']!=health['hplimit']:
                if health['hp']+consumabledict['berry'] <= health['hplimit']:
                  health['hp']+=consumabledict['berry']
                  print(f"You have regained {consumabledict['berry']} HP!")
                  graphics.spacer()
                else:
                  health['hp']=health['hplimit']
                  print("You have been healed completely")
                  graphics.spacer()
                consumables['berry']-=1
          else:
            print("Your HP is already full!")
        elif inp == "water":
          if health['hp']!=health['hplimit']:
                if health['hp']+consumabledict['water'] <= health['hplimit']:
                  health['hp']+=consumabledict['water']
                  print(f"You have regained {consumabledict['water']} HP!")
                  graphics.spacer()
                else:
                  health['hp']=health['hplimit']
                  print("You have been healed completely")
                  graphics.spacer()
                consumables['water']-=1
          else:
            print("Your HP is already full!")
        elif inp == "poison":
                if health['hp']-consumabledict['poison'] >= health['hplimit']:
                  health['hp']-=consumabledict['poison']
                  print(f"You have lost {consumabledict['poison']} HP!")
                  graphics.spacer()
                else:
                  health['hp']=choice([5,10,15,20,25])
                  print(f"The poison races through your veins leaving you with {health['hp']} HP!")
                  graphics.spacer()
                consumables['poison']-=1
        else:
          print("You didnt enter a valid option! Try Again!")
    else:
        print("Your inventory is empty!")
  except KeyError as whythefwouldyoutypethat:
    print("This item doesnt exist!")
    
def useitemduringfight():
  global enemyhp,enemyname,fight_switch
  try:
    from variables import consumabledict,consumables,health,bonus,enemyname,enemyhp,fight_switch,run_switch
    from random import choice
    inp = input("Enter name of item you want to use: ")
    if consumables[inp] > 0:
      if inp == 'potion':
        if health['hp']!=health['hplimit']:
              if health['hp']+consumabledict['potion'] <= health['hplimit']:
                health['hp']+=consumabledict['potion']
                print(f"You have regained {consumabledict['potion']} HP!")
                graphics.spacer()
              else:
                health['hp']=health['hplimit']
                print("You have been healed completely")
                graphics.spacer()
              consumables['potion']-=1
        else:
          print("Your HP is already full!")
      elif inp == "berry":
        if health['hp']!=health['hplimit']:
              if health['hp']+consumabledict['berry'] <= health['hplimit']:
                health['hp']+=consumabledict['berry']
                print(f"You have regained {consumabledict['berry']} HP!")
                graphics.spacer()
              else:
                health['hp']=health['hplimit']
                print("You have been healed completely")
                graphics.spacer()
              consumables['berry']-=1
        else:
          print("Your HP is already full!")
      elif inp == "water":
        if health['hp']!=health['hplimit']:
              if health['hp']+consumabledict['water'] <= health['hplimit']:
                health['hp']+=consumabledict['water']
                print(f"You have regained {consumabledict['water']} HP!")
                graphics.spacer()
              else:
                health['hp']=health['hplimit']
                print("You have been healed completely")
                graphics.spacer()
              consumables['water']-=1
        else:
          print("Your HP is already full!")
      elif inp == "poison":
              if enemyhp > 0:
                enemyhp-=consumabledict['poison']
                print(f"{enemyname} lost {consumabledict['poison']} HP!")
                graphics.spacer()
              else:
                enemyhp = choice[5,10,15,20,25]
                print(f"The poison races through {enemyname}'s veins leaving them with {enemyhp} HP!")
                graphics.spacer()
              consumables['poison']-=1
      else:
        print("You didnt enter a valid option! Try Again!")
    else:
      print("You don't have item(s)!")
  except KeyError as whythefwouldyoutypethat:
    print("This item doesnt exist!")
  fight_switch = 0