import sys

######## DEFINE CLASSES ########

class Node:
    def __init__(self, desc, water, hummus, item, choiceA, choiceB):
        self.desc = desc
        self.water = water
        self.hummus = hummus
        self.item = item
        self.a = choiceA
        self.b = choiceB


class Player:
    def __init__(self, water, hummus, inventory):
        self.water = water
        self.hummus = hummus
        self.inventory = inventory


####### CREATE NODE OBJECTS #######

# final Nodes #
end = Node("", 0, 0, '', None, None)
tigerWins = Node("", 0, 0, '', None, None)
jellyfishWin = Node("", 0, 0, '', None, None)
jaffar = Node("", 0, 0, '', None, None)

# all other nodes #
redSea = Node("Ah... the deep blue water... but oh my! Two hundred Jellyfish are coming at you, bloodthirsty!\n\nTo swim back to shore, enter 'A'. To fight them off with your bare hands, enter 'B'.\n",
            -1,
            -1,
            '',
            jellyfishWin,
            jellyfishWin)

redSeaSnorkel = Node("Ah... the deep blue water... but oh my! Two hundred Jellyfish are coming at you, bloodthirsty!\n\nTo swim back to shore, enter 'A'. To fight them off with your snorkel, enter 'B'.\n",
                -1,
                -1,
                'snorkel',
                jellyfishWin,
                end)

parking = Node("You have parked your car at the shore of the Red Sea.\n\nYou notice an old snorkel lying on the floor of the car.\nTo pick it up and jump into the water, enter 'A'.To leave it in the car and just enjoy swimming naked, enter 'B'.\n",
                -1,
                -1,
                '',
                redSeaSnorkel,
                redSea)

tigerKilled = Node("You braved the tiger and managed to kill him with your shoe only!\n\nNow, to go snorkeling in the Red Sea, enter 'A'. If you had enough adventures for one day, enter 'B'.\n",
                -1,
                -1,
                '',
                parking,
                end)

redCanyon = Node("You are going down the Red Canyon.\n\nSuddenly, out of nowhere, A tiger appears 200 feet away and runs towards you!!!\nto defend yourself with your shoe, enter 'A'. to flee, enter 'B'\n",
                -1,
                -1,
                'shoes',
                tigerKilled,
                tigerWins)

route90 = Node("You are driving down Route 90 to the desert, in an old car with no a/c.\n\nIn the car there is a pair of hiking shoes. To wear them and go hike in the Red Canyon trail, enter 'A'.\nTo continue to the Red Sea, enter 'B'\n",
            -1,
            -1,
            '',
            redCanyon,
            parking)

yasser = Node("You have replenished your reserves and are ready to get on the road!\n\nIf you want to go hiking, enter 'A'. If you want to go snorkeling at the Red Sea, enter 'B'.\n",
            10,
            10,
            '',
            route90,
            parking)


oldCity = Node("You are now in old city. You see a sign: \"JAFFAR'S FAMOUS HUMMUS JOINT\".\n\nTo enter the restaurant, enter 'A'. To walk 5 minutes to Yasser's Tavern, enter 'B'\n",
            -1,
            -1,
            '',
            jaffar,
            yasser)

startGame = Node(
            "You are in downtown Jerusalem. It is hot and dry, and you are hungry and thirsty.\n\nTo go to the old city, enter A. To do some hiking and snorkeling, enter B\n", 0, 0, '',
            oldCity,
            route90)


######## DEFINE 'nextNode' & 'main' FUNCTIONS ########

def nextNode(node, p):

    # final announcments #
    if node == jellyfishWin:
        print("\n***!@$%#$%&  Too bad... The jellyfish were particularly hungry. Game over.\n")
    elif node == jaffar:
        print("\n***!@$%#$%&  Shucks! You have been ambushed by dubious people who robbed you of all your belongings!\n\n Sorry... game over.\n")
    elif node == tigerWins:
        print("\n***!@$%#$%&  The tiger, not surprisingly, was faster. He ate you and the hummus leftovers.\n\n Game over...\n")
    elif node == end:
        print("\n       ******* Well done! *******\n\nYou avoided the malice of humans, fought off preditors, braved the elements, and survived the journey!\nHave a drink at the beach.\n\n*** Goodbye!\n\n")

    # update hummus, water and inventory #
    else:
        p.water += node.water
        p.hummus += node.hummus
        if node.item != '':
            p.inventory.append(node.item)

        # check and announce current levels #
        if p.water < 1 and p.hummus < 1:
            print("\n***!@$%#$%&  You're out of water and hummus!! game over.\n")
            sys.exit()
        elif p.water < 2 or p.hummus < 2:
            print ("\n   *** WARNING: YOU ARE RUNNING OUT OF FOOD AND DRINK! ***")

        print("\n-----> You have:\n")
        print("     " + (p.water * "*") + " {} water\n\n".format(p.water) + "     " + (p.hummus * "*") + " {} hummus\n".format(p.hummus))
        if len(p.inventory) > 0:
            for item in p.inventory:
                print("     - ", item, "\n")

        # print description #
        print(node.desc)

        # user chooses next Node, call 'nextNode' function (with a new node as argument) #
        choice = ''
        while choice != 'A' and choice != 'B' and choice != 'Q':
            choice = input().upper()
            if choice == 'A':
                nextNode(node.a, p)
            elif choice == 'B':
                nextNode(node.b, p)
            elif choice == 'Q':
                print("\n        ******** Goodbye! ********\n")
                sys.exit()
            else:
                print("invalid choice. Try again")


def main():
    p = Player(2, 2, [])
    print("\n\n\n\n        ******** Welcome to the Middle East! ********")
    print("\nMake sure you don't run out of food or drink.\nyou can quit at any point by entering Q.\nnow, let's start...\n")

    # call 'nextNode' function (with 'startGame' node as argument) #
    nextNode(startGame, p)

if __name__ == '__main__':
    main()
