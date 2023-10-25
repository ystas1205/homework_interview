class Stack:
    list_stack: list = []

    def isEmpty(self):
        if not self.list_stack:
            return True
        return False

    def push(self):
        self.list_stack.append(4)

    def pop(self):
        element_stack = self.list_stack.pop()
        return element_stack

    def peek(self):
        return self.list_stack[-1]

    def size(self):
        return len(self.list_stack)


if __name__ == '__main__':

    stack = Stack()
    print(stack.isEmpty())
    print(stack.push())
    print(stack.push())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
