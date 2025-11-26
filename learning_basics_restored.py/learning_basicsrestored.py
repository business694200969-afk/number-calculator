
# --- VARIABLE ---

# x = str(3)
# y = int(3)
# z = float(3) 
# print(x)
# print(y)
# print(z)
# 
# 
# x, y, z = "Orange", "Banana", "Cherry"
# print(x, y, z)
# print(x)
# print(y)
# print(z)
# 
# a = b = c = "Orange"
# print(a)
# print(b)
# print(c)
# print(a,b,c)
# 
# fruits = ["Oranges", "Bananas", "Cherries"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
# print(x, y, z)
# 
# fruits = ["Oranges", "Bananas", "Cherries"]
# x, y, z = fruits
# print(x + " " + y + " " + z)
# 
# 
# x = 5   
# y = "a"
# print( x + y) # Gives an error
# 
# x = "awesome"

# --- FUNCTIONS ---

# def myfunction():
#     print("Python is" + " " + x)
# myfunction()
# 
# x = "awesome"
# def myfunction():
#     x = "Fantastic"
#     print("Python is" + " " + x)
#     myfunction()
# 
# print("Python is" + " " + x)
# 
# 
# def myfunc():
#     global x           # Makes it so that x would work even outside the loop as it belongs to everyone not jsut the function
#     x = "Fantastic"
# 
# 
# myfunc()
# print("Python is" + " " + x)
# 
# 
# x = 1j
# print(type(x))
# 
# x = 1
# y = 21451512
# z = -12412
# print(type(x))
# print(type(y))
# print(type(z))
# 
# x = 35e3
# y = 12E4
# z = -87e100
# print(type(x))
# print(type(y))
# print(type(z))
# 
# x = 3+5j
# y = 5j
# z = -5j
# print(type(x))
# print(type(y))
# print(type(z))
# 
# x = 1
# y = 2.2
# z = 1j
# 
# a = float(x)
# b = int(y)
# c = complex(z)
# print(a)
# print(b)
# print(c)
# 
# print(type(a))
# print(type(b))
# print(type(c))
# 

# --- NUMBERS ---

# import random
# print(random.randrange(1,100))
# 
# x = int(1)
# y = int(2.8)
# z = int("3")
# 
# print(x)
# print(y)
# print(z)
# 
# print(type(x))
# print(type(y))
# print(type(z))
# 
# print("It's Alright")
# print("He is Called 'Johnny' ")
# 
# a = """Hi guys my name
# is talha and i am 
# the one and only 'GOAT' """
#print(a)
# 
# a = "Hello world"
# print(a[1]) # Prints 0, 1irst LETTER
# 
# a = "Hello world"
# print(a[0:])
# 

# --- LOOPS ---

# for x in "apple":
#     print(x)
# 
# a = "Hello, world"
# print(len(a))
# 
# text = "The best things in life are free"
# print("free" in text)
# 
# text = "The best things in life are free"

# --- CONDITIONALS ---

# if "free" in text:
#     print("Yes, free is present")
# 
# text = "The best things in life are expensive"
# if "free" not in text:
#     print("Free is not present")
# 
# a = "Hello, World"
# print(a[2:5])
# 
# b = "Hello world"
# print(b[:5])
# 
# c = "Hello world"
# print(c[1:])
# 
# name = "Talha Junaidi"
# first_name = name[0:5]
# last_name = name[6:13]
# fullname = name[:13]
# funky_name = name[0:13:2]
# print(first_name)
# print(last_name)
# print(fullname)
# print(funky_name)
# 
# name = "Bro Code"
# first_name = name[0:3]
# 
# last_name = name[4:]
# 
# fullname = name[0:8]
# 
# funky_name = name[0:8:2] #Start : Stop : Step. The steps prints firstltter and every letter that comes 3rd
# 
# print(first_name)
# 
# print(last_name)
# 
# print(fullname)
# print(funky_name)
# 
# name = "Bro Code"
# # firstname = name[:3]
# # lastname = name[4:]
# funkyname = name[::2] 
# print(funkyname)
# reversed_name = name[::-1]
# 
# print(funkyname)
# print(reversed_name)
# 
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice2 = slice(7,-4)
# slice = slice(7,-4)
# 
# print(website1[slice])
# print(website2[slice2])
# 
# game = "http://fortnite.com"
# slice = slice(7,-4)
# print(game[slice])
# 
# website = "google.com"
# print(website.upper())
# website2 = "WIKIPIDEA.COM"
# print(website2.lower())
# 
# website1 = "  Google.com  "
# print(website1.strip())
# website2 = "  wikipidea.com  "
# print(website2.strip())
# 
# book1 = "The, 48 Laws of, Power"
# print(book1.split())
# 
# book = "Atomic habits"
# print(book.replace("s", " "))
# 
# website_name = "google"
# commercial = ".com"
# website = website_name + commercial
# print(website)
# 
# first_name = "talha"
# last_name = "junaidi"
# fullname = first_name + " " + last_name
# print(fullname)
# 
# age = 16
# text = f"My name is Talha and i am {age} years old"
# print(text)
# 
# book_int = 48
# book_name = f"The books name is {book_int} laws of power"
# print(book_name)
# 
# price = 100
# text = f"The price is {price} dollars"
# print(text)
# 
# price = 150
# text = f"The price is {price:.2f} dollars"
# print(text)
# 
# book = input("Enter name of book you want to purchase")
# bookprice = 25
# book_price = f"The price of {book}  is {bookprice:.2f} dollars"
# print(book_price)
# 
# car = input("Enter name of car you want to purchase")
# car_price = 120000000
# cartobuy = f"The  {car}'s price is {car_price} dollars"
# print(cartobuy)
# 
# txt = f"The books price is {1*20} dollars"
# print(txt)
# 
# txt = "We are the so called \"Vikings\" from the north"
# print(txt)
# 
# name = input("Enter your full name: ")
# result = len(name)
# result = name.find(" ")
# name = input("Enter your full name: ")
# result = name.rfind(" ") #Gives -1 if no spaces are present
# print(result)
# result = name.rfind("q")
# name = name.capitalize()
# name = name.lower()
# result = name.isdigit() #Checks if string is all numbers, returns a boolean
# result = name.isalpha() # Checks if all numbers are alphabets, returns a boolean true if yea false if no
# print(result)
# phonenumber = input("Enter your phone number #: ")
# result = phonenumber.count("-")
# print(result)
# 
# projectname = "I_Love_Learning_Python"
# # result = projectname.count("_")
# result = projectname.replace("_"," ") # Always add to a variable whatever youre doing then print
# print(result)
# 
# 
#Username project. Question:    
#validate user input excersise

