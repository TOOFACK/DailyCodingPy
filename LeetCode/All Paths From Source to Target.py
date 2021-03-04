class Solution(object):

    def allPathsSourceTarget(self, graph):

        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(curr, path):
            if curr == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[curr]: dfs(i, path + [i])

        res = []
        dfs(0, [0])
        return res


#
# class Solution(object):
# #
# #     def __init__(self):
# #         self.paths = []
# #
# #     def allPathsSourceTarget(self, graph):
# #         """
# #         :type graph: List[List[int]]
# #         :rtype: List[List[int]]
# #         """
# #
# #         self.dfs(0, graph, "0")
# #         print(self.paths)
# #         for i in self.paths:
# #             if i[-1] != (len(graph)-1):
# #                 self.paths.remove(i)
# #         print(self.paths)
# #         return self.paths
# #
# #     def dfs(self, param, graph, curPath):
# #
# #         lst = graph[param]
# #         if lst:
# #             if param == (len(graph)-1):
# #                 lst = []
# #                 for i in curPath:
# #                     lst.append(int(i))
# #                 self.paths.append(lst)
# #                 return
# #             for v in lst:
# #                 self.dfs(v, graph, curPath + str(v))
# #         else:
# #             lst = []
# #             for i in curPath:
# #                 lst.append(int(i))
# #             self.paths.append(lst)
# #
# #
# # s = Solution()
# # lst = s.allPathsSourceTarget([[1,2],[3],[3],[]])
# # print(s.paths)
# # print(lst)
#
#
# class Solution(object):
#
#     def allPathsSourceTarget(self, graph):
#
#         """
#         :type graph: List[List[int]]
#         :rtype: List[List[int]]
#         """
#
#         def dfs(curr, path):
#             if curr == len(graph) - 1:
#                 res.append(path)
#             else:
#                 for i in graph[curr]: dfs(i, path + [i])
#
#         res = []
#         dfs(0, [0])
#         return res

