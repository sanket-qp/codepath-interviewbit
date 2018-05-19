"""
https://www.interviewbit.com/problems/colorful-number/
"""
class Solution:
    # @param A : integer
    # @return an integer

    def getSubSequences(self, strA):
        sub_sequences = []
        for seq_len in xrange(1, len(strA)+1):
            start = 0
            while (start + seq_len) <= len(strA):
                sub_sequences.append(strA[start:start+seq_len])
                start += 1
        return sub_sequences

    def getProduct(self, seq):
        product = 1
        for n in seq:
            product *= int(n)
        return product

    def colorful(self, A):
        # convert in to string for easy slicing
        product_dict = {}
        for seq in self.getSubSequences(str(A)):
            product = self.getProduct(seq)
            #print seq, product
            if product in product_dict:
                return 0
            product_dict[product] = True
        return 1


def main():
    soln = Solution()
    print soln.colorful(12)

if __name__ == "__main__":
    main()