# --- COMPREHENSIONS ---

#1. your username cant contain mroe than 12 letters #So, use len, variables and if
#2. ur username cant contain spaces. #Use username.find(" ") == -1
#3. ur username cant contain digits #use username.isdigit() == False
# username = input("Enter username: ")
# result = len(username)
# if result > 12:
#     print("your username cant be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username cannot have spaces")
# elif not username.isdigit()== False:
#     print("Your username cant contain digits")
# else:
#     print (f"Welcome {username}")
# 
# 
# x = 0
# y = False
# z =[]
# print(bool(x))
# print(bool(y))
# print(bool(z))
# 
# def myfunction():
#     return True
# 
# print(myfunction())
# 
# def myfunction():
#     return False
# 
# print(myfunction())
# 
# x = 200
# print(isinstance(x, str))
# 
# a = "a"
# print(isinstance(a, str))
# 
# b = 1j
# print(isinstance(b,complex))
# 
# x = 10 + 2
# y = 10 / 2
# z = 10 * 2
# print(x)
# print(y)
# print(z)
# 
# a = 10 % 3 # Gives remainder
# b = 10 ** 10 #to the power (expotential)
# c = 10 // 3 #Rounds to whole num
# print(a)
# print(b)
# print(c)
# 
# x = 10
# y = 20
# x = x + y
# print(x)
# 
# x = 10
# y = 20
# x += y #x and y will be added and the result will be stored in the left operatent
# print(x)
# 
# y = 50
# z = 20
# y += z
# print(y)
# 
# a = 50
# b = 100
# a += b
# print(a)
# 
# a = 10*10
# b = 50 // 3
# a -= b
# print(a)
# 
# x = 50
# y = 10
# x -= y
# print(x)
# 
# y = 10
# z = 50
# y *= z
# print("The result is", y)
# 
# x = 10
# y = 20
# x *= y
# print("The result is", x)
# 
# x = 50
# y = 10
# x /= y
# print(x)
# 
# a = 150
# y = 50
# a /= y
# print(a)
# 
# x = 25
# y = 3
# x //= y
# print(x)
# 
# a = 50
# b = 3
# a //= b
# print(a)
# 
# a = 26
# b = 6
# a %= b
# print(a)
# 
# x = 100
# y = 20
# x %= y
# print(x)
# 
# x = 10
# y = 2
# x **= y
# print(x)
# 
# 
# thislist = ["apple", "banana", "cherry", "oranges"]
# boolens= [True, False, True, False, True]
# print(boolens)
# print(type(boolens))
# print(len(boolens))
# print(len(thislist))
# print(thislist)
# 
# thislist = list(("apple", "banana", "cherry"))
# print(thislist[0:2])
# print(thislist[0:1])
# print(thislist[:2])
# print(thislist[0:])
# print(thislist[2])
# print(thislist[-3])
# print(thislist[-1])
# 
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1]) #last one dosent get printed
# 
# thislist = ["apple", "banana"]
# if "apple" in thislist:
#     print("yes, apple is in fruits list")
# 
# thislist = ["apple", "banana", "strawberry"]
# # thislist[0] = "cherry" # To replace fully , with del  
# # print(thislist)
# thislist[0:2] = ["cherries", "apricots"]
# print(thislist)
# 
# gamingpc = ["Gpu", "cpu", "case"]
# gamingpc[0:2] = ["motherboard", "ram"]
# print(gamingpc)
# 
# gamingtable = ["mousepad", "keyboard", "mouse"]
# gamingtable[1:3] = ["Monitor"]
# print(gamingtable)
# 
# fruits = ["apple", "banana", "cherry"]

# --- LISTS ---

# # fruits.insert(0, "mangoes")
# # print(fruits)
#  fruits.append("Pinapple")
#  print(fruits)
# fruits.remove("apple")
# fruits.pop(2)
# del fruits[0]
# for i in range (4)
#     print(fruits[0])
# for fruit in fruits:
#     print(fruit)
# i = 0
# while i < len(fruits): # i will firstly be 0(apple) then 1 then 2 and will stop when it reaches 3
#     print(fruits[i]) # we do this so then the output will be first apple banana cherry
#     i += 1 #first i = 0 then i =1 then i = 2 then i =3 . w/out this value of i wouldnt change
# 
# name = input("Enter your name: ")
# while name == "":
#     print("You did not enter your name!")
#     name = input("Enter your name!")
# 
# print(f"Hello {name}")
# cars =["lamborghini", "ferrari", "bmw", "mercedes"]
# for car in cars:
#     print(car)
# 
# fruits.sort()
# print(fruits.index("Pineapple"))
# print(fruits.count("banana"))
# fruits.reverse()
# fruits.clear()
# fruits.insert(0, "Grapes")
# print(fruits)
# 
# 
# 
# 
# gamingpc= ["case", "monitor", "gpu"]
# # gamingpc.append("cpu")
# gamingpc.sort()
# print(gamingpc)
# 
# 
# fruits = ["apple", "banana", "orange", "Strawberry"]
# # print(fruits[::2])
# # print(fruits[::-1])
# print(dir(fruits))
# for fruit in fruits:
#     print(fruit)
# 
#list comprehension IS A CONCICSE WAY TO CREATE LISTS IN PYTHON
#harder method (this is an example of traditional loop to see why list comprehnsion is useful)
# doubles = []
# for x in range (1,11):
#     doubles.append(x * 2)
# 
# print(doubles)
# 
# doubles = [expression for VALUE in iterable if condition] # easier method using list comprehension
# doubles = [x * 2 for x in range (1,11)]
# triples = [y * 3 for y in range (1,11)]
# print(triples)
# 
# quadruples = [x * 4 for x in range (1,101)]
# print(quadruples)
# 
# a = [y * 2 for y in range (1,11)]
# print(a)
# 
# squares = [x ** 2 for x in range(1,11)]
# print(squares)
#[expression for value in iterable if condition]
# 
# newlist = []
# for fruit in fruits:

