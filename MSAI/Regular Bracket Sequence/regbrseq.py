def is_regular_bracket_sequence(s):
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in bracket_map.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_map.keys():
            # Check if the stack is empty or the top of the stack doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Pop the top of the stack since we found a match
            stack.pop()

    # If the stack is empty at the end, it means all brackets matched properly
    if len(stack) == 0:
        return 'yes'
    return 'no'


def is_regular_bracket_sequence(s):
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in bracket_map.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_map.keys():
            # Check if the stack is empty or the top of the stack doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Pop the top of the stack since we found a match
            stack.pop()

    # If the stack is empty at the end, it means all brackets matched properly
    if len(stack) == 0:
        return 'yes'
    return 'no'


def bs_correct(x):
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    s = []
    for c in x:
        if c in bracket_map.keys():
            s.append(c)
        else:
            if len(s) == 0:
                return False
            if bracket_map[s.pop()] != c:
                return False
    return len(s) == 0


if __name__ == '__main__':
    s = input()
    #print(is_regular_bracket_sequence(s))
    print('yes' if bs_correct(s) else 'no')

