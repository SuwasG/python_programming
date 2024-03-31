class A:
    def say(self):
        print("A", end=' ')

class B(A):
    def say(self):
        super().say()
        print("B", end=' ')

class C(A):
    def say(self):
        super().say()
        print("C", end=' ')

class D(B,C):
    def say(self):
        super().say()
        print("D", end=' ')

d = D()
d.say()
