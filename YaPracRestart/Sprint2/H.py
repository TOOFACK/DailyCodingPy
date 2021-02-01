str = input()


def is_correct_bracket_seq(str):
    stack = []
    if str == "":
        return True
    for i in str:
        if i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif i == "(":
            stack.append(")")
        if not stack:
            return False
        if i == "}" and stack.pop() != i:
            return False
        if i == "]" and stack.pop() != i:
            return False
        if i == ")" and stack.pop() != i:
            return False


    if stack:
        return False
    return True


print(is_correct_bracket_seq(str))
