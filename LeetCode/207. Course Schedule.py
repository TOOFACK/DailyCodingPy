class Solution(object):

    def __init__(self):
        self.graph = {}
        self.colored = []

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        for i in range(numCourses):
            self.colored.append("w")

        for a, b in prerequisites:
            if a in self.graph:
                self.graph[a].append(b)
            else:
                self.graph[a] = [b]

        def dfs(root):
            if self.colored[root] == "w":
                if root not in self.graph:
                    self.colored[root] = "w"
                    return True
                self.colored[root] = "g"
                can_finish = True
                for must_to_takes_course in self.graph[root]:
                    can_finish = dfs(must_to_takes_course)
                    if not can_finish:
                        return False
                if can_finish:
                    self.colored[root] = "b"
                    return True
            elif self.colored[root] == "b":
                return True
            else:
                return False

        for root in range(numCourses):
            can_finish = True
            if self.colored[root] == "w" and root in self.graph:
                self.colored[root] = "g"
                for must_to_takes_course in self.graph[root]:
                    can_finish = dfs(must_to_takes_course)
                    if not can_finish:
                        break
                if can_finish:
                    self.colored[root] = "b"

        for cours in range(numCourses):
            if cours not in self.graph:
                self.colored[cours] = "b"
        print(self.colored)
        for i in self.colored:
            if i != "b":
                print("false")
                return False
        print("true")
        return True
