import random

secretNum = random.randint(1,20)
print('I am thinking a number between 1 and 20...')
#print(secretNum)

for myGuessTimes in range(1, 6):
    print('Please input your guess: ')
    myGuessNum = int(input())

    if(myGuessNum > secretNum):
        print('Your guess is too high')
    elif(myGuessNum < secretNum):
        print('Your guess is too low')
    else:
        print('You get it')
        break
            
print('Secret Number is: ' + str(secretNum))