"""
https://www.interviewbit.com/problems/diffk-ii/
"""
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) == 1:
            return 0

        dict_A = {}
        for i, n in enumerate(A):
            if n in dict_A:
                dict_A[n].add(i)
            else:
                dict_A[n] = set()
                dict_A[n].add(i)

        for j, a_j in enumerate(A):
            a_i = B + a_j
            # check if a_i is in dict         
            if a_i in dict_A:
                indices = dict_A[a_i]
                temp_lst = []
                for i in indices:
                    if i == j:
                        continue
                    temp_lst.append(i)
                if len(temp_lst) > 0:
                    return 1
        return 0

def main():
    soln = Solution()
    print soln.diffPossible([ 1, 5, 4, 1, 2 ], 0)

if __name__ == "__main__":
    main()
