class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = A
        for r, row in enumerate(B):
            row.reverse()
            B[r] = list(map(lambda x: (1,0)[x], row))
        return B
        
Solution = Solution();
c = Solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print(c)