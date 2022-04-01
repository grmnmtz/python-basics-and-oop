class Math:
    
    # Static methods don't have access to any instance
    # and they don't change anything.

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def multiply(x,y):
        return x * y

print(Math.add5(10)) # 15
print(Math.add10(10)) # 20
print(Math.multiply(10, 4)) # 40



    
