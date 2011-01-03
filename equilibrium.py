def equilibrium ( A ):
    # Finds an equilibrium index for the sequence A if one exists
    index = 0
    while index < len(A):
        left = 0
        right = 0
        if index > 0:
            left = sum(A[:index])
        if index < len(A) - 1:
            right = sum(A[index+1:])
        if left == right:
            return index
        index += 1
    return -1
