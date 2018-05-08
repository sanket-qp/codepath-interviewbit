"""
Print concentric rectangular pattern in a 2d matrix. 
Let us show you some examples to clarify what we mean.

Example 1:
input: A = 4
output:
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 


Example 2:
input: A = 3
output:
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
"""

class Solution:

    """
    creates a list for single row
    """
    def __make_list(self, max_element, min_element, num_elements):
        lst = []
        current_element = max_element
        for i in range(num_elements/2+1):
            lst.append(current_element)
            if current_element > min_element:
                current_element -= 1
        return lst + lst[:i][::-1]
        

    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A == 0:
            return [[]]

        # number of elements in a single list
        num_elements = 2*A - 1
        lists = []
        for i in range(A, 0, -1):
            lists.append(self.__make_list(A, i, num_elements))
        return lists + lists[:len(lists)-1][::-1]
            
def main():
    pprint = Solution()
    lists = pprint.prettyPrint(6)
    for x in lists:
        print x


if __name__ == "__main__":
    main()
    
