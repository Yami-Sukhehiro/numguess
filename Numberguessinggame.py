import random
ur_life= random.randint(1,9)
chances=0
while chances<5:
    guess= int(input("Enter your number"))
    if guess== ur_life:
        print("you are a loser dude who plays this trash game even?")
        break
    elif guess<ur_life:
        print("you dumb B")
    else:
        print("think of your IQ level")
    chances+=1
if not chances< 5:
    print("bruh how dumb are you?!")           