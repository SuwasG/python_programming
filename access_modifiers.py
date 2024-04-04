# public -> all the members in python class are public by default and they can be access from anywhere.

# private -> a double underscore '__' makes the variable private as well as secure.
# private member can be accessible within the class only. (wallet)

# protected -> a underscore '_' makes the variable protected.
# protected member can also be accessed from the child class.

class AccessTest:
    def __init__(self, a,b,c):
        self.a=a #public
        self.__b=b #private
        self._c=c #protected
    
    def display(self):
        print("display from function inside class: ")
        print("a= ", self.a)
        print("b= ", self.__b)
        print("c= ", self._c)

x = AccessTest(10,20,30)
print('x=',x.a)
# print('x= ',x.__b)
# print('x= ',x.b)

print('x=', x._c)

x.display()