class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = []

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if self.nodes:
            cur_node = self.nodes[0]
        else:
            self.nodes.append({})
            cur_node = self.nodes[0]

        for i in word:
            if i not in cur_node:
                cur_node[i] = len(self.nodes)
                self.nodes.append({})
            idx = cur_node[i]
            cur_node = self.nodes[cur_node[i]]

        # print(self.nodes)
        print("idx= ",idx)
        cur_node[idx] = idx

        # self.nodes[-1] = {len(self.nodes)-1:len(self.nodes)-1}

        print(self.nodes)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not self.nodes:
            return False
        else:
            cur_node = self.nodes[0]
            for i in word:
                if i not in cur_node:
                    return False
                else:
                    idx = cur_node[i]
                    cur_node = self.nodes[cur_node[i]]

            if idx in cur_node:
                return True
            else:
                return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not self.nodes:
            return False
        else:
            cur_node = self.nodes[0]
            for i in prefix:
                if i not in cur_node:
                    return False
                else:
                    cur_node = self.nodes[cur_node[i]]
            return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()
trie.insert("app")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("apple")
print(trie.search("app"))
trie.insert("beer")