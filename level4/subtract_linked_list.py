# -*- coding: utf-8 -*-
"""
Given a singly linked list, modify the value of first half nodes such that
1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,

Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,
You should return 4 -> 2 -> 3 -> 4 -> 5

as 
for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import math
import random
from singly import * 
class Solution:

    def __get_num_of_nodes(self, A):

        current_node = A
        if current_node == None:
            return 0
        if current_node.next == None:
            return 1
        num_nodes = 1 if current_node.next == None else 0 
        while current_node:
            num_nodes += 1
            current_node = current_node.next
        return num_nodes

    """
    recursively goes up to the middle of the list and backtracks towards the left side of nodes and expands towards right side of nodes
    """
    def __subtract(self, current_node, current_node_index, middle_node_index, num_nodes):
        if current_node_index == middle_node_index:
            # when list has even number of elements
            if num_nodes % 2 == 0:
                current_node.value = current_node.next.value - current_node.value
                # move the right node by one
                current_node = current_node.next
            return current_node.next 

        right_half_node = self.__subtract(current_node.next, current_node_index + 1, middle_node_index, num_nodes)
        current_node.value = right_half_node.value - current_node.value
        return right_half_node.next
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        num_nodes = self.__get_num_of_nodes(A)
        middle_node_index = math.ceil(num_nodes/2.0)
        current_node_index = 1
        print "total nodes", num_nodes
        self.__subtract(A, current_node_index, middle_node_index, num_nodes)
        return A

def main():
    soln = Solution()
    l = SinglyList()
    for _ in range(random.randint(1, 10)):
        l.add_node(random.randint(1, 100))
    print "list before subtracting: %s" % l
    soln.subtract(l.head)
    print "list after subtracting: %s" % l

if __name__ == "__main__":
    main()
