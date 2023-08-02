# issubclass() with Multiple Inheritance
class A:
   pass

class B:
   pass

class C(A, B):
   pass

print(issubclass(C, (A, B)))