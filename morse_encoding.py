class Morse:
    @classmethod
    def twos_comp(self,val, bits):
        """compute the 2's compliment of int value val"""
        if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)  # compute negative value
        return val  # return positive value as is

    @classmethod
    def bindigits(self,n, bits):
        s = bin(n & int("1" * bits, 2))[2:]
        return ("{0:0>%s}" % (bits)).format(s)

    @classmethod
    def encode(self,message):
        bits = 32
        int_array = []
        bit_rep = []
        for char in message:
            bit_rep.extend(list(alpha[char]))
            bit_rep.extend("000")
        while len(bit_rep) % bits != 0:
            bit_rep.extend("0")
        j = 0
        while len(bit_rep) != 0:
            i = 0
            bin_array = []
            while i < bits:
                bin_array.extend(bit_rep[i])
                i +=1
            del bit_rep[:i]
            b = ''.join(bin_array)
            a = self.twos_comp(int(b,2),len(b))
            int_array.append(a)
            j += 1
        return int_array

    @classmethod
    def decode(self,array):
        bits = 32
        bit_array = []
        for num in array:
            bit_array.append(self.bindigits(num,bits))
        bit_string = ''.join(bit_array)
        words = bit_string.split("0000000")
        out_string = ""
        for word in words:
            char_set = word.split("000")
            for char in char_set:
                try:
                    out_string += list(alpha.keys())[list(alpha.values()).index(char)]
                except: pass
            out_string += " "
        return out_string.strip()

alpha={
  'A': '10111',
  'B': '111010101',
  'C': '11101011101',
  'D': '1110101',
  'E': '1',
  'F': '101011101',
  'G': '111011101',
  'H': '1010101',
  'I': '101',
  'J': '1011101110111',
  'K': '111010111',
  'L': '101110101',
  'M': '1110111',
  'N': '11101',
  'O': '11101110111',
  'P': '10111011101',
  'Q': '1110111010111',
  'R': '1011101',
  'S': '10101',
  'T': '111',
  'U': '1010111',
  'V': '101010111',
  'W': '101110111',
  'X': '11101010111',
  'Y': '1110101110111',
  'Z': '11101110101',
  '0': '1110111011101110111',
  '1': '10111011101110111',
  '2': '101011101110111',
  '3': '1010101110111',
  '4': '10101010111',
  '5': '101010101',
  '6': '11101010101',
  '7': '1110111010101',
  '8': '111011101110101',
  '9': '11101110111011101',
  '.': '10111010111010111',
  ',': '1110111010101110111',
  '?': '101011101110101',
  "'": '1011101110111011101',
  '!': '1110101110101110111',
  '/': '1110101011101',
  '(': '111010111011101',
  ')': '1110101110111010111',
  '&': '10111010101',
  ':': '11101110111010101',
  ';': '11101011101011101',
  '=': '1110101010111',
  '+': '1011101011101',
  '-': '111010101010111',
  '_': '10101110111010111',
  '"': '101110101011101',
  '$': '10101011101010111',
  '@': '10111011101011101',
  ' ': '0'}
