def nesting( S ):
    left, right = 0
    for char in S:
        if char == '(':
            left++
        elif char == ')':
            right++

    if left == right:
        return 1
    else:
        return 0

