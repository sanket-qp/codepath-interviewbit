"""
https://www.interviewbit.com/problems/black-shapes/
"""
class Solution:
    # @param A : list of strings
    # @return an integer
    visited = 'V'    

    def black(self, A):
        graph = []
        for s in A:
            graph.append([ch for ch in s])
        rows = len(graph)
        cols = len(graph[0])
        count = 0
        #print rows, cols
        #print graph
        for row in range(rows):
            for col in range(cols):
                if graph[row][col] == self.visited:
                    continue
                if graph[row][col] == 'O':
                    continue 
                self.__dfs(row, col, graph, rows, cols)
                count += 1
                #print graph
    
        #print "final"
        #print graph
        return count 

    def __dfs(self, row, col, graph, total_rows, total_cols):
        
        if graph[row][col] == 'O':
            return 

        if graph[row][col] == self.visited:
            return 

        graph[row][col] = self.visited

        for new_row, new_col in self.__get_neighbors(row, col, graph):
            if new_row < 0 or new_row >= total_rows:
                continue
            if new_col < 0 or new_col >= total_cols:
                continue

            #print new_row, new_col
            self.__dfs(new_row, new_col, graph, total_rows, total_cols)
            
    def __get_neighbors(self, row, col, graph):
        return ((row, col+1), (row, col-1), (row-1, col), (row+1, col))

def main():
    soln = Solution()
    lst = [
        "OOOXOOO",
        "OOXXOXO",
        "OXOOOXO"
    ]
    print soln.black(lst)

if __name__ == "__main__":
    main()
