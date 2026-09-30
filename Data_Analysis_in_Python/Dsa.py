# stack implementation using in python
'''

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def push(self, data):
        if self.top >= self.size - 1:
            print("Stack Overflow")
            return
        self.stack.append(data)
        self.top += 1,

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        popped_item = self.stack.pop()
        self.top -= 1
        return popped_item
    
    
def display_menu():
    print("Choose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Status")
    print("4. Exit")

# Function to return precedence of operators
def precedence(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0

# Check if character is an operand
def is_operand(ch):
    return ch.isalnum()  # A-Z, a-z, 0-9

def infix_to_postfix(infix):
    stack = []        # stack for operators
    postfix = ""      # result string

    for ch in infix:
        # If operand, add to output
        if is_operand(ch):
            postfix += ch

        # If opening bracket, push to stack
        elif ch == '(':
            stack.append(ch)

        # If closing bracket, pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '('

        # Operator encountered
        else:
            while (stack and precedence(stack[-1]) >= precedence(ch)):
                # Special case: ^ is right associative
                if ch == '^' and stack[-1] == '^':
                    break
                postfix += stack.pop()
            stack.append(ch)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


expression = "A+(B*C-(D/E^F)*G)*H"
print("Infix:   ", expression)
print("Postfix: ", infix_to_postfix(expression))
'''

import numpy as np

def circular_matrix(arr):
    n = len(arr)
    mat = []
    for i in range(n):
        mat.append(arr[-i:] + arr[:-i])
    return np.array(mat)

arr = [1, 2, 3, 4]
print(circular_matrix(arr))