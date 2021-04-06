class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.dic = set()

        def dfs(stroka, dict, lenght):
            print("stroka = ", stroka)
            print("dict = ", dict)
            print("len = ", len(stroka))
            if len(stroka) == lenght:
                self.dic.add(stroka)
                return
            new_dict = dict
            for s in dict:
                new_dict = new_dict.replace(s, "")
                dfs(stroka + s, new_dict, lenght)

        dict = characters
        for s in characters:
            dict = dict.replace(s, "")
            dfs(s, dict, combinationLength)

        print(sorted(self.dic))


s = CombinationIterator("gkosu", 3)
