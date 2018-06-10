"""
https://www.interviewbit.com/problems/number-of-1-bits/
"""
def num_of_1_bits(n):
    counter = 1 if (n & 1) else 0
    for _ in range(32):
        n = n >> 1
        if n & 1:
            counter += 1
    return counter

def main():
    assert num_of_1_bits(int('1000', 2)) == 1
    assert num_of_1_bits(int('1111', 2)) == 4

if __name__ == "__main__":
    main() 
