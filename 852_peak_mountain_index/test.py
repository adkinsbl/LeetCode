class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
        
Solution = Solution()
c = Solution.peakIndexInMountainArray([0,2,1,0])
print(c)