# make snake ,water ,gun game using random.choice function,using for/while loop- max try 10 times,print how many times you
#     win and how many times computer wins

#snake,water ,gun game
import random
list=['s','w','g']
chance=10
no_of_chance=0
computer_point=0
yours_point=0
print("\t \t \t \t Snake,Water,Gun Game \n \n")
print(("S for snake \nW for water \nG for gun"))
#making the game in while
while no_of_chance<chance:
    _input=input("SNAKE,WATER,GUN:")#that we write from option of list
    _random=random.choice(list)

    if _input==_random:
        print(" tie both  0 point to each\n")
    #if user enter s
    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(f"your guess {_input} and computer choice {_random}\n")
        print("computer wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {yours_point}\n ")

    elif _input=="s" and _random=="w":
        yours_point=yours_point+1
        print(f"your guess {_input} and computer choice {_random}\n")
        print("you wins 1 point \n")
        print(f"comuter point is {computer_point} and yours point is{yours_point}\n")

    #if user enter g
    elif _input=="g" and _random=="s":
        yours_point=yours_point+1
        print(f"your guess {_input} and computer choice is {_random}\n")
        print("you wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {yours_point}\n")

    elif _input=="g" and _random=="w":
        computer_point=computer_point+1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point \n")
        print(f"computer point {computer_point} and your point {yours_point}\n")

    #if user enter w
    elif _input=="w" and _random=="g":
        yours_point=yours_point+1
        print(f"your guess {_input} and computer choice {_random}\n")
        print(("you wins 1 point \n"))
        print(f"computer point {computer_point} and your point {yours_point}\n")

    elif _input=="w" and _random=="s":
        computer_point=computer_point+1
        print(f"your guess {_input} and computer choice {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer point s{computer_point} and your point {yours_point}\n")

    else:
        print("you have enter wrong input\n")

    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")

print("GAME OVER")

if computer_point==yours_point:
    print("tie game")

elif computer_point>yours_point:
    print("computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {yours_point} and computer point is {computer_point}")

#the snake drinks the water, the gun shoots the snake  and gun has no effect on water
