class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        result = [0] * len(A)
        for idx in range(len(A)-1, -1, -1):
            _sum = A[idx] + carry
            if _sum > 9:
                _sum = 0
                carry = 1
            else:
                carry = 0
            #result = [_sum] + result
            result[idx] += _sum

        if carry:
            result = [carry] + result         
        
        # remove leading 0s
        idx = 0
        while True:
            if result[idx] == 0:
                result.pop(0)
            else:
                break
        return result

def main():
    soln = Solution()
    #soln.plusOne([1,2,3])
    print soln.plusOne([9, 9, 9])
    print soln.plusOne([0, 0, 0, 0])
    print soln.plusOne([0, 0, 3, 7, 6, 4, 0, 5, 5, 5 ])

if __name__ == "__main__":
    main()
