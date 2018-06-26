"""
https://www.interviewbit.com/problems/length-of-longest-subsequence/
"""
def xlongestIncreasingDecreasingSubSeq(array):
    # let's store increasing seq length and decreasing seq length
    memo = [(1,1) for _ in range(len(array))]
    for i in range(1, len(array)):
        print array[i]
        for j in range(0, i):
            print array
            print memo
            increasing_len, decreasing_len = memo[j]
            print "current(%d, %d) : %s" % (i, j, memo[j])
            if array[i] == array[j]:
                memo[i] = memo[j]
            elif array[i] > array[j]:
                print "%d is > %d" % (array[i], array[j])
                memo[i] = (increasing_len + 1, decreasing_len)
            else:
                print "%d is < %d" % (array[i], array[j])
                memo[i] = (increasing_len, max(increasing_len + 1, decreasing_len + 1))
            print memo
            print "-----"
        print "---------------------------"

    print memo
    return max(memo[-1])
                
def longestIncreasingDecreasingSubSeq(array):
    # let's store increasing seq length and decreasing seq length
    memo = [(1,1) for _ in range(len(array))]
    for i in range(1, len(array)):
        print array[i]
        for j in range(0, i):
            increasing_len, decreasing_len = memo[j]
            print "current(%d, %d) : %s" % (i, j, memo[j])
            print array[j], array[i]
            print array
            print memo
            
            if array[j] == array[i]:
                continue

            if array[j] < array[i]:
                print "%d < %d" % (array[j], array[i])
                max_so_far = max(memo[i][0], increasing_len + 1)
                memo[i] = (max_so_far, memo[i][1])
                print "chaging %d: %d" % (i, increasing_len + 1)
            else:
                print "%d > %d" % (array[j], array[i])
                max_so_far = max(memo[i][1], increasing_len + 1)
                memo[i] = (memo[i][0], max_so_far)
            print memo
            print "---------"
        print "------------------"

    print memo
    return max(memo[-1])

def main():
    """
    array = [1, 11, 2, 10, 4, 5, 2, 1]
    print "%s: %s" % (array, longestIncreasingDecreasingSubSeq(array))

    array = [5, 4, 3, 2, 1]
    print "%s: %s" % (array, longestIncreasingDecreasingSubSeq(array))

    array = [1, 2, 3, 4, 5]
    print "%s: %s" % (array, longestIncreasingDecreasingSubSeq(array))
    """
    array = [ 7, 6, 8, 10, 2, 5, 12, 30, 31, 20, 22, 18 ]
    print "%s: %s" % (array, longestIncreasingDecreasingSubSeq(array))

if __name__ == "__main__":
    main()
