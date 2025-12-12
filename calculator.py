class Calculator:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
    
    def multiply(self, a,b):
        return a*b

calc = Calculator()
print(calc.add(1,2))
print(calc.sub(2,1))
print(calc.multiply(1,2))

