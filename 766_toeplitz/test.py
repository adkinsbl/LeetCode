class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r,row in enumerate(matrix[1:],1):
            for c,val in enumerate(row[1:],1):
                if val != matrix[r-1][c-1]:
                    return False
        return True
            
        
Solution = Solution()
matrix = [
  [1,2],
  [2,2]
]
# matrix = [
  # [1,2,3,4],
  # [5,1,2,3],
  # [9,5,1,2]
# ]
c = Solution.isToeplitzMatrix(matrix)
print(c)