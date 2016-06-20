def hamming_weight(x):
    # have you already looked it up?
    a = '{0:08b}'.format(x)
    counter = 0
    for char in a:
        if char == "1":
            counter += 1
    return counter
