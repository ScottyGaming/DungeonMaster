from messages import deadmsg,debtcollector
import graphics
from time import sleep

def item():
        import random
        from messages import randomitemfind, noitemfind
        import variables
        picked = random.choice(list(variables.consumabledict))
        if picked != 'nothing':
            print(f"\n-- You found a {picked} {random.choice(randomitemfind)} --")
            variables.consumables[picked] += 1
        else:
            print(noitemfind)
            graphics.spacer()
          

def thievery():
  from random import choice
  import variables
  from variables import money,enemyhp
  from fight_mechanics import encounter
  print("\n-- You have come across some thieves! Fight to save your possessions! --")
  sleep(1)
  encounter()
  if enemyhp <= 0:
    print("\n-- You escaped from the thieves and saved all your possessions! --")
    sleep(1)
  if variables.health['hp'] <= 0:
    print("\n-- The thieves looted some of your coins and ran away! --")
    sleep(1)
    money['silver']-=choice(list(range(1,20)))
    money['gold']-=choice(list(range(1,10)))


