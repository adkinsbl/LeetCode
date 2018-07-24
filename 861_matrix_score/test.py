class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        numR = len(A)
        numC = len(A[0])
        for r, row in enumerate(A):
            if (not row[0]):
                A[r] = self.flipList(row)
        for c in range(numC):
            # print(c)
            col = self.column(A,c)
            if (col.count(1) < col.count(0)):
                col = self.flipList(col);
                for i in range(numR):
                    A[i][c] = col[i]

        return self.scoring(A)
        
    def scoring(self,A):
        scor = 0
        for r in A:
            b = ''.join(str(e) for e in r)
            scor += int(b,2)
        return scor

    def column(self,A,i):
        return [row[i] for row in A]
        
    def flipList(self,L):
        return list(map(lambda x: (1,0)[x],L))
        
Solution = Solution()
c = Solution.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
print(c)