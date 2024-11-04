# class A:         #(A, object)
#     def method(self):
#         print("A method")

# class B(A):      #(B, A, object)
#     def method(self):
#         print("B method")

# class C(A):      #(C, A, object)
#     def method(self):
#         print("C method")

# class D(B, C):   #(D, B, C, A, object)
#     pass

# # Task: Calculate the MRO for class D manually and confirm it by printing D.__mro__.
# print(D.__mro__)


#2
# class A:            #(A, object)
#     def method(self):
#         print("A method")

# class B(A):         #(B, A, object)
#     pass

# class C(A):         #(C, A, object)
#     def method(self):
#         print("C method")

# class D(B, C):      #(D, B, C, A, object)
#     pass

# # Task: Calculate the MRO for class D and confirm by printing D.__mro__.
# print(D.__mro__)

#3

# class X:        #(X, object)
#     def method(self):
#         print("X method")

# class Y(X):     #(Y, X, object)
#     pass

# class Z(X):     #(Z, X, object)
#     def method(self):
#         print("Z method")

# class W(Y, Z):  #(W, Y, Z, X, object)
#     pass

# # Task: Calculate the MRO for class W manually and check it using W.__mro__.
# print(W.__mro__)
# p = W()
# print(p.method())

#4

# class Base:             #(Base, Object)
#     def action(self):
#         print("Base action")

# class MixinA:           #(MixinA, Object)
#     def action(self):
#         print("MixinA action")

# class MixinB:           #(MixinB, Object)
#     def action(self):
#         print("MixinB action")

# class FinalClass(Base, MixinA, MixinB):    #(FinalClass, Base, MixinA, MixinB, Object)
#     pass

# # Task: Manually determine the MRO for FinalClass, then check by printing FinalClass.__mro__.
# print()

import numpy as np

arr = np.zeros(10)
print(arr)

