#Functions -
# A.Define a Python function named greet_user that takes a user's name as a parameter and prints a greeting message.Call the function to greet the user by their name.
# def greet_user(name):
#     print("Hello", name)
    
# greet_user("Eldar")


#B.Write a  function named calculate_area that takes the radius of a circle as a parameter and returns the area of the circle.Print the area of a circle with radius 5 using this function.
# from math import pi
# def calculate_area():
#     r = float(input("Input the radius of the circle: "))
#     area = pi*r**5
#     print("The area of the circle with radius" + str(r) +  "is:" + str(area))

# calculate_area()   


#C.Create a function named calculate_total_cost that takes the price and quantity of an item as parameters and returns the total cost.Print the total cost for an item with a price of $10 and a quantity of 3 using this function.
# def calculate_total_cost(esya):
#     a = "10$"
#     count = 3
#     esya = "book"
#     print(f"The price of this {esya} is {a} and there are {count} copies")
    
# calculate_total_cost(esya= "book")



#D.Write a function named 'hello' that prints "Hello world". Call this function two times.
# def hello_word ():
#     for x in range(2):
#      x = "HELLO world"
#      print(x)

# hello_word()     



#Quiz-
#1.What is a function in Python?
# a) A named sequence of statements that can be reused.


#2.How do you define a function in Python?
#a)Using the def keyword followed by the function name and parameters.


#3.What is the purpose of parameters in a Python function?
#b) Parameters spesifcy the input values that the function expects.


#4.What is a return statement in a Python function?
#a)It exits the function and returns a value to the calling code.


#5.How can you call a function in Python?
#a)Using the call keyword followed by the function name and arguments.

#6.What is the difference between parameters and arguments in a Python function? 
#c)Parameters are the values specified in the function definition, and arguments 



#7.Write a Python function named add_numbers that takes two parameters a and b and returns their sum.
#c) def add_numbers(a,b):
#  return a +b


#8.Write a Python function named is_even that takes a single parameter num and returns True if the number is even and False otherwise.
#a)def is_even(num):
#  return num %2 ==0


#9.Write a Python function named greet that takes a single parameter name and prints a greeting message.
#a) def greet(name):
#    print("Hello, " + name + "!")


#10.Write a Python function named calculate_average that takes a list of numbers and returns their average.
#a) def calculate_average(numbers):
# return sum(numbers) / len(numbers)


#11.Write a Python function named calculate_power that takes two parameters base and exponent and returns the result of base raised to the power of exponent.
#d) def calculate_power(base, exponent):
#   return base^exponent


#12.Consider the following Python program:
# def print_greeting():
#     print("Hello, world!")
    
# print_greeting()
# What will this program print?
# a) Hello, world!


#13.Consider the following Python program:
# def print_numbers():
#     print(1)
#     print(2)
#     print(3)

# print_numbers()

#What will this program print?
#a)
#1
#2
#3


#14.Consider the following Python program:
# def print_multiple_messages():
#     print("Hello!")
#     print("How are you?")
#     print("Goodbye!")
    
# print_multiple_messages()
#  What will this program print?
#a)
# Hello!
# How are you?
# Goodbye!


#15.Consider the following Python program:
# def print_values():
#     print("Value 1")
#     print("Value 2")
#     print("Value 3")

# print_values()
# What will this program print?
# a)
# Value 1
# Value 2
# Value 3


#16.Consider the following Python program:
# def print_repeated_message():
#     for _ in range(3):
#         print("This is a repeated message.")

# print_repeated_message()

# What will this program print?
# a)
# This is a repeated message.
# This is a repeated message.
# This is a repeated message.


#17.What is the purpose of the return keyword in a Python function?
#a) To exit the function and return to the calling code.


#18.What happens if a function in Python does not contain a return statement?
# b)The function automatically returns None if there is no return statement.


#19. What does the return statement without a value return in Python?
# c) It returns None.

#20. What is the data type of the value that can be returned by a Python function?
#c) The data type is determined by the return statement.