# --- STRINGS ---

#     newlist.append(fruit.upper())
#     print(newlist)
# 
# fruits1 = ["apple", "banana", "cherry"]
# fruits1 = [fruit.upper() for fruit in fruits]
# print(fruits1)
# 
# #Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# fruits = ["apple", "banana", "cherry", "coconut"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
# 
# fruits = ["apple", "banana", "orange", "coconut"]
# fruits_char = [fruit.upper() for fruit in fruits] #expression for value in iterable if condition
# print(fruits_char)
# 
# fruits = ["apple", "banana", "orange", "coconut"]
# fruit_chards = [fruit[0] for fruit in fruits]
# print(fruit_chards)
# 
# numbers = [1, -2, 3, 4, 5, -6]
# numbers_positive = [number for number in numbers if number >=0]
# print(numbers_positive)
# 
# letters = ["abc", "adc", "bcd", "lcd"]
# a_inletters = [letter for letter in letters if "a" in letter]
# print(a_inletters)
# 
# numbers = [1, 2, -3, -4, -69]
# negative_numbers = [num for num in numbers if num <=0] #expression for value in iterable if condition ..
# print(negative_numbers)
# 
# grades = [69, 40, 20, 50]
# passing_grades = [grade for grade in grades if grade >=50]
# print(passing_grades)
# 
# fruit = ["apple"]
# fruit2 = fruit.copy()
# print(fruit2)
# 
# fruits = ["apple", "banana"]
# fruits2 = list(fruits)
# print(fruits2)
# 
# fruits = ["apple", "banana", "oranges", "cherries"]
# fruits2 = ["coconut", "mangoes"]
# fruits.extend(fruits2)
# print(fruits)
# 
# list1 = ['a', 'b', 'c', 'c']
# list2 = [1, 2, 3, 4]
# list1.append(list2)
# print(list1)
# 
# list = ['a', 'b', 'c', 'd', 'e']
# # # list.reverse()
# list.pop(2)
# print(list)
# 
# set
# fruits = {"apple", "banana", "orange", "coconut", "coconut"}
# # print(len(fruits))
# # print("apple" in fruits)
# print(fruits)
# # print(fruits[0]) No work

# --- SETS ---

# # fruits.add("pineapple")
# # fruits.remove("banana")
# # fruits.pop()
# fruits.clear()
# print(fruits)
# 

# --- TUPLES ---

#tuple()
# fruits = ('apples', 'bananas', 'oranges', 'cherries')
# # print(len(fruits))
# print('apples' in fruits)
# fruits = fruits + (0,)
# print(fruits)
# print(fruits.index("apples"))
# print(fruits.count("oranges"))
# if_a_in_variable = [fruit for fruit in fruits if "a" in fruit]
# print(if_a_in_variable)
# for fruit in fruits:
#     print(fruit)
# 
#dictionaries
# {key:value} ordered and changeable (add/remove )
# capitals = {"USA": "Washington D.C", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow" }
# if print(capitals.get("Japan")): 
#      print("That capital exists")
# 
# else:
#      print("That capital dosent exist")
# print(capitals.get("Russia"))
# print(capitals.get("USA"))
# 
# result = [capital for capital in capitals if "a" in capital.lower()]
# print(result)
# keys = capitals.keys()
# print(keys)
# values = capitals.values()
# print(values)
# values = capitals.values()
# key = capitals.keys()

# --- DICTIONARIES ---

# for value in capitals.values():
#     print(value)
# print(values) 
# print(capitals.get("USA"))
# print(capitals.get("China"))    
# items = capitals.items()
# print(items)
# for values, key in capitals.items():
#     print(f"{key}: {values}")
# print(items)
# if  capitals.get("India")
#     print("That capital exists")
# else:
#     print("That capital dosent exist")
# 
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# print(capitals)
# capitals.pop("China")
# print(capitals)
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "colors": ["Red", "Blue", "Orange"], "interior": True} 
# print(thisdict["year"])
# print(thisdict)
# print(len(thisdict))
# 
# 

# myfamily = {
#     "Child1": "Talha",
#     "Child2": "Taha",
#     "Child3": "Leena"
# }
# print(myfamily)

# x

# thisdict = dict(brand = "Ford", model = "Mustang", Year = 1857)

