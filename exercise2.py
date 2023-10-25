opening_brackets = ["[", "{", "("]
closing_parentheses = ["]", "}", ")"]


def checking_parentheses(data):
    stack = []
    for _ in data:
        if _ in opening_brackets:
            stack.append(_)
        elif _ in closing_parentheses:
            i = closing_parentheses.index(_)
            if ((len(stack) > 0) and
                    (opening_brackets[i] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Несбалансированно"
    if len(stack) == 0:
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == "__main__":
    print(checking_parentheses('(((([{}]))))'))
