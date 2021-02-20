from collections import Counter, defaultdict


class Solution(object):

    def countSubTrees(self, n, edges, labels):
        def dfs(node, parent):
            cnt = Counter(labels[node])

            for i in g.get(node):
                if i != parent:
                    cnt += dfs(i, node)
            ans[node] = cnt[labels[node]]
            return cnt

        g, ans = defaultdict(list), [0] * n
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        dfs(0, -1)
        return ans

s = Solution()
s.countSubTrees(5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab")
