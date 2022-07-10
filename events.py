from messages import deadmsg,debtcollector
import graphics
from time import sleep

def item():
        import random
        from messages import randomitemfind, noitemfind
        import variables
        picked = random.choice(list(variables.consumabledict))
        if picked != 'nothing':
            graphics.print_centre(f"-- You found a {picked} {random.choice(randomitemfind)} --")
            variables.consumables[picked] += 1
        else:
            graphics.print_centre(noitemfind)
            graphics.spacer()
          

def thievery():
  from random import choice
  import variables
  from variables import money,enemyhp
  from fight_mechanics import encounter
  graphics.print_centre("-- You have come across some thieves! Fight to save your possessions! --")
  sleep(1)
  encounter()
  if enemyhp <= 0:
    graphics.print_centre("-- You escaped from the thieves and saved all your possessions! --")
    sleep(1)
  if variables.health['hp'] <= 0:
    graphics.print_centre("-- The thieves looted some of your coins and ran away! --")
    sleep(1)
    money['silver']-=choice(list(range(1,20)))
    money['gold']-=choice(list(range(1,10)))


