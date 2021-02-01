class StackMax:
    def __init__(self):
        self.items = []
        self.maxItems = []

    def push(self, item):
        self.items.append(item)
        if len(self.maxItems) != 0:
            if self.maxItems[-1] <= item:
                self.maxItems.append(item)
        else:
            self.maxItems.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "error"
        elif self.items[-1] == self.maxItems[-1]:
            self.maxItems.pop()
            self.items.pop()
        else:
            self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if len(self.maxItems) == 0:
            return "None"
        return self.maxItems[-1]


temp = int(input())
ans = []
stack = StackMax()
for i in range(temp):
    word = input()
    # print(word)
    if word == "get_max":
        ans.append(stack.get_max())
        # print(stack.get_max())
    elif word.split(" ")[0] == "push":
        t = word.split(" ")
        # print("t = ", t[1])
        stack.push(t[1])
        # ans.append(stack.push(t))
    else:
        r = stack.pop()
        if r is not None:
            # print(r)
            ans.append(stack.pop())
for i in ans:
    print(i)
