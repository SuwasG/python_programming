# Assignment operator:  Assignment operator is used to assign the value to the variable.

#  = -> Value assign.
# += -> eg: x+=y is same as x=x+y
# -= -> eg: x-=y is same as x=x-y
# *= -> eg: x*=y is same as x=x*y
# /= -> eg: x/=y is same as x=x/y
# **= -> eg: x**=y is same as x=x**y
# %= -> eg: x%=y is same as x=x%y
# //= -> eg: x//=y is same as x=x//y

# &= Bitwise AND assignment
# |= Bitwise OR assignment
# ^= Bitwise XOR assignment
# >>= Bitwise Right shift assignment
# <<= Bitwise Left shift assignment.




x=5
y=10

x+=y
print(x)

x-=4
print(x)

x**=2
print(x)

x/=121
print(x)

x//=0.3
print(x)

x%=2
print(x)

# Bitwise AND assignment
a=3  # 11
b=5  #101

a&=b # a = a & b
print(a)

# Bitwise OR assignment
a=3
b=5
a |=b
print(a) # 7 or 5?

# Bitwise XOR assignment
a=3
b=5
a^=b
print(a)  # 0 or 6?

# Bitwise right shift and assign
a=3
b=5
a>>=b
print(a) 

# Bitwise Left shift and assign
a=3
b=5
a<<=b
print(a)