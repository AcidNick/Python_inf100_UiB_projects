import random

# "Sixer yatzy" is a game played with five dice, where the winner is the
# first person to roll only sixes. In each turn, the player may re-roll
# dice that are *not* six up to two times; in other words, in a single
# turn each dice may be rolled once (if it was six right away), twice
# (if it became six on the second roll) or three times.
#
# In this script, we want to find out what the probability is of winning
# the game in a single turn. In order to do so, we simulate playing a turn
# many times, and count how many of our simulations gave us a win.

def sim_count_yatzy_of_six(n):
    ''' Simulate a turn of sixer yatzy n times and return
    how many attempts were successful. '''
    success_count = 0
    for _ in range(n):
        if sim_yatzy_of_six():
            success_count += 1
    return success_count


def sim_yatzy_of_six():
    ''' Simulate a single turn of sixer yatzy '''
    # Initialize dice rolls to None before they are rolled first time
    dice1 = dice2 = dice3 = dice4 = dice5 = None

    # Each dice may be rolled up to three times
    for _ in range(3):
        if dice1 != 6:
            dice1 = random.randrange(1, 7)
        if dice2 != 6:
            dice2 = random.randrange(1, 7)
        if dice3 != 6:
            dice3 = random.randrange(1, 7)
        if dice4 != 6:
            dice4 = random.randrange(1, 7)
        if dice5 != 6:
            dice5 = random.randrange(1, 7)

    return are_all_six(dice1, dice2, dice3, dice4, dice5)


def are_all_six(dice1, dice2, dice3, dice4, dice5):
    ''' Return True if all dice rolls are six, False otherwise. '''
    for dice in (dice1, dice2, dice3, dice4, dice5):
        if dice != 6:
            return False
    return True


if __name__ == '__main__':
    n = 1000
    success = sim_count_yatzy_of_six(n)
    print(f'{success}/{n} attempts to get a sixer yatzy were successful')