import re

def isvalid(expression):
    stack = []

    for ch in expression:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()

    return not stack

def calculate(expression):
    try:

        expression = re.sub("r\s", '', expression)
    
        if not isvalid(expression):
            return "Error: Unbalanced Paranthesis"
        
        result = eval(expression)
        
        return result
    
    except Exception as e:
        return f"Error: {str(e)}"
    
if __name__ == '__main__':
    print("Enter a expression or enter 'exit' to exit: ")
    usr_in = input("> ")

    if usr_in.lower() != 'exit':
        result = calculate(usr_in)
        print("Result:", result)
