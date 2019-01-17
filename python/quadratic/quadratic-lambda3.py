#file 3 : quadratic_function
def quadratic_function(a,b,c):
    return lambda x: a*(x**2) + b*x + c

a1 = quadratic_function(1,2,1)
print(" a1 ", a1(0))
print("Input a,b and c from a quadratic_function in the form of ")
print("x = ax^2 + bx + c")
# we have a problem here
a = input("Input a ")
b = input("input b ")
c = input("Input c ")
x = int("Input x")
a2 = quadratic_function(a,b,c)
fx = a2(1)
print("f(x) = ", fx)
# end of the quadratic.py files
