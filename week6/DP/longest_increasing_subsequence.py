"""
https://www.interviewbit.com/problems/longest-increasing-subsequence/
"""
def longestIncreasingSubSeq(array):
    # let's store increasing seq length and decreasing seq length
    memo = [1 for _ in range(len(array))]
    max_seq = 1
    for i in range(1, len(array)):
        print array[i]
        for j in range(0, i):
            print "current(%d, %d) : %s" % (i, j, memo[j])
            print array[j], array[i]
            print array
            print memo

            if array[j] < array[i]:
                print "%d < %d" % (array[j], array[i])
                memo[i] = max(memo[j] + 1, memo[i])
                max_seq = max(max_seq, memo[i])
            print memo
            print "---------"
        print "------------------"

    return max_seq

def main():
    array = [ 7, 6, 8, 10, 2, 5, 12, 30, 31, 20, 22, 18 ]
    array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print "%s: %s" % (array, longestIncreasingSubSeq(array))

if __name__ == "__main__":
    main()