#21.Consider the following function:
# def greet():
#         print("Hello, world!")

# result = greet()
#What will be the value of result after calling greet()?
#b) Hello, world!


#22.Can a Python function have both a return statement and print statements inside it?
# a)Yes



#Functions- 2-ci Hisse
#A.Create a function named add_numbers that takes two parameters, a and b, and returns their sum. Test the function with values 10 and 15.
# def add_number(a,b):
#     return a+b

# res = add_number(10,15)
# print(res)


#B. Create a function named calculate_area that calculates the area of a rectangle. 
# Add a docstring explaining what the function does and use type annotations for parameters 
# and the return value.
# def calculate_area_rectangle():
#     a = int(input("Please enter width \n"))
#     b = int(input("Please enter length \n "))
#     return a*b

# res = calculate_area_rectangle()
# print(res)


#C.Write a function that takes a string as a parameter and returns the count of vowels (a,e,i,o,u) in the string.
# def vowel_count(str):
#     count = 0
#     vowel = "a,e,i,o,u"
#     for alphabet in str:
#         if alphabet in vowel:
#             count = count +1
#     print(count)
    
# str = "GeeksforGeeks"
# vowel_count(str)



#D. Write a function that calculates the factorial of a given number n using a for loop.
# def calculate_area_factorial():
#     n = int(input("Please enter your factorial"))
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact *i
#         print("The n factorial is:", end="")
#         print(fact)
        
# calculate_area_factorial()


#E.Write a function that takes a string as a parameter and returns the reverse of the string . Using a for loop to iterate through the characters in the string.
# def word_palindrome(word):
#      return word == word[::-1]
 
# word = "malayalam"
# ans = word_palindrome(word)
# if ans:
#     print("True")
# else:
#     print("False")



#F.Write a function that takes  a string as a parameter and returns the reverse of the string. Use a for loop to iterate through the characters in the string.
# def reverse(s):
#     s = "Hello World"[::-1]
#     print(s)
    
# reverse("Hello World")


#G.Write a function that takes a number as a parameter and prints whether it's positive,negative,or zero using if-elif-else statements.
# def positive_negative_number(num):
#     num = int(input("Please enter your integer: "))
#     if num <0:
#         print("Negative number", num)
#     elif num>0:
#         print("Positive number", num)
#     else:
#         print("Invalid input")

# positive_negative_number(num= 20)



#H.Write a function that takes a list of boolean values as a parameter and returns the count of True and False values in the list. Use a for loop and if statements.
# def boolean():
#     for boolean in range(3):
#         bool = [True, True,True]
#         count = 3
#         if count in bool:
#             print("True",True)
#         else:
#             print("False")

# boolean()


#I.Write a function that checks if a given number is a prime number.Return True if it's prime, and False if it's not.Use for loop conditionals.
# from math import sqrt
# def prime_number(number, itr):
#     if itr == 1 or itr ==2:
#         return True
#     if number % itr == 0:
#         return False
#     if prime_number(number, itr -1) == False:
#         return False
    
# num = 13
# itr = int(sqrt(num)+1) 
# print(prime_number(num, itr))



#J. Write a function that takes a list of numbers as a parameter and returns the largest number in the 
# list. Use an if statement to track the largest number.
# def number_list(third,second):
#     number = [10,20,30,40,50,60,70,80,90,100]
#     third = int(input("Please enter third number"))
#     second = int(input("Please enter second number"))
#     if third >second:
#         print("Third number is the biggest")
#     else:
#         print("Second number is the biggest")

# number_list(90,100)


#K.Write a program that calculates the sum of all even numbers from 1 to a given number n.Use a for loop and an if statement.

# def even_sum(number):
#     total = 0
#     for i in range(12):
#         if i%2 == 0:
#             total += i 
#             print(f"{i} is an even number") 
#             print(total)
#         else:
#             print(f"{i} is an odd number")
#             total +=1
            
# even_sum(20)



