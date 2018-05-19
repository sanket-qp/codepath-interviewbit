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
    def __isPalindrome(self, current_node, current_node_index, middle_node_index, num_nodes):
        if current_node_index == middle_node_index:
            print current_node_index, current_node, current_node.next
            if num_nodes % 2 == 0:
                is_pali = 1 if current_node.value == current_node.next.value else 0
                current_node = current_node.next
            return (current_node.next, is_pali) 

        right_half_node, is_palindrome = self.__isPalindrome(current_node.next, current_node_index + 1, middle_node_index, num_nodes)
        x = 1 if right_half_node.value == current_node.value else 0
        return (right_half_node.next, is_palindrome & x)
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    def isPalindrome(self, A):
        num_nodes = self.__get_num_of_nodes(A)
        middle_node_index = math.ceil(num_nodes/2.0)
        if num_nodes == 2:
            return 1 if A.value == A.next.value else 0

        middle_node_index = math.ceil(num_nodes/2.0)
        print num_nodes, middle_node_index
        current_node_index = 1
        _, is_palindrome = self.__isPalindrome(A, current_node_index, middle_node_index, num_nodes)
        return is_palindrome

def main():
    soln = Solution()
    l = SinglyList()
    l.add_node(4)
    l.add_node(28)
    l.add_node(6)
    l.add_node(23)
    l.add_node(46)
    l.add_node(46)
    l.add_node(23)
    l.add_node(6)
    l.add_node(28)
    l.add_node(4)
    print soln.isPalindrome(l.head)

if __name__ == "__main__":
    main()
