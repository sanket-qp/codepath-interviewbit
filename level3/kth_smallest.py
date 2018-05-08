"""
Find the kth smallest element in an unsorted array of non-negative integers.

NOTE
You are not allowed to modify the array ( The array is read only ). 
Try to do it using constant extra space.

A : [2 1 4 3 2]
k : 3

answer : 2
"""
import random
import heapq

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        heap = []
        kth_smallest = -1
        for n in A:
            heapq.heappush(heap, n)
        for _ in range(B, 0, -1):
            kth_smallest = heapq.heappop(heap)
        return kth_smallest
            
def main():
    soln = Solution()
    lst = [random.randint(1, 10) for _ in range(10)]
    kth_smallest = soln.kthsmallest(lst, 9)
    print "kth_smallest: %s from list: %s" % (kth_smallest, lst)

if __name__ == "__main__":
    main()
