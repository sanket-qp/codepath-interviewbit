"""
https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
"""
from singly import * 

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        prev_node = None
        current_node = A
        while current_node:
            print "prev:", prev_node, "current:", current_node
            if prev_node != None and prev_node.value == current_node.value:
                prev_node.next = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next 
        return A 

def main():
    soln = Solution()
    l = SinglyList()
    l.add_node(1)
    l.add_node(1)
    l.add_node(1)
    l.add_node(1)
    l.add_node(1)
    l.add_node(1)
    l.add_node(2)
    l.add_node(2)
    l.add_node(2)
    l.add_node(2)
    l.add_node(2)
    print l
    x = soln.deleteDuplicates(l.head)
    while x:
        print x
        x = x.next

if __name__ == "__main__":
    main()
