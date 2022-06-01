class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


def parenthesis_checker(expression):
    stack = Stack()
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for symbol in expression:
        if symbol in pairs:
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False

            top = stack.pop()
            if pairs[top] != symbol:
                return False

    return stack.is_empty()


def infix_to_postfix(expression: str):
    priority_operations_dict = {
        "/": 3,
        "*": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }

    stack = Stack()
    postfix_list = []
    infix_list = expression.split()
    for token in infix_list:
        if token.isdigit():
            postfix_list.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            top_token = stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = stack.pop()
        else:
            while not stack.is_empty() and priority_operations_dict[stack.peek()] >= priority_operations_dict[token]:
                postfix_list.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix_list.append(stack.pop())

    return " ".join(postfix_list)


def calculate(postfix_string):
    stack = Stack()
    for ch in postfix_string.split():
        if ch.isdigit():
            stack.push(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            res = do_math(ch, int(op1), int(op2))
            stack.push(res)

    return stack.pop()


def do_math(symbol, op1, op2):
    if symbol == '/':
        return op1 / op2
    elif symbol == '*':
        return op1 * op2
    elif symbol == '-':
        return op1 - op2
    else:
        return op1 + op2
