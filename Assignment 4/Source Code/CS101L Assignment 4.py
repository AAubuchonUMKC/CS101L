import random
def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    user_input = input('Do you want to play again?')
    while user_input.upper() != ('Y') and user_input.upper() != ('N'):
        print('You must enter Y/YES/N/NO to continue.  Please try again')
        user_input = input('Do you want to play again?')
        if user_input.upper() == ('Y'):
            print('Please think of a number between and including 1 and 100 ')
            return True
        elif user_input.upper() == ('N'):
            exit()
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How many chips do you want to wager? ==> '))
    if wager > 0 and wager <= bank:
        return 1 
    while wager < 0:
        print('The wager amount must be greater than 0. Please enter again. ')
        wager = int(input('How many chips do you want to wager? ==> '))
        continue
    while wager > bank:
        print('The wager amount cannot be greater than how much you have. {}'.format(bank))
        wager = int(input('How many chips do you want to wager? ==> '))
        continue

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reela = random.randrange(1,11)
    reelb = random.randrange(1,11)
    reelc = random.randrange(1,11)

    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    while reela == reelb and reela == reelc:
        matches = 3
        return matches
    while reela == reelb or reela == reelc:
        matches = 2
        return matches
    while reelb == reelc:
        return 2
    else:
        matches = 0
        return matches

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input('How many chips do you want to start with? '))
    if bank > 0 and bank <= 100:
        return bank
    while bank < 0:
        print('Too low a value, you can only choose 1 -100 chips')
        bank = int(input('How many chips do you want to start with? '))
        continue
    while bank > 100:
        print('Too high a value, you can only choose 1 -100 chips')
        bank = int(input('How many chips do you want to start with? '))
        continue

    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10 - wager

    elif matches == 2:
        return wager * 3 - wager

    return -wager


if __name__ == "__main__":

    playing = True
    while playing:

        bank = max_chips = init_chips = get_bank()
        rounds = 0
        while bank > 0:



            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            max_chips = max(bank,max_chips)
            rounds += 1
           
        print("You lost all", init_chips, "in", rounds, "spins")
        print("The most chips you had was", max_chips)
        playing = play_again()