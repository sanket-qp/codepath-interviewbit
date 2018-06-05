# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
import random

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = []
        for lst in A:
            for n in lst:
                heapq.heappush(heap, n)

        while True:
            try:
                x = heapq.heappop(heap)
                print x
            except IndexError, e:
                break

def main():
    A = []
    K = 3
    for i in range(K):
        A.append([random.randint(0, 50) for _ in range(5)])
    print A
    soln = Solution()
    soln.mergeKLists(A)

if __name__ == "__main__":
    main()
