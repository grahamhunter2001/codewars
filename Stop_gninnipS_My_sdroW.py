def spin_words(sentence):
    out = ""
    string = []
    for word in sentence.split():
        if len(word)>=5:
            string.append(word[::-1])
        else:
            string.append(word)
    return ' '.join(string)
