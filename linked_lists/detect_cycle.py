"""
https://www.interviewbit.com/problems/list-cycle/
"""
from singly import * 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
        
    def isCycle(self, A):
        slow = A
        fast = A
        while True:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                return None
            if slow == None or fast == None:
                return None
            if slow == fast:
                return slow

    def numNodesInCycle(self, node):
        count = 0
        current_node = node.next
        while current_node:
            count += 1
            if current_node == node:
                return count 
            current_node = current_node.next

    def detectCycle(self, A):
        node_in_cycle = self.isCycle(A)
        if not node_in_cycle:
            return None
        # how many nodes in a loop
        num_nodes_in_cycle = self.numNodesInCycle(node_in_cycle)
        ptr1 = A
        ptr2 = A
        # move two points the loop length apart
        for _ in range(num_nodes_in_cycle):
            ptr2 = ptr2.next
        
        # after traversing the loop length they both should meet at starting point
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

def main():
    soln = Solution()
    l = SinglyList()
    l.add_node(1)
    l.add_node(2)
    l.add_node(3)
    l.add_node(4)
    l.add_node(5)
    l.add_node(6)

    second_node = l.head.next.next.next.next.next
    last_node = l.tail
    last_node.next = second_node
    #print l
    print soln.detectCycle(l.head)    

if __name__ == "__main__":
    main()
