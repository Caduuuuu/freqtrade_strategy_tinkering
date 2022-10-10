import random

intro = "abv"
while intro != "Y":
    intro = input("Welcome to my little test game! you will have 10 tries to guess what number I am thinking. Type Y and press enter to continue:    ")

loopcount = 0
while loopcount < 9:
    answer = input("what number between 1 and 10 am I guessing right now?   ")
    x = random.randint(0,10)
    #print('-----------------------------------')
    if answer == x:
        print('Well done, the number is corect!')
    else: 
        offset = int(answer) - x
        print("The number your guessed is off by: ", offset) 
    print('-----------------------------------')
    loopcount += 1

quit()