class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        rtype = 0
        print(J)
        for j in J.split():
            print(j)
            rtype += S.numberOfOccurrences(j)
        return rtype
            
def main():
    S = Solution
    S.numJewelsInStones('aAb','afasfafa')
