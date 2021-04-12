class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a1,a2 = map(int, a[:-1].split("+"))
        b1,b2 = map(int, b[:-1].split('+'))
        print(a1,a2)
        print(b1,b2)
        print(str(a1*b1+a2*-b2) + "+" + str(a1*b2+b1*a2)+"i")
        return str(a1*b1+a2*-b2) + "+" + str(a1*b2+b1*a2)+"i"


s = Solution()
s.complexNumberMultiply("1+-1i", "1+-1i")
