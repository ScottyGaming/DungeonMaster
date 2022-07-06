import os
def debugmenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''  _____  ______ ____  _    _  _____ 
 |  __ \|  ____|  _ \| |  | |/ ____|
 | |  | | |__  | |_) | |  | | |  __ 
 | |  | |  __| |  _ <| |  | | | |_ |
 | |__| | |____| |_) | |__| | |__| |
 |_____/|______|____/ \____/ \_____|
                                    
                                    ''')
        inp = input("Enter debug cmd to proceed: ")

        if inp == 'addgold':
            import variables
            add = int(input("Enter coins to add: "))
            variables.money["gold"] += add

        elif inp == 'additem':
            import variables
            add = input("Enter item name to add: ")
            variables.consumables[add]+=1
      
        elif inp == 'addsilver':
            import variables
            add = int(input("Enter coins to add: "))
            variables.money["silver"] += add

        elif inp == 'stats':
            import playerhud
            playerhud.stats()
          
        elif inp == 'triggerrandomencounter':
            from fight_mechanics import encounter
            encounter()

        elif inp == 'triggeritemfind':
            from randomiser import item
            item()
        elif inp == 'thieverytest':
            import events
            events.thievery()
        elif inp == 'undebug' or inp == 'quit' or inp == 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')
            from playerhud import gridprinter
            gridprinter()
            break
