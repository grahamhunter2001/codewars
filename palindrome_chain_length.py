def palindrome_chain_length(n):
    n = str(n)
    steps = 0
    digits = len(n)
    if digits == 1:
        return 0
    while True:
        if digits % 2 == 0:
            if n[::digits/2] == n[::-digits/2]:
                return steps
            else:
                n = str(int(n) + int(n[::-1]))
                steps += 1
        else:
            if n[::(digits-1)/2] == n[::-(digits-1)/2]:
                return steps
            else:
                n = str(int(n) + int(n[::-1]))
                steps += 1
