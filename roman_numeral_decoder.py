def solution(roman):
    year = 0
    rn = {
        "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }
    for char in range(len(roman)):
        try:
            if rn[roman[char]] >= rn[roman[char+1]]:
                year += rn[roman[char]]
            else:
                year -= rn[roman[char]]
        except: year += rn[roman[char]]
    return year
