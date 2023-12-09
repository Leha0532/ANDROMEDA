def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multipy(a,b):
    return a*b
def divide(a,b):
    return a/b
a = int(input())
znak = input()
b = int(input())
if znak == "+":
    print(plus(a,b))
if znak == "-":
    print(minus(a,b))
if znak == "*":
    print(multipy(a,b))
if znak == "/":
    print(divide(a,b))