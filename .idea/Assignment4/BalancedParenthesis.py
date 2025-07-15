def is_balanced():
    expr = input("Enter parentheses string: ")
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                print("Balanced:", False)
                return
    print("Balanced:", not stack)

is_balanced()