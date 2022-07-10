import graphics

def useitem():
  try:
    from variables import consumabledict,consumables,health
    from random import choice
    inp = input("Enter name of item you want to use: ")
    if consumables[inp] > 0:
      if inp in consumabledict and inp!= 'poison':
        if health['hp']!=health['hplimit']:
                if health['hp']+consumabledict[inp] <= health['hplimit']:
                  health['hp']+=consumabledict[inp]
                  consumables[inp]-=1
                  return f"You have regained {consumabledict[inp]} HP!"

                else:
                  health['hp']=health['hplimit']
                  consumables[inp]-=1
                  return "You have been healed completely"
        else:
            return "Your HP is already full!"
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
  except KeyError:
    print("This item doesnt exist!")
    
def useitemduringfight():
  global enemyhp,enemyname,fight_switch
  try:
    from variables import consumabledict,consumables,health,enemyname,enemyhp,fight_switch
    from random import choice
    inp = input("Enter name of item you want to use: ")
    if consumables[inp] > 0:
      if inp in consumabledict and inp!= 'poison':
        if health['hp']!=health['hplimit']:
                if health['hp']+consumabledict[inp] <= health['hplimit']:
                  health['hp']+=consumabledict[inp]
                  consumables[inp]-=1
                  return f"You have regained {consumabledict[inp]} HP!"

                else:
                  health['hp']=health['hplimit']
                  consumables[inp]-=1
                  return "You have been healed completely"
        else:
            return "Your HP is already full!"
      elif inp == "poison":
                if enemyhp > 0:
                  enemyhp-=consumabledict['poison']
                  consumables['poison']-=1
                  return f"{enemyname} lost {consumabledict['poison']} HP!"

                else:
                  enemyhp = choice[5,10,15,20,25]
                  consumables['poison']-=1
                  return f"The poison races through {enemyname}'s veins leaving them with {enemyhp} HP!"
      else:
          print("You didnt enter a valid option! Try Again!")
    else:
      return "You don't have item(s)!"
  except KeyError:
    print("This item doesnt exist!")
  fight_switch = 0