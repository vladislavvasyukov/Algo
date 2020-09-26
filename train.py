from stack import Stack


def infix_to_postfix(string):
    stack = Stack()
    prec = {
        '/': 3,
        '*': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    postfix_list = []

    for token in string:
        if token.isdigit():
            postfix_list.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = stack.pop()
        else:
            while len(stack) > 0 and prec[stack.peek()] >= prec[token]:
                postfix_list.append(stack.pop())
            stack.push(token)

    while len(stack) > 0:
        postfix_list.append(stack.pop())

    return ''.join(postfix_list)


if __name__ == '__main__':
    print(infix_to_postfix('(8+9)*(2+1)'))
