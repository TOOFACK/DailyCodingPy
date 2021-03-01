class Codec:

    cer = "http://tinyurl.com/"
    enc = {}
    dec = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        lst = []
        ert = 1
        n = 13
        sep = longUrl.split("/")
        for i in sep[-1]:
            ert += ord(i) * 13**n
        ert = int(ert/37)
        self.enc[self.cer+str(ert)] = longUrl
        self.dec[longUrl] = self.cer+str(ert)
        return self.cer+str(ert)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.enc[shortUrl]
