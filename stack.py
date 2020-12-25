class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def parenthesis_checker(string):
    stack = Stack()
    balanced = True
    for ch in string:
        if ch == '(':
            stack.push(ch)
        else:
            if len(stack) == 0:
                balanced = False
                break
            else:
                stack.pop()

    return balanced and len(stack) == 0


def infix_to_postfix(string):
    prec = {
        "/": 3,
        "*": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }

    stack = Stack()
    postfix_list = []
    infix_list = string.split()
    for el in infix_list:
        if el.isdigit():
            postfix_list.append(el)
        elif el == '(':
            stack.push(el)
        elif el == ')':
            top_el = stack.pop()
            while top_el != '(':
                postfix_list.append(top_el)
                top_el = stack.pop()
        else:
            while len(stack) > 0 and prec[stack.peek()] >= prec[el]:
                postfix_list.append(stack.pop())
            stack.push(el)

    while len(stack) > 0:
        postfix_list.append(stack.pop())

    return ' '.join(postfix_list)


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


if __name__ == '__main__':
    s1 = '()()()'
    s2 = '((()))'
    s3 = '())('
    for s in (s1, s2, s3):
        print(parenthesis_checker(s))
    # print(infix_to_postfix("( 1 + 2 ) * ( 3 + 4 )"))
    st = infix_to_postfix("( 1 + 2 ) * ( 3 + 4 )")
    # print(st)
    print(calculate(st))

