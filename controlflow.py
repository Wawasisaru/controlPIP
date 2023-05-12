# Write a Python program that takes a list of strings 
# as input and outputs the number of times each string appears in the list, 
# using a dictionary and conditional statements.
# words_string = ['pen', 'heals', 'jacket', 'pen', 'bag', 'bag', 'shoe']
# counts = {}
# for x in words_string:
#     if x in counts:
#         counts[x] += 1
#     else:
#         counts[x] = 1
# for x, count in counts.items():
#     print(x, count)
def median_num(numbers):
    length=len(numbers.sort())
    if(length%2 == 0):
        numbers((length)/2)
    else:
        return numbers[(length-1)/2]
    numbers = [17, 10, 6, 13, 4,8, 19]
    print(median_num(numbers))

    
    

# Write a Python program that takes a list of numbers as 
# input and outputs the median of the numbers 


numbers = [7, 10, 6, 3, 4,8, 19]
num_sorted = sorted(numbers)
length = len(numbers)
if length % 2 == 0:
    median = (num_sorted[length//2] + num_sorted[length//2-1]) 
else:
    median = num_sorted[length//2]
print (f"The median is {median}")
# 


# Write a Python program that takes a list of numbers as 
# input and outputs the second largest number in the list using 
# conditional statements and a for loop.
def numbers(numb):
    count_1= numb[0]
    count_2=numb[0]
    for num in numb:
        if num > count_1:
            count_2 = count_1
            count_1 = num
        elif num > count_2 and num != count_1:
            count_2 = num
    return count_2
input_list = [3, 5, 1, 7, 2, 8, 4]
output = numbers(input_list)
print(output)
# Write a Python program that takes a year as input and 
# determines if it is a leap year.
# Python program to check if year is a leap year or n
def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
input_year = 2015
output = leap_year(input_year)
print(output)

# Write a Python program that takes a string as input and 
# checks if it is a palindrome (reads the same forwards and backwards), 
# ignoring spaces and punctuation.
#  def string_check_palindriome(string):