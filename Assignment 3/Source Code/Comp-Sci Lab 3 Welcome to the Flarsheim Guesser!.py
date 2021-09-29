print('Welcome to the Flarsheim Guesser!')
print()
print('Please think of a number between and including 1 and 100 ')
print()
play = True
while play:
    print('What is the remainder when your number is divided by 3 ?')
    remainder_input = int(input())
    if remainder_input < 0:
        print('The value entered must be 0 or greater')
        continue
    elif remainder_input >= 3:
        print('The value entered must be less than 3')
        continue
    else:
        remainder_input = remainder_input
    print()
    print('What is the remainder when your number is divided by 5 ?')
    remainder_input2 = int(input())
    if remainder_input2 < 0:
        print('The value entered must be 0 or greater')
    print()
    if remainder_input >= 0:
        print('What is the remainder when your number is divided by 7 ?')
        remainder_input3 = int(input())
    elif remainder_input < 0:
        print('The value entered must be 0 or greater')
    print()
    for i in range(1,101):
        if i %3 == remainder_input and i %5 == remainder_input2 and i%7 == remainder_input3:
            print('Your number was', i)
            print('How amazing is that?')
            user_input = input('Do you want to play again? Y to continue, N to quit  ==> ')
            while user_input.upper() != ('Y') and user_input.upper() != ('N'):
                user_input = input('Do you want to play again? Y to continue, N to quit  ==> ')
            if user_input.upper() == ('Y'):
                print('Please think of a number between and including 1 and 100 ')
                play = True
            elif user_input.upper() == ('N'):
                exit()


                

                

                
