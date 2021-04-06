import collections
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.dic = set()

        def dfs(stroka, dict, lenght):
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
        self.q = collections.deque(sorted(self.dic))


    def next(self):
        """
        :rtype: str
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.q

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