# print(thisdict)
# 
# cars = dict(car1 = "Ferrari", car2 = "Lamborghini") 
# print(cars)
# cars2 = cars.copy()
# print(cars2)
# for x in cars.keys():
#     print(x)
# # # for x in cars.values():
# #     print(x)
# for x,y in cars.items():
#     print(x,y)
# # cars.update({"color": "Orange"})
# # print(cars)
# # cars.pop("car1")
# cars.popitem() # to remove last key + value
# print(cars)
# change = cars.update({"car2": "Koeinsegg"})
# print(cars)
# 
# x = cars.items() #returns as tuples
# print(x)
# # x = cars.get("car1")
# # y = cars.get("car2")
# z = cars.keys()
# f = cars.values()
# print(z)
# print(f)
# print(x)
# print(y)
# 
# capitals.popitem() # removes end value
# print(capitals)
# 
# keys = capitals.keys()
# print(keys)
# 
# for key in capitals.keys():
#     print(key)
# 
# grades = {"Math": 50, "Physics": 79, "Urdu": 98}
# grades_keys = grades.keys()
# print(grades.get("Math"))
# grades.update({"Chemistry": 60}) #({ is necessary as this is a dictionary.
# grades.update({"Math": 72}) #.update can be used to add and update a dictionary
# for key in grades_keys:
#     print(key)
# grades.pop("Math") 
# grades.popitem()
# print(grades)
# print(grades_keys)
# 
# 
# def add (x,y):
#     print(x + y)
# 
# 
# add(3, 5) #no store in variable as we did print
# 
# 
# 
# def add (x,y):
#      return x + y
# 
# 
# print(add(5,5)) #dont store in variable
# #OR 
# result = add(5,5) #store in variable
# print(result)
# 
# 
# return more effecient as when i will understand in future i havent learnt that yet
# 
# result = print("Hello world")  #what happens here is that python sends text hello world on screen. 
#                                   #It doesn’t give a value back for Python to save.  so python replaces it
#                                   #with None. result = None. print(result) prints Non                      
# print(result)
# 
# 
# name = "Talha"
# print(name.upper())
# print(name)
# 
# print("apple" > "banana") #as 'a' in apple is less than 'b' in banana it will give false. compares alphabetica
# if "banana" > "apple":
#     print("Yes banana is greater than apples and is more superior in taste")
# else:
#     print("No apples are greater than bananas and is more superior in taste")
# 
# 
# enter_car = input("Enter a car: ")
# if enter_car == "Bughatii":
#     print("Congrats your car is the fastest in earth!")
# elif enter_car == "Tesla":
#     print("Your car is the worst in existence")
# else:
#     print("You cannot enter this car. Choose between Bughatti and Tesla")
# 
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can sign up for a credit card")
# elif age < 0:
#     print("You havent been born yet!")
# else:
#     print("You must be 18+ to sign up!")
# 
# 
# response = input("Do you want some food ? (Y/N): ")
# if response == "Y":
#     print("Have some food")
# elif response == "N":
#     print("ok! no food for you")
# 
#name project use string method is.digit()
# name = input("Enter your name: ")
# if name == "":
#     print("You did not enter your name")
# elif name.isdigit():
#     print("Your name have numbers!")
# else:
#     print("Your name is", name)
# 
# for_sale = True
# if for_sale:
#     print("this item is for sale")
# else:
#     print("This item is not for sale")
# 
# 
# 
# 
# 
# 
# for_sale = False
# if for_sale:
#     print("This item is for sale")
# else:
#     print("This item is not for sale")
# 
# 
# 
# user = input("Enter username: ")
# user = False
# if user:
#     print("Your username is valid")
# else:
#     print("Your username is invalid")
# 
#X if condition else Y
# num = 5
# print("Positive" if num > 0 else "Negative")
# 
# user = "a"
# print("Alphabets" if user.isalpha() else "Integers")
# 
# zodiac = input("Enter month of birth: ")
# print("Zodiac Sign is leo" if zodiac == "January" else "Zodiac Sign is Ligma")
# 
# num = 6
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)
# 
#odd even game
# number = 5
# result = "Even" if number % 2 == 0 else "Odd"
# print(result)
# 
# 
# a = 6
# b = 7
# max_num = a if a > b else b
# print("max number is", max_num)
# 
# a = 6
# b = 7
# min_num = a if b > a else b
# print("minimum number is", min_num)
# 
# age = 25
# status = "Adult" if age >= 18 else "Teenager"
# print(status)   \
# 
# sale = True
# discount = "A discount of 25%" if sale else "No discount"
# print(discount)

a = 200
b = 400
c = 300
d = 200
# if a > b or c > d:
#     print(True)

# if b > a and c > d:
#     print(True)
# if a > b and c > d:
#     print("yes")
# else:
#     print("One of the condition is false")

# - - - Logical Operators - - - #
# temp = 20
# sunny = False   
# if temp <=0 or temp >=30:
#     print("The temperature is bad")
# else:
#     print("The temperature is good")
# if not sunny:
#     print("It is sunny outside")
# else:
#     print("It is cloudy outside")


# import random
# correctnum = random.randint(1,5)
# number = int(input("Guess a number between 1 to 5: "))
# if number == correctnum:
#     print("You guessed correct!")
# else:
#     print("You guessed wrong!", "the correct number was", correctnum )


# a = 5
# b = 3

# if a > b:
#     pass # if statement with no content, put pass statement


# - - Functions - - #
# def happy_birthday(name, age): # these are parameters and should be in order 
#  print(f"Happy birthday to {name}")
#  print(f"You are {age} years old!")
#  print("Happy birthday to you!")
# print()

# happy_birthday("Bro", 20) # these are arguments
# happy_birthday("Talha", 16)
# happy_birthday("Leena", 22)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username} ")
#     print(f"Your bill of ${amount:.2f} is due on {due_date}")
#     print()


# display_invoice("Talha", 250, "27/10/25")


# def add (x,y):
#     result = x + y
#     return result

# def subtract(x, y):
#     result = x - y
#     return result

# def multiply(x,y):
#     result = x * y
#     return result

# print(add(5,10))
# print(subtract(10,8))
# print(multiply(10,10))

# def create_a_fullname(firstname, lastname):
#     result = firstname.capitalize() + " " + lastname.capitalize()
#     return result

# fullname = create_a_fullname("talha", "junaidi")
# print(fullname)

# def my_function(name):
#     print("My name is" + " " + name)

# my_function("Talha")
# my_function("Leena")

# def my_function(name = "Talha"):
#     print("My name is ", name)

# my_function("Leena")

# def my_function(animal, name, breed):
#     print("I have a", animal, "and his name is", name, "and her breed is", breed)

# my_function(animal = "dog", name = "ella", breed = "German shepherd")

# def my_function(fruits):
#     for fruit in fruits:
#         print(fruit)
    

# fruits = ["apple", "banana", "orange"]
# my_function(fruits)

# def my_function(person):
#     print("Name:", person["Name"])
#     print("Age:", person["Age"])

# my_person = {"Name": "Talha", "Age": 16}
# my_function(my_person)












# def gaming_pc_creation():
#     cpu = input("Enter CPU: ")
#     gpu = input("Enter GPU: ")
#     motherboard = input("Enter motherboard: ")
#     ram = input("Enter RAM: ")
#     print(f"The specs of the custom built gaming pc are: {cpu}, {gpu}, {motherboard}, {ram}")

# gaming_pc_creation()

# def buy_dog():
#     breed = input("Enter dog breed you want to buy: ")
#     age = (input("Enter the dogs age that you want: "))
#     print(f"You want to buy a dog of breed {breed} and of age {age}")

# buy_dog()

# def fav_dogbreed():
#     a = input("Enter favourite dog breed: ")
#     print(f"Your favourite dog breed is {a}")

# fav_dogbreed()




# - - - Match Case Statements - - - #
# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is monday"
#         case 2:
#             return "It is Tuesday"
#         case 3:
#             return "It is Wednesday"
#         case 4:
#             return "It is Thursday"
#         case 5:
#             return "It is Friday"
#         case 6:
#             return "It is Saturday"
#         case 7:
#             return "It is Sunday"
#         case _:
#             return "Not a valid day"



