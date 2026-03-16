class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def  multiply(a, b):
        return a * b
    
print(MathUtils.add(5,3))
print(MathUtils.multiply(5,3))

math = MathUtils()

print(math.add(5, 4))
print(math.multiply(5, 4))
