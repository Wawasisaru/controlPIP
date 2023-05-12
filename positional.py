# Write a function that takes an unknown number of arguments and returns their sum.

def addition(*args):
    return(args)
args = (23,45)
print(addition)
 
# Write a function that takes two arguments, the first being a string and 
# the second being an unknown number of integers. The function should 
# return a new string where the integers have been added to the original string.
def add_string(string, *args):
    word = string
    for num in args:
        word += str(num)
        return word
    args = "saru","wawasi"
    print(add_string)

# Write a function that takes an unknown number of keyword arguments and
# returns a dictionary where the keys are the argument names and the values are the argument values.

# Write a function that takes a function and an unknown number of arguments,
# and returns the result of calling the function with the arguments.
def numbers_function(func,*args):
    return func(*args)
args=(20,21)
print(numbers_function)

# Write a function that takes a list of integers and an unknown number
# of keyword arguments. The function should return a new list where each 
# integer in the original list has been multiplied by the value of the corresponding keyword argument
def multiply_list(numbers,**kwargs):
    numbs = []
    for i in numbers:
        if i < len(kwargs):
            numbs.append()
        else:
            numbs.append()
            kwargs=(34,78)
            print(multiply_list)
# Write a function that takes a list of integers and an unknown number
# of additional integers as arguments. The function should return the 
# index of the first occurrence of the sum of the list and the additional integers
# def find_sum_index(numbers, *args):
#     total = sum(numbers) + sum(args)
#     return numbers.index(total)
def find_first_sum(numbers,*args):
    total = sum(numbers) + sum(args)
    return numbers.index(total)

# Write a function that takes an unknown number of keyword arguments, 
# each with a string value. The function should concatenate all the strings and 
# return the resulting string.
def concatenate_string(**kwargs):
    return ''.join(kwargs)
kwargs= "saru","fruits"
