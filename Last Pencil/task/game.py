import random


def change_turn(player1, player2):
    global player
    player = player1 if player2 == player else player2
    return player

def print_pencils(nbr_of_pencils):
    nbr_of_pencils = int(nbr_of_pencils)
    for i in range(0, nbr_of_pencils):
        print("|", end="")

def input_pencils():
    nbr_of_pencils = input()
    while not nbr_of_pencils.isdigit():
        print("The number of pencils should be numeric")
        nbr_of_pencils = input_pencils()
    while(nbr_of_pencils <= '0'):
        print("The number of pencils should be positive")
        nbr_of_pencils = input_pencils()
    return nbr_of_pencils

def input_name():
    player = input()
    while(player not in ["John","Jack"]):
        print("Choose between 'John' and 'Jack'")
        player = input_name()
    return player

def input_pencils_removed(nbr_of_pencils, player):
    list_pencils=list(range(0,200))
    valid_values = ['1', '2', '3']
    if(player == "Jack"):
        list1 = list_pencils[5:200:4]
        list2 = list_pencils[4:200:4]
        list3 = list_pencils[3:200:4]
        list4 = list_pencils[2:200:4]
        if(int(nbr_of_pencils) in list1):
            pencils_removed = random.randint(1,3)
        elif(int(nbr_of_pencils) == 1):
            pencils_removed = 1
        elif(int(nbr_of_pencils) in list2):
            pencils_removed = 3
        elif(int(nbr_of_pencils) in list3):
            pencils_removed = 2
        elif(int(nbr_of_pencils) in list4):
            pencils_removed = 1
        else:
            pencils_removed = None
        print(pencils_removed)
    else:
        pencils_removed = input()
        while(pencils_removed not in valid_values or pencils_removed.isalpha()):
            print("Possible values: '1', '2' or '3'")
            pencils_removed = input_pencils_removed(nbr_of_pencils, player)
        while(int(pencils_removed) > int(nbr_of_pencils)):
            print("Too many pencils were taken")
            pencils_removed = input_pencils_removed(nbr_of_pencils, player)
    return pencils_removed


player1 = "John"
player2 = "Jack"
print("How many pencils would you like to use:")
nbr_of_pencils = input_pencils()
print("Who will be the first (John, Jack):")
player = input_name()
print_pencils(nbr_of_pencils)
print("\n{}'s turn!".format(player))
pencils_removed = input_pencils_removed(nbr_of_pencils, player)
nbr_of_pencils = int(nbr_of_pencils)
pencils_removed = int(pencils_removed)
nbr_of_pencils = nbr_of_pencils - pencils_removed
if(nbr_of_pencils == 0):
        print("{} won!".format(change_turn(player1,player2)))
while(nbr_of_pencils != 0):
    print_pencils(nbr_of_pencils)
    new_player = change_turn(player1, player2)
    print("\n{}'s turn!".format(new_player))
    pencils_removed = input_pencils_removed(nbr_of_pencils, player)
    nbr_of_pencils = nbr_of_pencils - int(pencils_removed)
    if(nbr_of_pencils == 0):
        print("{} won!".format(change_turn(player1,player2)))