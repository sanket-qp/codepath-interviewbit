class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if len(A) == 0:
            return 0

        current_elem = A[0]
        A = sorted(A)
        max_seq_len = 1
        current_seq_len = 1
        for index, element in enumerate(A[:-1]):
            if A[index] == A[index+1]:
                continue            
            if element + 1 == A[index+1]:
                current_seq_len += 1
            else:
                if current_seq_len > max_seq_len:
                    max_seq_len = current_seq_len
                current_seq_len = 1
        return max(max_seq_len, current_seq_len)

def main():
    soln = Solution()
    #print soln.longestConsecutive([5, 100, 4, 200, 1, 3, 5])
    print soln.longestConsecutive([ 65, 7, 3, 29, 39, -3, 87, 85, 21, 22, 108, 89, 54, 120, 92, 1, 72, 80, 9, 117, 16, 96, 34, 4, 119, 61, 84, 35, 99, 113, 18, 59, 42, 62, -1, 69, 48, 52, 2, 102, 40, 28, 74, 104, 23, 90, 44, 0, 47, 5, 43, 111, 6, 60, 46, 10, 63, 68 ])

if __name__ == "__main__":
    main()