#L. Write a program that prints numbers from 1 to 10. For multiples of 3, print "Fizz" instead of the 
# number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# def buz_fiz():
#     for fizzbuzz in range(51):
#         if fizzbuzz % 3 == 0 and fizzbuzz % 5 ==0:
#             print("fizzbuzz")
#             continue
#         elif fizzbuzz % 3 ==0:
#             print("fizz")
#             continue
#         elif fizzbuzz %5 == 0:
#             print("buzz")
#             continue
#         print(fizzbuzz)
        
# buz_fiz()



#Quiz.
#1.What is a function in Python?
#b) A block of reusable code


#2.How do you define a function in Python?
#a)def function_name()


#3.What is the purpose of a return statement in a function?
#c)To return a value from the function


#4.Can a Python function return multiple values?
#a)Yes



#5. What is a docstring in Python?
#c)A comment used for explaining the purpose and usage of a function, class or module



#6.How do you write a docstring in a Python function?
#a)Using triple single-quotes or triple double-quotes at the beginning of the function



#7.What is the purpose of type annotations in Python?
#c)To provide hints about the expected types of arguments and return values



#8.How do you add type annotations to a function in Python?
#b)By writing the types as comments next to the variables


#9.What is a type hint in Python?
#b)A suggestion for the expected type of a variable or expression



#10. What is the benefit of using type hints in Python?
#b)It makes the code more readable and self-explanatory


#11. How do you specify the return type of a function in a type hint?
#a)By using -> followed by the return type


#12.What is the purpose of using type annotations for function parameters and return values?
#c)To make the code more understandable and maintainable


#13.What does the following Python code snippet do?
# def greet(name):
#     print(f"Hello, {name}!")
    
# greet("Alice")
#a)Defines a function to greet a person by name


#14.What is the primary purpose of the following Python function?
# def calculate_average(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     return total/count
#c)To calculate the average of a list of numbers
    


#15. What is the output of the following Python code snippet?
# def is_even(num):
#     return num %2 ==0
# print(is_even(4))

#a)True



#16.How do you call the function is_even from question 15 to check if the number 7 is even?
#a)is_even(7)


#17. What does the following Python code snippet do?
# def print_numbers(n):
#         for i in range(n):
#             print(i)
            
# print_numbers(5)

#a)Prints the numbers 0 to 4


# #18. What does the following Python code snippet do?
# def absolite_value(num):
#     if num >=0:
#         return num
#     else:
#         return - num
    
# result = absolite_value(-5)


#b)Calculates the absolute value of a number


#19.What is the output of the following Python code snippet?
# def greet(time):
#         if time < 12:
#             return "Good morning!"
#         elif time < 17:
#             return "Good afternoon!"
#         else:
#             return "Good evening!"

# print(greet(10))
#a)Good morning!



#20. What does the following Python code snippet do?
# def square(num):
#         return num ** 2

# numbers = [1, 2, 3, 4]
# squared_numbers = [square(num) for num in numbers]
#a)Doubles each number in the list numbers


#21.What is the purpose of using functions with loops in Python?
#b)To modularize code and avoid repetition


#22. What is the purpose of using functions with if statements in Python?
#a)To define the if statement's condition


# Zip(Parallel Iteration) & Enumarate(Counter)-
# A.Write a program that takes a list and uses the enumarate method to print each element in the list along with its index.Use a suitable formatting for the output.
# ls = ["Apple", "Book", "Computer", "eat"]
# y = enumerate(ls)
# print(list(y))


#B.Parallelly iterate over the following collections and print the corresponding pair values:
# students = ["Namig", "Zaur", "Murad", "Aysel"]
# gifts = ["Book", "Phone", "Car Model", "Bag"]
# zipped = list(zip(students, gifts))
# print(zipped)


#C.Iterate over sequence of fruits and print and print the order of each fruit:
# fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
# x = enumerate(list(fruits))
# print(list(enumerate(x)))


