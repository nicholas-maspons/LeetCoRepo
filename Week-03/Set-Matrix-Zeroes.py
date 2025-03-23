# 73. Set Matrix Zeroes

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        # find
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Set to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

sol = Solution()  
sol.setZeroes(matrix)
print(matrix)  
