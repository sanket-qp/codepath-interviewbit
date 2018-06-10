"""
https://www.interviewbit.com/problems/min-xor-value/
"""
import sys
def min_xor(array): 
    min_value = sys.maxsize
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            xor = array[i] ^ array[j]
            min_value = min(min_value, xor)
    return min_value

def main():
    print min_xor([0, 2, 5, 7])
    print min_xor([0, 4, 7, 9])

if __name__ == "__main__":
    main() 
