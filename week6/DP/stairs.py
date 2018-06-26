"""
https://www.interviewbit.com/problems/stairs/
"""
def numOfWays(n, memo):
    
    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    memo[n] = numOfWays(n-1, memo) + numOfWays(n-2, memo)
    return memo[n]

def main():
    memo = {}
    print numOfWays(4, memo)

if __name__ == "__main__":
    main()
