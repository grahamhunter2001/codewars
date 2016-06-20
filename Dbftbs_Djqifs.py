import re, string
def encryptor(key, message):
    if message:
        out_string = ""
        for char in message:
            regex = r"([a-zA-Z]+)"
            if re.search(regex,char):
                if char.islower():
                    new_char = string.lowercase.index(char) + key
                    new_char = new_char % 26
                    out_string += string.lowercase[new_char]
                else:
                    new_char = string.uppercase.index(char) + key
                    new_char = new_char % 26
                    out_string += string.uppercase[new_char]
            else:
                out_string += char
        return out_string
    else:
        return ''
