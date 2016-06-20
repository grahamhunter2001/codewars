def iq_test(numbers):
    evens, odds = [] , []
    l = numbers.split()
    for n in l:
        if int(n) % 2 == 0:
            evens.append(l.index(n))
        else:
            odds.append(l.index(n))
    if len(evens) > len(odds):
        return odds[0]+1
    else:
        return evens[0]+1