# print(day_of_week(3))




# day = 1
# match day:
#     case 1:
#         print("Sunday")


# month = 1
# match month:
#     case 1:
#         print("January")


# - - for loops -- #
# for x in reversed(range(1,11)):
#     print(x)

# credit_card = "1234-5678-9101-2421"
# for x in credit_card:
#     print(x)

# for x in (range(1,11,4)):
#     print(x)

# for x in range (1,21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range (1,21):
#     if x == 13:
#         break
#     else:
#         print(x)


# userinput = input("Enter food you are eating: ")
# for x in range(1,6):
    
#     if userinput == "Protein powder":
#         print("WWWWW")
#     else:
#         print("EAT HEALTHY SMALL AS TWIG")

# list_of_nums = [1,2,3,4,5,6,7,8,9,10]
# for x in list_of_nums: #for every number in that list
#     print("This number is:", x) #do this


# - - - While Loops - - - #

# name = input("Enter your name: ")
# while name == "": #while this condition remains true
#     print("You did not enter your name") #execute this code potentially forever
#     name = input("Enter your name: ") #then reprompt the user
# else:
#     print(f"Hello, {name}")

# age = int(input("Enter your age: "))
# while age == 9:
#     print("Please come back next year! 9 years old are not permitted to go to school")
#     age = int(input("Enter your age: "))
# else:
#     print(f"You are {age} years old and are allowed to go to school")

# age = int(input("Enter your age: "))
# while age < 0:
#     print("Please enter a positive number! You cannot be negative years old")
#     age = int(input("Enter your age"))
# print(f"You are {age} years old")

# food = input("Enter a food you like: (q to quit): ")
# while not food == "q":
#     print(f"You like the foods, {food}")
#     food = input("Enter amother food you like: (q to quit): ")


# print("Bye")

# num = int(input("Enter a number between 1 - 10: "))
# while num < 1 or num > 10:
#     print("Your number has to be between 1 - 10, cannot be greater")
#     num = int(input("Enter a number between 1 - 10: "))

# print("Your number is", num)

# correct_pass = "Rimisthegoat420"
# password = input("Enter password: ")
# while password != correct_pass:
#     print("Wrong password! Try again!")
#     password = input("Enter password: ")

# else:
#     print("Correct pass was", correct_pass)

# correct_pass = 440501
# password = int(input("Enter password of safe: "))
# attempt_left = 4


# while password != correct_pass and attempt_left > 0: #“Keep looping as long as the password is wrong and I still have tries left.”
#     print("Wrong password! Try again")
#     password = int(input("Enter password of safe: "))
#     attempt_left -= 1


# else:
#     print("You are out of tries!, Correct password was", correct_pass)

# import random
# computer = random.randint(1,11)
# num = int(input("Enter a number between 1 to 10: "))

# while num != computer:
#     print("Wrong! Your number is wrong!")
#     num = int(input("Enter a number between 1 to 10: "))
              
# else:
#     print("You guessed right! correct num was", computer)


# - - - Range Function - - - #
# x = range(1,11)
# print(list(x))

# x = range(11)
# print(list(x))

# x = range(0,11,2)
# print("The numbers are",list(x))

# x = range(0,11,0.5)
# print("The numbers are",list(x))


# numbers = range(0,101,10)
# print("The table of 10 is", list(numbers))


# for num in range(1,11,2):
#     print(num)

# - - - Python Unpacking - - - #
# person = ["Maria", 29, "Data Engineer", "Spain"]

# name = person[0] # dont do this but u can just make several variables in order

# age = person[1] 

# role = person[2]

# country = person[3]

# *details, country = person
# print(country)
# print(details)

# *details, country = person #Only have mentioned country so thats why country is being important
# print(country)
# print(details)



# OWN PROECT, OWN IDEA:

# classroom = ["10 by 10 feet", "20 students", "8 subjects"]

# # space, student_strength, amount_of_subjects = classroom
# student_strength, *details = classroom

# print(student_strength)

# print(details)










# - - - FOr loops + while loops review by myself - - - #
# for i in range(1,6):
#     age = int(input("Enter your age: "))
#     if age < 18:
#         print("You need to be 18 to qualify!"), print(f"You have used {i} tries, you only have 5 tries"),
#     elif age == 18:
#         print("Yes you can qualify (Enter 100 to quit)")
#     elif age == 100 or age > 18:
#         print("bye")
#         break


# phone_num = int(input("Enter phone number you want to register: "))
# for i in range(1,5):
#     if phone_num == 0000 and 1111:
#         print("Too common phone number! please choose something else!")
#     i += 1
#     print(i)
    

# num = int(input("Enter a number between 1 to 10: "))
# while num > 10:
#     print("please enter a number between 1 to 10!!")
#     num += 1
#     num = int(input("Enter a number between 1 to 10: "))

# else:
#     print(f"The number you wrote is {num}")


# for i in range(0,3):
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
# print(f"Your name is {name} and you are {age} years old!")

# name = input("enter your name: ")
# for i in range(1,6):
#     while name != "talha":
#         print (f"Hey, {name}, your name has to be talha! this is not ur account!")
#         i += 1
#         name = input("enter your name: ")
#     else:
#         print("Welcome, Sir!", )



# age = int(input("Enter your age: "))
# while age < 18:
#     print("Your age needs to be lower than 18! Try again")
#     age += 1
#     age = int(input("Enter your age: "))
# else:
#     print(f"You are {age} years old!")

    
# for i in range(1,10):
#     age = int(input("Enter your age: "))
#     name = input("Enter your name: ")
#     if age < 16 or age > 100 and name != "talha":
#         print("Your age is matching! and this isnt ur acccount! try again!")
#         age = int(input("Enter your age: "))
#     elif age == 16 and name == "talha":
#         print("Welcome")
#         break


# age = int(input("Enter age: "))
# name = input("Enter name: ")
# while age != 16 or name != "Talha":
#     print("Wrong credentials. Try again (either one credential is wrong or both)")
#     age = int(input("Enter age: "))
#     name = input("Enter name: ")
# else:
#     print(f"Welcome, {name}, you are {age} years old")
        
        



    
    
        

    

        

# - - - Match - Case statements - - - #    

# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Saturday":
#             return True
#         case _:
#             return False
        

# print(is_weekend("Friday"))




# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":    
#             return False
#         case _:
#             return "Not a valid day"
        

# print(is_weekend("Friday"))


# def months_holidays(months):
#     match months:
#         case "June" | "July":
#             return "Yes, travel months"
#         case "august" |"september" | "november" | "december" | "january" | "february" | "march" | "april" | "may":
#             return "No travel months, only School / work months."
        




# print(months_holidays("august"))


# def months_to_travel(month):
#     match month:
#         case "January":
#             return "Yes you can travel"

# print(months_to_travel("January"))

     
 


# def months_to_travel(month):
#     match month:
#         case "January":
#             return "Yes you can travel"

# user_input = input("Enter month you want to travel in: ")
# result = months_to_travel(user_input)
# print(result)




















# def body_part_to_train(inweekday):
#     match inweekday:
#         case "Sunday" | "sunday":
#             return "back and biceps!"
#         case "Monday" | "monday":
#             return "Chest and Triceps!"
#         case "Tuesday" | "tuesday":
#             return "Shoulders and abs!"
#         case "Wednesday" | "wednesday":
#             return "Traps!"
#         case "Thursday" | "Friday" | "Saturday" | "thursday" | "friday" | "saturday":
#             return "Rest days"
#         case _:
#             return "Not a valid day"
        

# userinput = input("Enter weekday and i will tell you which body parts to train!: ")
# result = body_part_to_train(userinput)
# print(result)

# def i_dont_like_to_look_up_pastpapers(hate):
#     match hate:
#         case "History":
#             return "Worst subject ever"
#         case _:
#             return "Not that bad"
        
# userinput = input("Enter subject: ")
# result = i_dont_like_to_look_up_pastpapers(userinput)
# print(result)



# - - - READING FILES - - - #

# try:
#      with open("C:/Users/TempAdmin\Desktop/input.tx") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("That file was not found")
     

# print(file.closed)

#mY OWN PROJECT
# try:
#    with open('C:/Users/TempAdmin/Desktop/read.tx') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("You made a mistake entering file location")
    

# with open("C:/Users/TempAdmin/Desktop/2nd_work.txt") as file:
#     print(file.read())



# file_path = "C:/Users/TempAdmin/Desktop/2nd_work.txt"

# try:
#     with open(file_path,"r") as file:
#      content = file.read()
#     print(content)
# except FileNotFoundError:
#    print("Wrong file path")



# file_location = "C:/Users/TempAdmin/Desktop/2nd_work.txt"
# with open(file_location) as file:   # Logic here is that, python is saying to open this file in read mode by default and while its open, its gonna be refered as to as file. Once done using  file, it gets closed automatically behind the scenes even if something goes wrong, with does this                              
#     content = file.read()
#     print(content)





# try:
#    file_location = "C:/Users/TempAdmin/Desktop/2nd_work.txt"
#    with open(file_location) as file:
#     print(file)
# except PermissionError:
#   print("You dont have permission to read that file")


# import json
# try:
#    file_location = "C:/Users/TempAdmin/Desktop/2nd_work.json"
#    with open(file_location) as file:
#       content = json.load(file)
#       print(content["Dog breed i like"])
   
   

# except PermissionError:
#   print("You dont have permission to read that file")


# import csv 

# file_location = "C:/Users/TempAdmin/Desktop/2nd_work.csv"
# with open(file_location) as file:
#     content = csv.reader(file)
#     for line in content:
#         print(line[0])
#     print(content)

# OWN PROJECT #
# quote = int(input("What quote do you want to hear?(1, 2, 3, 4 or 5?): "))

# one, two, three, four, five = 1, 2, 3, 4, 5

# file_path = "C:/Users/TempAdmin/Desktop/ownproject.txt"


# with open(file_path) as file:
#     quotes = file.readlines()

# print(quotes[quote - 1].strip())


# OWN PROJECT #

# file_path = "C:/Users/TempAdmin/Desktop/own_project2.txt"

# fun_fact = int(input("Enter number from (1-3) to get some fun facts of the day: "))

# with open(file_path) as file:
#     funfacts = file.readlines()

# print(funfacts[fun_fact - 1].strip())


# - - - Writing FIles - - - #
# text = "Hi\n how are you doing?\n"
# with open("texttwo.txt", "a") as file:
#     file.write("\n This line was added later")

# text ="Hi\n how are you doing?\n you good?\n"
# with open("Abcd.txt","w") as file:
#     file.write(text)


# text ="Hi\n how are you doing?\n you good?\n"
# with open("Abcd.txt","a") as file:
#     file.write("Hi this text was added later dumbass")
    

# txt_data = "Hi my name is talha im learning coding as its a valuable skill and its digital superpowers"

# file_path = "C:/Users/TempAdmin/Desktop/projects_folder.txt"

# try:
#     with open(file_path, "a") as file:
#             file.write("\n" + txt_data)
#             print(f"The file {file_path} was created")
# except(FileExistsError):
#       print("That file already exists!")

# file_path = "C:/Users/TempAdmin/hi_i_created_this_file.txt"

# file_data = "spongebob GOAT ez im gonna be the best in the world ong inshallah bismillah"
# with open(file_path, "w") as file:
#     file.write(file_data)
#     print(f"File has been created in {file_path}")
    
# - - Own project - - #
# txt_data = input("Enter a note: ")

# text_file = "note.txt"

# with open(text_file,"a") as file:
#     file.write("\n" + txt_data)

# file_path = "py.txt"
# file_data = "\nThis text was added later dumbass"
# with open(file_path,"a") as file:
#     file.write(file_data)
#     print(f"File {file_path} has been created!")


# - - working with collections(lists,sets.tuples) and Json, writing files - - #
# file_path = "C:/Users/TempAdmin/employees.txt"

# employees = ["Eugene", "Patrick", "Spongebob", "Squidward"]

# with open(file_path, "w") as file:
#     for employee in employees:
#         file.write(employee + " ")
#     print(f"File {file_path} was created!")


# import json


# file_path = "C:/Users/TempAdmin/employees.json"

# employees = {"name": "Spongebob",
#              "Age": 30,
#              "Job": "cook"
# }

# with open(file_path, "w") as file:
#     json.dump(employees, file, indent=3)
#     print(f"File {file_path} was created!")


