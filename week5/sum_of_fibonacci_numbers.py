"""
https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/
"""
import sys
class Solution:
    def solve(self, N):
        numbers = self.__fibNumbersUpToN(N)
        if N in numbers:
            return 1

        # do BFS on each number
        _min = sys.maxint
        for n in numbers:
            _sum = self.__bfs(n, numbers, N)
            _min = min(_sum, _min)
        return _min

    def __bfs(self, n, numbers, N):
        queue = []
        queue.append((n, 1))
        visited = set()
        _sum = 1
        while queue:
            current, _sum = queue.pop(0)
            #print "hello", current, _sum
            visited.add(current)
            if current == N:
                return _sum
            # each number is a neighbor
            for x in numbers:
                if x in visited:
                    continue
                queue.append((x+current, _sum+1))
                #print queue
        return _sum    

    def __fibNumbersUpToN(self, N):
        if N == 1:
            return [1]
        lst = [1, 1]
        num_0 = 1
        num_1 = 1
        idx = 2
        while True:
            current = num_0 + num_1
            if current > N:
                break
            lst.append(current)
            num_0 = num_1
            num_1 = current
            idx += 1
        return lst

def main():
    soln = Solution()
    print soln.solve(5)


if __name__ == "__main__":
    main()
