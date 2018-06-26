"""
https://www.interviewbit.com/problems/jump-game-array/
"""
import sys

def jumpGame(array):
    min_jumps = sys.maxint
    queue = []
    visited = set()
    queue.append((0, 1))
    while queue:
        current_idx, level = queue.pop(0)
        if current_idx == len(array) - 1:
            return level

        if current_idx + array[current_idx] == len(array) -1:
            return level

        if current_idx in visited:
            continue 
        visited.add(current_idx)
        for next_idx in range(current_idx+1, len(array)):
            queue.append((next_idx, level+1))
    return -1
        
def main():
    array = [2,3,1,1,4]
    print jumpGame(array)


if __name__ == "__main__":
    main()
