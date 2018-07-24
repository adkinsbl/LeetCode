class Codec:
    alphabet = "!@#$%^&*()abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(alphabet)
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        longNum = list(map(lambda x: ord(x),longUrl))
        longNum = ''.join(map(lambda x: str(x).zfill(3),longNum))
        longNum = int(longNum)
        arr = []
        if longNum == 0:
                return Codec.alphabet[0]
                # continue
        while longNum:
            longNum, rem = divmod(longNum,Codec.base)
            arr.append(Codec.alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        sum = 0
        for pow,num in enumerate(reversed(shortUrl)):
            idx = Codec.alphabet.index(num)
            sum += idx * (Codec.base**pow)
        sum = str(sum)
        hmm = [sum[i:i+3] for i in range(0,len(sum),3)]
        url = ""
        for hm in hmm:
            url += chr(int(hm))
        return url

# Your Codec object will be instantiated and called as such:
codec = Codec()
c = codec.encode("http://tinyurl.com/4e9iAk")
print(c)
d = codec.decode(c)
print(d)