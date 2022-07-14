import random
import json
from os.path import exists
from random import choice
consumabledict = {'potion':50,'berry':20,'water':10,'poison':30,'nothing':'nothing'}

armordict = {
  
          'helm':{'nothing':[list(range(1,2)),1,0], 'Boar Hide Headguard':[list(range(1,6)),5], 'Orcskin HeadDress':[list(range(1,6)),5,100], 'Beskar Visor':[list(range(5,11)),10,250], 'Shaman HeadDress':[list(range(5,11)),10,250] },
  
          'chestplate':{'nothing':[list(range(1,2)),1,0], 'Boar Hide Chestplate':[list(range(1,6)),5], 'Orcskin Corset':[list(range(1,6)),5,100], 'Beskar Cuirass':[list(range(5,11)),10,250], 'Shaman Bandeau':[list(range(5,11)),10,250] },
  
          'leggings':{'nothing':[list(range(1,2)),1,0], 'Boar Hide Leggings':[list(range(1,6)),5], 'Orcskin Leggings':[list(range(1,6)),5,100], 'Beskar Legguards':[list(range(5,11)),10,250], 'Shaman Robe':[list(range(5,11)),10,250] },
  
          'boots':{'nothing':[list(range(1,2)),1,0], 'Boar Hide Boots':[list(range(1,6)),5], 'Orcskin Slippers':[list(range(1,6)),5,100], 'Beskar Treads':[list(range(5,11)),10,250], 'Shaman Treads':[list(range(5,11)),10,250] },
  
          'vambraces':{'nothing':[list(range(1,2)),1,0], 'Boar Hide Vambraces':[list(range(1,6)),5], 'Orcskin Trinkets':[list(range(1,6)),5,100], 'Beskar Vambraces':[list(range(5,11)),10,250], 'Shaman Markings':[list(range(5,11)),10,250] },
  
          'shield':{'nothing':[list(range(1,2)),1,0], 'Boar Hide Shield':[list(range(1,6)),5], 'Orcskin Shield':[list(range(1,6)),5,100], 'Beskar Aegis':[list(range(5,11)),10,250], 'Shaman Aura':[list(range(5,11)),10,250] },
}


consumables = {'potion':1,'berry':3,'water':0,'poison':0}

armory = {'helm':['Boar Hide Headguard'],
          'chestplate':['Boar Hide Chestplate'],
          'leggings':['Boar Hide Leggings'],
          'boots':['Boar Hide Boots'],
          'vambraces':['Boar Hide Vambraces'],
          'shield':['Boar Hide Shield']}

equipped = {'helm':'nothing','chestplate':'nothing','leggings':'nothing','boots':'nothing','shield':'nothing','vambraces':'nothing'}

#health
bonus = {'bonushp':0}
health = {'hp':100,'hplimit':100+bonus['bonushp']}

#inventory
genlist = ['Male','Female']
gender = None
money = {'gold':0,'silver':0}


xp = {'xp':0.,'level':0.,'modifier':2.5,'lvlnext':25}
#info
stats = {'enemies':0,'bosses':0}

Enemies = {0:0,('Slime','Goblin','Imp','Cougar'):[50,10,10]
,('Rogue','Bat','Smurf','Zombie'):[80,20,20]
,('Skeleton','Golem','Troll','Kobold'):[100,20,30]
,('Giant','Great Unclean','Tyranid','Orc','Necron'):[200,50,40]
,('Fallen Palladin','Druid','Doraemon'):[300,100,50]
,('The Reaper Of Souls', 'Bootleg Galactus', 'The Scarlet Witch'):[600,200,100],('The World Destroyer G'):[1000,400,300]}
enemies = list(Enemies.keys())
loot = list(Enemies.values())

attackrange = {1:[2,4,6,8,10,12,14,16,18,20],2:[10,12,14,16,18,20,22,24],3:[20,22,24,26,28,30,32,34,36],4:[30,32,34,36,38,40,42,44,46,48],5:[40,42,44,46,48,50,52,54,56,58,60],6:[50,52,52,54,56,58,60,62,64,66],7:[50,60,70,80,90,100,110,120,130,140,150]}

enemyhp = 0
fight_switch = random.choice([0, 1])
run_switch = 0
enemyname = 'none'


def save():
  filename = input("Enter name of save: ")
  filename = filename+'.dat'
  import grid
  
  data = {'money':money,'consumables':consumables,'xp':xp,'stats':stats,'currentpos':grid.currentpos,
'armory':armory,'equipped':equipped,'gender':gender}
  if exists(filename):
    y=input("Save Already Exists! Overwrite?\n1)Yes\n2)No\n:  ")
    if y==1:
      with open(filename,'w') as file_object:
        json.dump(data,file_object)
        print("Save succeeded")
    elif y==2:
      print("Cancelling save process!")
  else:
    with open(filename,'w') as file_object:
        json.dump(data,file_object)
        print("Save succeeded")

  
def load(filename):
  with open(filename,'r') as file_object:
    try:
      import grid
      global money,consumables,xp,stats
      data = json.load(file_object)
      money = data['money']
      consumables = data['consumables']
      xp = data['xp']
      stats = data['stats']
      grid.currentpos = data['currentpos']
      armory = data['armory']
      equipped = data['equipped']
      gender = data['gender']
    except KeyError as oldsave:
      print("Old save file detected! Newer Variables will not load!")
      