# - - CSV files, comma seperated values - - - #

# import csv
# file_path = "C:/Users/TempAdmin/employees.csv"

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", "30", "Cook"],
#              ["Sandy", 27, "Scientist"]
# ]

# with open(file_path, "w") as file:
#     writer = csv.writer(file)
#     for row in employees:
#         writer.writerow(row)
        
    
#     print(f"File {file_path} was created!")



# - - own projects of collections, json and csv files - - #

# file_path = "C:/Users/TempAdmin/cars.txt"
# cars = ["Koeinsegg", "Lamborghini", "Ferrari", "Supra"]

# with open(file_path, "w") as file:
#     for car in cars:
#         file.write(car + "\n")
#         print(f"File {file_path} was created")


# import json
# file_path = "C:/Users/TempAdmin/cars.json"
# cars = {"Name": "Koeingsegg",
#         "Launched_In": "1948",
#         "Colour": "Blue"
# }

# with open(file_path, "w") as file:
#         json.dump(cars, file)
#         print(f"File {file_path} was created")

# import csv

# file_path = "C:/Users/TempAdmin/cars.csv"
# cars = [["Car", "When_Launched", "Colour"],
# ["Koeinsegg", "1947", "Blue"],
# ["Lamborghini", "1921", "Yellow"]
# ]

# with open(file_path, "w", newline = "") as file:
#         writer = csv.writer(file)
#         for row in cars:
#                 writer.writerow(row)
        
#         print(f"File {file_path} was created")




# file_path = "C:/Users/TempAdmin/foods.txt"
# foods = ["pizza", "burgers", "biryani"]

# with open(file_path, "w") as file:
#     for food in foods:
#         file.write(food + " ")
#         print("Following txt file was created!")



# import json
# file_path = "C:/Users/TempAdmin/names.json"

# names = {"Name": "Talha", "Name2": "Taha"}
# with open(file_path, "w") as file:
#     json.dump(names, file)
#     print("Following json file was created!")



# import csv

# file_path = "C:/Users/TempAdmin/descriptions.csv"

# descriptions = [["Name", "Ethincity", "Hobbies"],
#                 ["Talha", "Pakistani", "None"],
#                 ["Taha", "Pakistani", "Gaming"]
# ]

# with open(file_path, "w", newline= "") as file:
#         writer = csv.writer(file)
#         for row in descriptions:
#             writer.writerow(row)
#             print("Following csv file was created")



# import csv 

# file_path = "a.csv"

# specs = [["GPU", "CPU", "Motherboard", "RAM"],
#          ["Rtx 3090", "i9 9900", "DDR4", "32GB RAM"],
#           ["Hi this text was added later"]
# ]

# with open(file_path, "a", newline="") as file:
#     writer = csv.writer(file)
#     for spec in specs:
#         writer.writerow(spec)
#         print("file was indeed created")
        

# import csv
# file_path = "ninja.csv"

# description = input("Enter description: ")
# descriptions = [["Name", "Age", "skin_colour"],
#                 ["Wahaj", "54", "White"]
                




# with open(file_path, "w") as file:
#     writer = csv.writer(file)
#     for row in descriptions:
#         writer.writerow(row)

#         if description == "Code":
#             print("File created!")
#         else:
#             break
        



# import csv
# try:
#     file_path = "Back2d.csv"
#     randoms = [["Cars", "Planes", "Jets"],
#                 ["Lambo", "saudi airlines plane", "F-4 JET"]]
#     with open(file_path, "x",newline = "") as file:
#             writer = csv.writer(file)
#             for random in randoms:
#                     writer.writerow(random)
#                     print(f"File {file_path} was created")
# except FileExistsError:
#        print("This file already exists!")
            
    


# - - Modules - - #

# print(help("modules"))

# print(help("math"))

# import math
# import math as m
# from math import pi

# print(math.pi)
# print(m.pi)
# print(pi)


# from math import e

# a, b, c, d, e  = 1,2,3,4,5

# result = a ** e, b ** e, c ** e, d ** e, e ** e
# print(result)

# print(a ** e)
# print(b ** e)
# print(c ** e)
# print(d ** e)
# print(e ** e)

# import example

# # print(example.pi)
# # print(example.e)
# # print(example.tau)

# number = int(input("Enter a number between 2 to 5: "))

# while number < 2 or number > 5:
#     print('number needs to be in range of 2-5!')
#     number += 1
#     number = int(input("Enter a number between 2 to 5: "))

# if number == 2:
#     print("Your number is", example.square(2))
# elif number == 3:
#     print("Your number is", example.square(3))
# elif number == 4:
#     print("Your number is", example.square(4))
# elif number == 5:
#     print("Your number is", example.square(5))


# import modul

# guess_num = int(input("Guess a number (between 1 to 10): "))

# while guess_num != modul.random_int:
#     print("U guessed wrong try again!")
#     guess_num = int(input("Guess a number (between 1 to 10): "))

# else:
#     print(f"u guessed right!, the correct number was, {modul.random_int}")



# def read_book(book):
#     print(f"U are now reading a book called {book} !")

# read_book("diary of wimpy kid")



# - - Object Oreinted Programming - - #



# class Car:
#     def __init__(self,model,year,color,For_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.For_Sale = For_sale 
        
#     def drive(self):
#         print("You drive the car!")
#     def stop(self):
#         print("You stop the car!")
            


        



# car1 = Car("BMW", 2023, "Purple", False)
# car2 = Car("Mercedes Benz", 1999, "Grey", True)

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.For_Sale)

# car1.drive()
# car2.stop()


        
# from pc import Pc

# pc1 = Pc("RTX 3090", "Ryzen 5 3600", "DDR4", "32GB")
# pc2 = Pc("gtx 1080", "i5 5500", "ddr3", "8gb ram")

# print(pc2.GPU)
# print(pc2.CPU)
# print(pc2.motherboard)
# print(pc2.RAM)

# pc2.turn_on()
# pc2.turn_off()


# - - OWN PROJECT!! - - #

# from phones import Phone

# phone1 = Phone("iphone", 13, "Black", "6 inch")
# phone2 = Phone("Samsung", "S21", "Grey", "8 inch")

# print(phone2.model)
# print(phone2.model_num)
# print(phone2.color)
# print(phone2.phone_size)

