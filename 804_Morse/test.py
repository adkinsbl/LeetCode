class Solution(object):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morsewords = {}
        for word in words:
            morsewords[''.join(list(map(lambda x: Solution.morse[Solution.alphabet.index(x)],word)))] = 1
        return len(list(morsewords))

Solution = Solution()
c = Solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(c)