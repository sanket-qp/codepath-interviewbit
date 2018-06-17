"""
https://www.hackerrank.com/challenges/pascals-triangle/problem
"""
import sys
def pascalTriangle(k):
    memo = []
    for i in range(k):
        row = [None] * k
        memo.append(row)

    memo[0][0] = 1
    print "%s" % memo[0][0]
    for row in range(1, k):
        num_elements = row + 1
        for j in range(num_elements):
            if j == 0 or j == num_elements-1:
                memo[row][j] = 1
            else:
                memo[row][j] = memo[row-1][j] + memo[row-1][j-1]
            sys.stdout.write("%s " % memo[row][j])
        print ""
                
def main():
    pascalTriangle(10)

if __name__ == "__main__":
    main()
