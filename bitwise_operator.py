
# Bitwise Operators:
'''
-> Operators are used to perform operations on values and variables.
-> These are the Special Symbols that carry out Arithmetic and Logical computations.

-> Bitwise Operators are used to perform bitwise calculations on integers.
-> The integers are first converted into Binary and then operations are performed on each bit or corresponding
    pair of bits.
-> The result is then returned in decimal format.
NOTE: Python bitwise operators work only on INTEGERS.

Operator  ->  Name  ->   Description   -> Syntax
& -> Bitwise AND -> Result bit 1, if both operand bits are 1, otherwise results bit 0.  -> a&b

'''
a=10  # 1010 (binary)
b=4   # 0100 (binary)

x = 6 # 0110 (binary)
y = 7 # 0111 (binary)
# Bitwise AND Operator:
'''
a & b = 1010
        &
        0100
      = 0000
      = 0 (decimal)

x & y = 110 
        &
        111
       = 110 (binary)
       = 1*2^2 + 1*2^1 + 0*2^0
       = 4 + 2 + 0
       = 6
'''
print(f"a&b: {a&b}")
print(f"x&y: {x&y}")


# Bitwise OR operator -> Returns 1 if either of the bits is 1 else 0.
'''
a | b = 1010
         |  
        0100
       = 1110
       = 1*2^3 + 1*2^2 + 1*2^1 + 0*2^0
       = 8 +  4 + 2 + 0
       = 14 

x | y = 110 
         |
        111
      = 111
      = 1*2^2 + 1*2^1 + 1*2^0
      = 4 + 2 + 1
      = 7

'''
print(f"a|b: {a|b}")
print(f"x|y: {x|y}")


# Bitwise NOT Operator -> Returns one's complement of the number. 1->0, 0-> 1
'''
a  = 1010 
~a = 0101 


NOTE: The bitwise NOT operation essentially calculates -(y+1) for any integer y.
binary representation of 7 in 32-bit system: 00000000 00000000 00000000 00000111
Applying bitwise NOT:                        11111111 11111111 11111111 11111000

Interpreting the Result:                      00000000 00000000 00000000 00000111
Add 1:                                       + 1
                                             = 00000000 00000000 00000000 00001000  
conversion to decimal:                       = 8(decimal)
Negative Sign: Since we started with a binary number representing a negative value (indicated by the leading 1 in the binary), the decimal value is -8.

The bitwise NOT operation flips all bits. For positive integers, this operation always yields a binary result that starts with 1, which signifies a negative number in two's complement representation.

Since all bits are flipped, the positive sequence that represented the original number is transformed into the negative sequence representing its two's complement, hence the negative result.
'''
print(f"~a: {~a}")

print("-7: ", ~(-7))

print(f"~b: {~b}")

print( f"~(a&b): {~(a&b)}")
print( f"~(a|b): {~(a|b)}")

# Bitwise XOR operator -> Return 1 if one of the bits is 1 and the other is 0 else returns false.
'''
a ^ b =  1010
         ^  
         0100
       = 1110
       = 1*2^3 + 1*2^2 + 1*2^1 + 0*2^0
       = 8 +  4 + 2 + 0
       = 14 

x ^ y = 110 
         ^
        111
      = 001
      = 1*2^0
      =  1
'''
print(f"a^b: {a^b}")
print(f"x^y: {x^y}")


print("-------Shift Operators --------")
'''
-> Shift operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by two respectively.
-> They can be used when we have to multiply or divide a number by two.
'''

# bitwise right shift : Shifts the bits of the number to the right and fills 0 on voids left(fills 1 in the case of negative numbers) as a result.
# similar effects as dividing the number with some power of two.

# a = 10 = 0000 1010 (binary)
# a >> 1 = 0000 0101 = 5

# a = -10 = 1111 0110 (binary)
# a >> 1 = 1111 1011 = -5

print(f"a >> 1= {a>>1}")
print(f"-10 >> 1= {-10>>1}")
print(f"7 >> 1= {7>>1}") # 0111 -> 0011 -> 1*2^1 + 1*2^0 = 2 + 1 = 3
print(f"-7 >> 1= {-7>>1}")  # 1000+ 1 = 1001 = 100 = 1*2^2 + 0 + 0 = -4 (Apply negative sign as we started with negative number.)



# bitwise left shift:
'''
Shifts the bits of the number to the left and fills 0 on voids right as result.
Similar effect as of multiplying the number with some power of two.

a = 5 = 0000 0101 (binary)
a << 1 = 0000 1010  = 4+0+1+0= 5
a << 2 = 0001 0100  = 16+0+4+0+0= 20


NOTE: The left shift operation 5 << 2 can be mathematically understood as multiplying 5 by 
2^2. (since we are shifting by 2 positions.)
5 * 2^2 = 20
Thus, 5 << 2 results in 20, reflecting the binary operation's nature to multiply the number by two for each shift to the left.

'''
print(f"5<<1 : {5<<1}")
print(f"5<<2 : {5<<2}")


'''
7 = 0111
7 << 2 = 00001 1100 = 1*2^4 + 1*2^3 + 1*2^2 + 0 + 0 = 16 + 8 + 4 =28 = 7 *2^2
7 << 3 = 00011 1000 = 1*2^5 + 1*2^4 + 1*2^3 + 0 + 0 + 0 = 32 + 16 + 8  =56  = 7 * 2^3

'''
print(f"7<<3 : {7<<3}") 


print("--------Bitwise Operator Overloading----------")
'''
-> Operator overloading means giving extended meaning beyond their predefined operational meaning.
-> For eg: operator + is used to add two integers as well as join two strings and merge two lists.
-> It is achievable because the '+' operator is overloaded by int class and str class.
'''

class Overload():
    def __init__(self, value):
        self.value = value
    
    def __and__(self, obj):
        print("AND operator overloaded.")
        if isinstance(obj, Overload):
            return self.value & obj.value 
        else:
            raise ValueError("Must be object of class Overload.")
        
    def __or__(self, obj):
        print("OR operator overloaded.")
        if isinstance(obj, Overload):
            return self.value | obj.value
        else:
            raise ValueError("Must be object of class Overload.")
        
    def __invert__(self):
        print("Invert operator overloaded.")
        return ~self.value
    
    def __xor__(self, obj):
        print("XOR operator overloaded.")
        if isinstance(obj, Overload):
            return self.value ^ obj.value 
        else:
            raise ValueError("Must be object of class Overload.")
        
    def __rshift__(self, obj):
        print("Right Shift operator overloaded.")
        if isinstance(obj, Overload):
            return self.value >> obj.value
        else:
            raise ValueError("Must be object of class Overload.")
        
    def __lshift__(self, obj):
        print("Left Shift operator overloaded.")
        if isinstance(obj, Overload):
            return self.value << obj.value
        else:
            raise ValueError("Must be object of class Overload.")

# driver's code:
if __name__== '__main__':
      p = Overload(10)
      q = Overload(12)
      print(p&q)
      print(p|q)
      print(p^q)
      print(p<<q)
      print(p>>q)
      print(~p)


# + operator for different purposes:
print(1+2)
print("Hello"+"Suwas")

# * operator for different purposes:
print(8*5)
print("Suwas" *5)