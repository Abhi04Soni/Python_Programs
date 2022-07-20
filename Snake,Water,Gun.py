# Exercise6 Snake,Water,gun Game

import random


Choices = ["Snake", "Water", "Gun"]


# j=-1
while True :
    i = 0;
    Player_Point = 0;
    Computer_Points = 0;
    Number_of_games = 10;

    while i<Number_of_games:
        Random_choice = random.choice(Choices)
        Player_choice = str(input("Write `S` for Snake \n `W` for Water \n `G`for Gun \n "))
        i+=1;
        if (Player_choice == "s" and Random_choice == "Water"):
            print("You choose Snake and computer chooses Water \n")
            print("Player wins\n")
            Player_Point = Player_Point + 1;

        elif (Player_choice == "s" and Random_choice == "Gun"):
            print("You choose Snake and computer chooses Gun \n")
            print("Computer wins\n")
            Computer_Points = Computer_Points +1;

        elif (Player_choice == "s" and Random_choice == "Snake"):
            print("You choose Snake and computer chooses Snake \n")
            print("Match Draw\n")

        elif (Player_choice == "w" and Random_choice == "Gun"):
            print("You choose Water and computer chooses Gun \n")
            print("Player wins\n")
            Player_Point = Player_Point + 1;

        elif (Player_choice == "w" and Random_choice == "Snake"):
            print("You choose Water and computer chooses Snake \n")
            print("Computer wins\n")
            Computer_Points = Computer_Points +1;

        elif (Player_choice == "w" and Random_choice == "Water"):
            print("You choose Water and computer chooses Water \n")
            print("Match Draw\n")

        elif (Player_choice == "g" and Random_choice == "Gun"):
            print("You choose Gun and computer chooses Gun \n")
            print("Match Draw\n")
                
        elif (Player_choice == "g" and Random_choice == "Water"):
            print("You choose Gun and computer chooses Water \n")
            print("Computer wins\n")
            Computer_Points = Computer_Points +1;
        elif (Player_choice == "g" and Random_choice == "Snake"):
            print("You choose Gun and computer chooses Snake \n")
            print("Player Wins\n")
            Player_Point = Player_Point + 1;
        else:
            print("Invalid Input");
        Chances = Number_of_games - i ;
        print(f"Chances left  {Chances} out of {Number_of_games}")

    print(f"Player points = {Player_Point} and Computer Points = {Computer_Points} ")

    if Player_Point > Computer_Points :
        print("Congratulations!! You won by",( Player_Point - Computer_Points), "Points");
        break;
    else:
        print("You Lose, Better Luck Next Time");
        break;

# print("Wanna Play Again (y/n)")
# Response = input();
# if Response == "y" :
#     print("lets play again!!")
#     continue
# elif Response == "n":
#     j+=1;
# else :
#      print("Invalid");



