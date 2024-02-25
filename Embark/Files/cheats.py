from extras import *

def cheats(uid=None, character=None):
    global debug_mode, pro_mode  
    while True:
        prints('Input a Code below')
        prints('vvvvvvvvvvvvvvvvvv')
        print()

        choice1 = inputs('Input cheat (0 to return): ')

        if choice1 == 'back':
            prints('Dumbass')
            print()
            return
        elif choice1 == 'killdembugz':
            debug_mode = True  
            prints('Debug Mode Enabled')
            print()
        elif choice1 == '42069':
            if character is not None:
                from found import Item
                bud = Item(420, 'Green Seed', 69, None, True, 1, None, None, 1, bool, bool, bool, 3, 'A seed that grows into a beautiful green bud.')
                character['Inventory'].append(bud)
            else:
                prints('Please Load a Character first.')
                print()
        elif choice1 == 'justahero':
            if character is not None:
                character['Stats']['Attack'] = 10000
                character['Stats']['Defense'] = 10000
                character['Stats']['Dodge'] = 10000
                prints("Character Saitama'd.")
                print()
            else:
                prints('Please Load a Character first.')
                print()
        elif choice1 == '2pr04U':
            pro_mode = True  
            prints('Pro Mode Enabled')
            print()
        elif choice1 == 'giggles':
            giggles = True
            prints('Giggles Enabled')
            print()
        elif choice1 == '0':
            return
        else:
            prints('Invalid Cheat.')
            print()
