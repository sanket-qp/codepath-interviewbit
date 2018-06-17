"""
https://www.hackerrank.com/challenges/counter-game/problem
"""
from itertools import cycle

def isPowerOfTwo(n):
    return n != 0 and ((n & n-1) == 0)

def largestPowerOfTwoLessThan(n):
    if n > 0:
        return 1 << n.bit_length() - 1
    else:
        raise Exception("invalid n:%d" % n)

def xlargestPowerOfTwoLessThan(n):
    if n < 2:
        raise Exception("invalid n:%d" % n)
    for i in range(n, 1, -1):
        if isPowerOfTwo(i):
            return i
    return i

def whoWins(n, current_player, players, memo={}):
    print n, current_player
    if n == 1:
        return next(players)

    if isPowerOfTwo(n):
        return whoWins(n/2, next(players), players)
    else:
        return whoWins(n-largestPowerOfTwoLessThan(n), next(players), players)
        

def counterGame(array):
    for n in array:
        memo = {}
        players = cycle(('Louise', 'Richard'))
        # Louise starts the game
        current_player = next(players)
        print "%s" % whoWins(n, current_player, players)
        print "------------------"

def main():
    array = [10, 8, 6, 17]
    counterGame(array)

if __name__ == "__main__":
    main()
