#importing various modules
import sys
import random
import os


#function definition uses the "def" keyword
def myFunc(param):
    return param

#global variables put _G when making it global
numba_G = 5

def foo(num):
    #use global keyword to modify the global "numba"
    global numba_G
    numba_G = num

print(numba_G)
foo(10)
print(numba_G)

#classes the __init__ means initialization
#the self keyword is like the this keyword
#for default constructor your need to put data="default" like this
class TestClass:
        def __init__(self, data="default", more="default"):
            self.data = data
            self.more = more


test_obj = TestClass("This is the data","more data here")

print(test_obj.data+" "+test_obj.more)

test_obj2 = TestClass()

print(test_obj2.data+" "+test_obj2.more)