#D.Write a program that takes two lists of equal lengths and uses the zip method to create a list of tuples, where each tuple contains elements from both lists at the corresponding index.Print the resulting list of tuples.
# name = ["Eldar", "Yusif", "Kenan"]
# surname = ["Eliyev", "Hesenli", "Eliyev"]
# x = zip(name,surname)
# s = enumerate(name)
# a = enumerate(surname)
# print(tuple(x))
# print(list(enumerate(name)))
# print(list(enumerate(surname)))




#Data & Time-
#A.Write a program that prints 'Running...' each 1.5 seconds.The program should be terminated after 5 executions of the print statement.
# import time
# x = time.sleep(1.5)
# for x in range(6):
#     print(x, "Running")


#B. Write a program that uses the datetime module to display the current date and 
# time in the format "YYYY-MM-DD HH:MM:SS". Print this information to the console.
# import datetime
# now = datetime.datetime.now()
# print("Current date and time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))



#C.Write a program that takes a birthdate (year, month, day) and uses the datetime 
# module to calculate the age in years.
# from datetime import date
# date_of_birth = int(input("In which year you took bith: "))
# today_date = date.today().strftime("%Y")
# print("Your currect age is:", int(today_date)- date_of_birth)


#D.Write a program calculate_elapsed_time(start_time, end_time) that takes two 
# datetime objects representing a start time and an end time. Calculate and return 
# the elapsed time in hours, minutes, and seconds
# import time
# start_time = time.time()
# elapsed_time = time.time() - start_time
# print(elapsed_time)



#E.Write a program that takes a year and a month (1-12) as arguments. Use the calendar 
# module to determine and return the number of days in that month.
# import calendar
# import datetime
# year = datetime.datetime.now().year
# month = datetime.datetime.now().month
# print(calendar.month(year, month))



#F.Write a program that takes a birthdate (as a datetime object) and calculates the time 
# remaining until the next birthday in days, hours, and minutes. Make it in live-clock style.
# from datetime import datetime
# today = datetime(2024,7,10)
# birthday = datetime(2005,12,2)
# difference = birthday - today
# print(str(difference) + "days until your birthday")
# print(str(difference.total_seconds()/ 60)+ "minutes until your birthday" )
# print(str(difference.total_seconds()) + " seconds until your birthday")


#G.Write a program that uses the time module to display the current time. However, 
# add a delay of 5 seconds using time.sleep(5) before displaying the time.
# from datetime import datetime
# import time
# time_sleep = time.sleep
# x = datetime.now()
# print(x, time_sleep)



#H. Write a program that acts as a countdown timer. Prompt the user to enter a time 
# in seconds. Use time.sleep() to create a countdown from the specified time, displaying the 
# remaining seconds at each interval of 1 second.
# import time
# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02} : {minutes:02} : {seconds:02}")
#     time.sleep(1)
    
#     print("Time'S UP!")



#I. Write a program that displays the current time every minute. Use a loop and time.sleep() 
# to achieve this. The program should display the time at each minute interval.
# import time
# x = time.sleep(8)
# a = "Python Development"
# print(x, a)



#J. Write a program that displays a random message every 2 to 5 seconds. Use the random 
# module to select a random message from a predefined list and display it to the
# import random
# import time
# programming_language = ["Python", "C#", "Java", "JavaScript", "Htmll"] 
# def print_random_word(): 
#     while True: 
#         word = random.choice(programming_language) 
#         print(f"Random word: {word}") 
#         time.sleep(2)
        
#         new_word = input("Type a new word (or press Enter to keep the same): ") 
#         if new_word: 
#             programming_language.append(new_word)
            
# print_random_word()
        
        
        
 #K.  Write a program in style of "Squid Game". First, create a list of ten random numbers.
# Then, every 10 seconds remove (kill) the smallest value from the list.
# import time
# import random
# a = time.sleep(10)
# number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# b = random.choice(number_list)
# c = min(number_list)
# print(number_list,b, c )