# phone1.turn_on()
# phone1.turn_off()
# phone2.describe()





# class AC:
#     def __init__(self, model, size, year):
#         self.model = model
#         self.size = size
#         self.year = year
    
#     def turnon(self):
#         print("You turned on your AC!")

# AC1 = AC("Haier", "40 inches", 2023)

# print(AC1.model)

# AC1.turnon()






# - - own real hard projects - -# 
# tasks = []

# while True:
#     task = input("Enter task: (a to stop): ")
#     if task == "a":
#         break

#     tasks.append(task)
#     print("Current tasks are:", tasks)

# delete_index = int(input("Enter the task you want to delete: 1, 2, 3 ....: ")) -1
# if 0 < delete_index < len(tasks):
#     removed = tasks.pop(delete_index)
#     print(removed)

# sc0re = "Current score is:"
# score = []
# quiz_question1 = input("What is double of radius?: ")
# quiz_question2 = input("What is meaning of Shariah?: ")
# ans1 = "Diameter".lower()
# ans2 = "Islamic law".lower()
# if quiz_question2 == ans2 and quiz_question2 == ans1:
#     score.append(f"{sc0re} 10")
#     print(score)
# elif quiz_question1 == ans1 and quiz_question2 == ans2:
#     score.append(f"{sc0re} 10")
#     print(score)
# elif quiz_question1 != ans1 and quiz_question2 != ans2:
#     score.append(f"{sc0re} 0")
#     print(score)
# elif quiz_question1 == ans1 and quiz_question2 != ans2:
#     score.append(f"{sc0re} 5")
#     print(score)
# elif quiz_question1 != ans1 and quiz_question2 == ans2:
#     score.append(f"{sc0re} 5")
#     print(score)







# file_path = 'C:/Users/TempAdmin/Desktop/New Text Document.txt'

# with open(file_path,"r") as file:
#     print(file.read())

# file_path = 'C:/Users/TempAdmin/Desktop/icreatedthis.txt'
# file_txt ="YOOO IM RELEARNING"
# with open(file_path,"w") as file:
#     print(file.write(file_txt))

# file_path = 'C:/Users/TempAdmin/Desktop/imakemistakessproject.txt'
# def my_func(note):
#     with open(file_path, "a") as file:
#         file.write(note)
# my_func("spongebob is the best" + "\n")



# import csv
# file_path = 'C:/Users/TempAdmin/Desktop/newday.csv'
# file_text = "Spongebob, squidward, hi, car, you"

# with open(file_path, "w") as file:
#     file.write(file_text)
#     print("Csv file was created")

# import json
# # file_path = 'C:/Users/TempAdmin/Desktop/newdayuuuu.json'
# # cars = {"car":"Lambo",
# #              "Color":"Blue"
# # }


# # with open(file_path, "w") as file:
# #     json.dump(cars, file)
# #     print("following json file was created")

# students = dict(Talha = "Grade 10", Zooiz = "Grade 10", Wasey = "Grade 11")
# print(dict.copy(students))
# print(students.keys())
# print(students.values())
# students.update(Mustufa = "Grade 9")
# students.pop("Talha")
# students.popitem()
# print(students)

# books = []
# while True:
#     title = input("Enter title: ")
#     author = input("Enter author: ")
#     year = int(input("Enter year book was published: "))

#     book = {"title": title, "author": author, "year": year
# }
#     books.append(book)
#     print(books)





# notes = []
# while True:
#     note = input("Enter your notes: (Press stop to stop): ")
#     if note == "stop":
#         break
#     notes.append(note)
#     print(notes)

# delete_a_note = int(input("Enter the integer for the value of note you want to delete:"))
# if delete_a_note == 0:
#     notes.remove(notes[0])
#     print(notes)  
# elif delete_a_note == 1:
#     notes.remove(notes[1])        
#     print(notes)  


# import random
# chars = "asdfcghjklqwertyuiopp[asdfghjklzxcvbnm=-()]"
# length = int(input("Enter length: "))
# password = " "

# for a in range(length):
#     password+=random.choice(chars)
# print(password)


# num1, num2, num3, num4 = int(input("Enter a number: ")), int(input("Enter a number: ")), int(input("Enter a number: ")), int(input("Enter a number: "))

# symbol = input("Enter a symbol: ")

# if symbol == "+":
#     print(num1 + num2 + num3 + num4)
    
# elif symbol == "-":
#     print(num1 - num2 - num3 - num4)

# elif symbol == "/":
#     print(num1 / num2 / num3 / num4)

# elif symbol == "*":
#     print(num1 * num2 * num3 * num4)

# elif symbol == "**":
#     print(num1 ** num2 ** num3 ** num4)

# elif symbol != "+" or "-" or "/" "*":
#     print("Invalid symbol! Please make sure symbols only have +, -, /, *, **. ")
  

import math
nums = []
while True:
    num = int(input("Enter number between 1 to 100. (press 0 to stop): " ))
    num_count = len(nums) + 1
    print("You wrote this amount of numbers", num_count)
    nums.append(num)
    if num == 0:
        nums.remove(0)
        break
    elif num > 100 or num < 1:
        print("Number must be in between 1 to 100!")
        num = int(input("Enter number between 1 to 100. (press 0 to stop): " ))


symbol = input("Enter symbol: (+, -, /, *, **) ")

if symbol == "+":
    sum1 = sum(nums)
    print("Sum of numbers you wrote is:", sum1)

elif symbol == "-":
    if num_count == 3:
        print(nums[0] - nums[1])
    if num_count == 4:
        print(nums[0] - nums[1] - nums[3])
    if num_count == 5:
        print(nums[0] - nums[1] - nums[2] - nums[3])
    if num_count == 6:
        print(nums[0] - nums[1] - nums[2] - nums[3])

elif symbol == "*":
    result = math.prod(nums)
    print(result)

elif symbol == "/":
    if num_count == 3:
        print(nums[0] / nums[1])
    elif num_count == 4:
        print(nums[0] / nums[1] / nums[2])
    elif num_count == 5:
        print(nums[0] / nums[1] / nums[2] / nums[3])
    elif num_count == 6:
        print(nums[0] / nums[1] / nums[2] / nums[3] / nums[4])

    
    





