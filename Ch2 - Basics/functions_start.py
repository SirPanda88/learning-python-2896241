#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("i am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value
def cube(x):
    return x*x*x

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# TODO: function with variable number of arguments
def multi_add(arg1=0, *args):
    result = arg1
    for x in args:
        result += x
    return result 


print(multi_add(4,5,10,4))