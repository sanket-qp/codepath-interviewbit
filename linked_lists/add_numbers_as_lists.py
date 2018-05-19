"""
https://www.interviewbit.com/problems/add-two-numbers-as-lists/
"""
from singly import * 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def printList(self, head):
        while head:
            print head.val
            head = head.next
        print "---------------"

    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        current_A = A
        current_B = B
        current_sum = None
        has_carry = False
        carry = 0
        head = None 
        while True:
            print current_A, current_B
            if not current_A and not current_B:
                break
            elif current_A == None:
                x = current_B.value
            elif current_B == None:     
                x = current_A.value
            else:
                x = current_A.value + current_B.value

            if has_carry:
                x = x + carry

            if x > 9:
                has_carry = True
                carry = x/10
                x = x % 10
            else:
                has_carry = False
                carry = 0

            if not current_sum:
                current_sum = ListNode(x)
                head = current_sum
            else:
                current_sum.next = ListNode(x)
                current_sum = current_sum.next

            if current_A:
                current_A = current_A.next
            if current_B:
                current_B = current_B.next

        if carry > 0:
            current_sum.next = ListNode(carry)

        return head
        

def main():
    soln = Solution()
    l1 = SinglyList()
    l2 = SinglyList()
    l1.add_node(0)
    l2.add_node(1)
    l2.add_node(0)
    l2.add_node(1)
    x = soln.addTwoNumbers(l1.head, l2.head)
    while x:
        print x
        x = x.next

if __name__ == "__main__":
    main()
