"""
https://www.interviewbit.com/problems/possibility-of-finishing-all-courses-given-prerequisites/
"""
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        graph = self.__buildGraph(B, C)
        # lets do DFS on each node of B 
        for b in B:
            visited = set()
            x = self.__dfs(b, graph, visited)
            if not x:
                return 0
        return 1

    def __dfs(self, vertex, graph, visited):
        if vertex not in graph:
            return True

        if vertex in visited:
            return False

        visited.add(vertex)
        for neighbor in graph[vertex]:
            x = self.__dfs(neighbor, graph, visited)         
            if not x:
                return False
        return True

    def __buildGraph(self, B, C):
        graph = {}
        for b, c in zip(B, C):
            if b not in graph:
                graph[b] = set()
            graph[b].add(c)
        return graph

def main():
    soln = Solution()
    print soln.solve(3, (1, 2), (2, 3))
    print soln.solve(2, (1, 2), (2, 1))
    print soln.solve(5, (1, 2, 3, 4), (2, 3, 1, 5))


if __name__ == "__main__":
    main()
