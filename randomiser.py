import graphics
import random


def randomiser():
    e = ['item','encounter','thievery']
    ee = random.choices(e, weights = [2,1,1], k=1)
    if 'item' in ee:
        from events import item
        item()
    if 'encounter' in ee:
      from fight_mechanics import encounter
      encounter()
    if 'thievery' in ee:
      from events import thievery
      thievery()