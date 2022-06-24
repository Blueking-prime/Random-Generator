from random import choice

def func2run():
    print ('Please select a function')
    f = input('-')
    if f == 'coin flip':
        coin_flip()     
    elif f == 'standard dice roll':
        dice_roll()
    elif f == 'dice roll':
        dice_roll()
    else:
        print ('I can\'t do that yet')

def dice_roll():
    n = int(input('Roll how many times? '))
    while True:
        t = 0
        result = []
        while t < n:
            roll = choice(range(1, 7))
            result.append(roll)
            t += 1
        print (result)
        print ()
        replay = input('Do you want to repeat the roll(s), Y/N? ')
        if replay == 'Y' or replay == 'y':
            continue
        elif replay == 'N' or replay == 'n':
            break
    func2run()
def coin_flip():
    n = int(input('Flip how many times? '))
    while True:
        t = 0
        result = []
        while t < n:
            flip = choice(['H', 'T'])
            result.append(flip)
            t += 1
        print (result)
        print ()
        replay = input('Do you want to repeat the flip(s), Y/N? ')
        if replay == 'Y' or replay == 'y':
            continue
        elif replay == 'N' or replay == 'n':
            break
    func2run()
def create_set():
    a = int(input('What do you want your range to be: '))
    b = int(input('to: '))
    print ()
    c = int(input('''Any spacing? 
    (If none, input '1')
    '''))
    while True:
        n = int(input('How many tries? '))
        while True:
            t = 0
            result = []
            while t < n:
                Try = choice(range(a, b))
                result.append(Try)
                t += 1  
            print ()
            replay = input('Do you want to repeat the try/tries, Y/N? ')
            if replay == 'Y' or replay == 'y':
                continue
            elif replay == 'N' or replay == 'n':
                break      
        print()
        replay = input('Do you want to change your values, Y/N? ')
        if replay == 'Y' or replay == 'y':
            break
        elif replay == 'N' or replay == 'n':
            continue
    func2run()

func = ['-Standard dice roll', '-Coin flip', '-more coming soon']
print ('''Welcome!
Today we have a probabilty program that can be used for things like rolling dice, flipping a coin, etc
You can currently select from a list of:''')
for item in func:
    print (item)
func2run()