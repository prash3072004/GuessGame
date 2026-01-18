import random
while True:
    secretnumber = random.randint(0,100)
    for i in range(3):
        try:
            userinput = int (input("Guess a value from 0 to 100: "))
        except:
            print('Invalid input.Please enter an integer value: ')
            continue                                   
        if userinput==secretnumber:
            print('You won!')
            break
        else:
            if i==2:
                print('You lost.The correct guess was : {}'.format(secretnumber))
            else:
                print('Wrong guess.Try again.')
                if userinput > secretnumber:
                    print('Guess a smaller number.')
                else:
                    print('Guess a higher number.')
    print('Do you wanna play again?')
    choice = input('Y/N: ').upper()
    if choice =='Y':
        continue
    elif choice =='N':
        print('Thank you for playing. You have exited the game')
        break
    else :
        print('Invalid input.You have exited game')
        break
