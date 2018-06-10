"""
https://www.interviewbit.com/problems/single-number/
https://www.youtube.com/watch?v=eXWjCgbL01U
"""
def single_number(array):
    result = 0
    for n in array:
        result ^= n
    return result

def main():
    print single_number([1,2,2,3,1])

if __name__ == "__main__":
    main()
