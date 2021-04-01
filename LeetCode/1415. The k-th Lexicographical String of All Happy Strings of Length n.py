class Solution(object):
    def __init__(self):
        self.happy_strings = []

    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def gen_happy_string(len, stroka):
            if len == n:
                self.happy_strings.append(stroka)
            else:
                if stroka[-1] == "a":
                    gen_happy_string(len + 1, stroka + "b")
                    gen_happy_string(len + 1, stroka + "c")
                elif stroka[-1] == "c":
                    gen_happy_string(len + 1, stroka + "a")
                    gen_happy_string(len + 1, stroka + "b")

                elif stroka[-1] == "b":
                    gen_happy_string(len + 1, stroka + "a")
                    gen_happy_string(len + 1, stroka + "c")

        gen_happy_string(1, "a")
        gen_happy_string(1, "b")
        gen_happy_string(1, "c")
        print(self.happy_strings)

        return sorted(self.happy_strings)[k - 1] if k <= len(self.happy_strings) else ""