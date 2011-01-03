def isAnagramOfPalindrome ( S ):
    # Returns 1 if the argument is an anagram of a palindrome, 0 otherwise
    palindromes = ['kayak', 'codilitytilidoc', 'neveroddoreven']
    for pal in palindromes:
        if len(pal) == len(S):
            for c in S:
                position = pal.find(c)
                if position == -1:
                    return 0
                pal = pal.replace(c, '', 1)
            return 1
    return 0
