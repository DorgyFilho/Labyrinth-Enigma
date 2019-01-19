#Text-Game

from time import sleep
from random import randint

def intro():

    print()

    print('''A traveler is walking down the road to find his hometown. For this, he needs to cross the labyrinth that separates 
him from his goal. Soon, upon arriving, he finds two people near two entrances.''')

    sleep(3)

    print()
    
    print('''Laby: Hello, traveler. I am Laby, an emissary from the Labyrinth who helps travelers to get out. 
Trust me and you will reach your destination.''')

    sleep(3)

    print()

    print('''Rinth: He is wrong, traveler. I am Rinth, the emissary of the Labyrinth. Follow me along this path that you will reach your destination.''')

    sleep(3)

    print()

    print('''Laby: Come with me you'll be happy''')

    sleep(3)

    print()

    print('''Rinth: It is with me that you will be safe.''')

    sleep(3)

    print()

    print('''Faced with this dilemma, what are you going to do? A-Continue or B-Quit''') 

    print()

def play():
    answer = input('Answer: ').upper()
    if answer == 'A':
        sleep(3)
        print('Traveler: I want to ask a question. Can be?')
        sleep(3)
        print()
        print('Laby and Rinth: Yes!')
        sleep(3)
        print()
        print('Traveler: What door will lead me to the exit?')
        sleep(3)
        print()
        print("Laby: The Rinth's door!")
        sleep(3)
        print()
        print('Rinth: My door will lead to the exit')
        sleep(3)
        print()
        print('''Traveler: I have two coins. Each one has a drawing corresponding to Laby and Rinth. I'm going to throw one of the 
    coins and the coin in my closed hand is my choice.''')
        print()
        sleep(3)
        if randint(0,1) == 0:
            print('Traveler: The answer is... Laby')
            sleep(3)
            print()
            print('Laby: The right answer is Rinth. You Lose!!!')
            sleep(3)
            print()
            print('Traveler: As I imagined, there is no right answer. If I chose Laby, the answer would be Rinth. If I chose Rinth, the answer would be Laby')
            sleep(3)
            print()
            print('Laby: That does not matter. You chose the option and lost.')
            sleep(3)
            print()
            print('Traveler: Not even. Remember that I said that the answer chosen would be the one in my closed hand?')
            sleep(3)
            print()
            print('Laby and Rinth: What?!')
            sleep(3)
            print()
            print('Traveler: My answer is Rinth!')
            sleep(3)
            print()
            print('Traveler: You wanted to deceive me, but I deceived you. Did you notice? One of my hands did not tell the truth.')
        else:
            print('The answer is... Rinth')
            sleep(3)
            print()
            print('Rinth: The right answer is Laby. You Lose!!!')
            sleep(3)
            print()
            print('Traveler: As I imagined, there is no right answer. If I chose Laby, the answer would be Rinth. If I chose Rinth, the answer would be Laby')
            sleep(3)
            print()
            print('Rinth: That does not matter. You chose the option and lost.')
            sleep(3)
            print()
            print('Traveler: Not even. Remember that I said that the answer chosen would be the one in my closed hand?')
            sleep(3)
            print()
            print('Laby and Rinth: What?!')
            sleep(3)
            print()
            print('Traveler: My answer is Rinth!')
            sleep(3)
            print()
            print('Traveler: You wanted to deceive me, but I deceived you. Did you notice? One of my hands did not tell the truth.')
    else:
        print('Come back next time.')

def main():
    again = 'Y'
    while again == 'Y':
        print('Welcome to the Labyrinth Enigma. What is Your Option? [S]tart or [Q]uit')
        print()
        opt = input('Option: ').upper()
        if opt == 'S':
            intro()
            play()
        else:
            print('Exit!')
            exit()
        print()
        print('Do you want to play again? Y or N')
        again = input('Answer: ').upper()
        if again == 'Y':
            continue
        elif again == 'N':
            print('Goodbye!')
            break
    else:
        print('Invalid Option!')

main()







