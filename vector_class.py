class Vector():
    def __init__(self,pos):
        self.pos = pos
    def add(self, vect):
        new_pos = []
        if len(self.pos) != len(vect.pos): raise Exception ("Vectors not same length")
        try:
            for i in range(len(self.pos)):
                new_pos.append(self.pos[i]+vect.pos[i])
            return Vector(new_pos)
        except Exception as e: print(e)

    def subtract(self, vect):
        new_pos = []
        if len(self.pos) != len(vect.pos): raise Exception  ("Vectors not same length")
        try:
            for i in range(len(self.pos)):
                new_pos.append(self.pos[i]-vect.pos[i])
            return Vector(new_pos)
        except: raise Exception

    def dot(self, vect):
        dp = 0
        if len(self.pos) != len(vect.pos): raise Exception  ("Vectors not same length")
        try:
            for i in range(len(self.pos)):
                dp += self.pos[i]*vect.pos[i]
            return dp
        except: raise Exception

    def norm(self):
        norm_val = 0
        for i in range(len(self.pos)):
            norm_val += self.pos[i]**2
        norm_val = norm_val**0.5
        return norm_val

    def __str__(self):
        return str(tuple(self.pos)).replace(" ", "")

    def equals(self,vect1):
        if self.pos == vect1.pos:
            return True
        else: return False
