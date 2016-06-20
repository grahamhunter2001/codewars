def order(sentence):
    words = sentence.split()
    out_sen = [0]*len(words)
    for word in words:
        for char in word:
            try:
                place = int(char) - 1
                out_sen[place] = word
            except:
                pass
    string = " ".join(out_sen)
    return string
