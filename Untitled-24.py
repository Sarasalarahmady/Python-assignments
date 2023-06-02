class Kasr:
    def __int__(self , soorat  , makhraj ) :
        self.soorat = soorat
        self.makhraj = makhraj

    def show(self):
        print(self.soorat, "/" ,self.makhraj)

    def sum (self , another):
        result = Kasr()
        result.soorat = (self.soorat * another.makhraj) + (self.makhraj * another.soorat)
        result.makhraj = (self.makhraj * another.makhraj)
        return result
    
    def mul(self , another):
        result = Kasr()
        result.soorat = self.soorat * another.soorat
        result.makhraj = self.makhraj * another.makhraj
        return result
    
    def sub(self , another):
        result = Kasr()
        result.soorat = (self.soorat * another.makhraj) - (self.makhraj * another.soorat)
        result.makhraj = self.makhraj * another.makhraj
        return result
    
    def div(self , another):
        result = Kasr
        result.soorat = self.soorat * another.makhraj
        result.makhraj = self.makhraj * another.soorat
        return result

s1 = Kasr(6 , 7)
s2 = Kasr(8 , 2)
r = s1.add(s2)
r.show()

        