#-Chat GPT's Homework-
#1.Write a program that uses the zip method to create a new list of tuples,
# where each tuple contains elements from both lists at the corresponding 
# index.
# my_tuple = ("Eldar", "Eliyev")
# favorite_color =("black", "blue")
# o = enumerate(my_tuple )
# s = enumerate(favorite_color)
# x = zip(my_tuple, favorite_color)
# print(tuple(x)) 



#2.Write a program that takes two lists, keys and values and uses the zip 
# method to create a dictionary where the elements from the keys list are the 
# keys and the elements from the values list are the corresponding values. 
# inputDict = {'Hello':1, 'tutorialspoint':2, 'python':3, 'codes':3}
# inputList = [10, 20, 30, 40]
# zippedResult = zip(inputDict.items(), inputList)
# print("Combining input dictionary and list together:")
# print(list(zippedResult))



#3.Write a program that takes an iterable and an optional starting index 
# (default is 0). Implement the functionality of enumerate using a loop, and 
# return a list of tuples where each tuple contains the index (starting from 
# the provided start) and the corresponding element from the iterable.
# my_list = ["Development", "Jed Academy", "apple", "samsung"]
# print(list(enumerate(my_list)))


#4.Explain the difference between the time() method and the sleep() method 
# in the time module. Provide use cases for each.
# Time metodu deqiqeleri gosderir . time sleep istediyimiz saniyelerde proqrami gecikdire bilerik. Numunen:
# import time
# a = time.time()
# b = time.sleep(10)
# print(a, b)


#5.Describe the purpose and functionality of the strftime() method in the 
# datetime module. Provide an example of how to use it.
# from datetime import datetime
# now = datetime.now()
# year = now.strftime("%Y")
# print("year:", year)
# month = now.strftime("%m")
# print("month:", month)
# day = now.strftime("%d")
# print("day:", day)
# time = now.strftime("%H: %M: %S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:", date_time)



#6.Explain the significance of the epoch time (January 1, 1970) and how it's 
# related to the time() method in the time module.
# import datetime
# today = datetime.date(2024, 7, 10) #Today's date
# past_date = datetime.date(1970, 1, 1) #Jan 1 1970
# print ((today - past_date).days)



#7. What is the purpose of the timedelta class in the datetime module? Provide 
# an example use case where timedelta can be helpful.
# from datetime import datetime, timedelta
# date_time = datetime.now()
# time_diff = timedelta(
#     days=2,
#     hours=3,
#     minutes=15
# )
# req_date_time = date_time + time_diff
# print(req_date_time)



#Quiz.
#1.The datetime module in Python provides a class for manipulating dates and times.What is the name of this class?
#a)Datetime


#2.Which method in the datetime module returns the current date and time?
#b)now()


#3.In the strftime method , what does %Y represent in the formatting string?
#b) Year(e.g.,2023)


#4.Which module in Python provides functionality to work with time-related 
# operations such as measuring time intervals, and converting between different 
# time representations?
#a)time


#5.Which method from the time module returns the current time in seconds since 
# the epoch (January 1, 1970)?
#a)time()


#6.In the time module, which method pauses the program's execution for the specified 
# number of seconds?
#a)sleep()

#7.Which method of the datetime class in the datetime module returns a for matted string 
# representing the date and time?
#b)strftime()


#8.In the datetime module, what does the timedelta class represent?
#a)A duration expressing the difference between two date or time instances


#9.Which method of the timedelta class allows you to extract the number of days?
#a)days()


#10.To get the current date and time, which method would you use in the datetime module?
#a)datetime.now()


#11. In the strftime method, what does %d represent in the formatting string?
#c)Day of the month(01-31)


#12.In the strftime method, what does %H represent in the formatting string?
#c)Hour(00-23)


#13.In the strftime method, what does %M represent in the formatting string?
#c)Minute(00-59)

#14.Consider the following Python code snippet:
# import time
# start_time = time.time()
# time.sleep(3)
# end_time = time.time()
# print(f"Execution took {end_time-start_time} seconds")
#What is the purpose of this code,and what will be the output when it is executed?
#a)This code measures the execution time of the time.sleep(3) statement
 