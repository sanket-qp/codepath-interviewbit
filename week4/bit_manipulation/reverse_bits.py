"""
https://www.interviewbit.com/problems/number-of-1-bits/
"""
def reverse_bits(n):
    result = 0
    counter = 32
    while counter >= 1:
        counter -= 1
        right_most_bit = n & 1
        print result, bin(result)
        print n, bin(n)
        result = (result << 1) + right_most_bit
        n = n >> 1 
    return result

def main():
    #assert reverse_bits(int('1000', 2)) == int('0001', 2)
    #assert reverse_bits(int('1111', 2)) == int('1111', 2)
    assert reverse_bits(int('0011', 2)) == int('1100', 2)

if __name__ == "__main__":
    main() 
