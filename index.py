# no parameter, no return value

def print_welcome():
    print("Welcome to python for Datascience")
    
print_welcome()

# parameters and a rerutn value

def square(numbers):
    return numbers * numbers

print(square(5))

result = square(9)
print(result)

def square(*numbers):
    "square each number and return a list"
    return[number * number for number in numbers]


print(square(2, 4, 8))

# Default parameter values ( You assign a default value to any parameter, incase the caller omits it, it defaults to the deafualted paremter )


def greet(name, language='English'):
    if language == 'English':
        print(f"Hello, {name}")
    elif language == 'Swahili':
        print(f"Habari,{name}")
    else :
        print ("bwakire")
    

greet("Diana")
greet("Alice", "Swahili")

# Create a function within a function, the first function defines temperature validations. The next function uses the first function to classify temperature

# Tupples 

coordinates = (-1.286578, 34.56789)
students = ("Alice", 20, "Computer Science")
empty_tupple = ()
single_tupple = ("Diana",) # tupple
single_tupple = ("Dee") # string

# Accessing tupples

students = ("Alice", 20, "Computer Science", 40, 60) # zero-based indexing to access elements in a tupple

print(students[0])
print(students[2])
print(students[1:4]) # start stop end
print(students[:2])
print(students[2:])

def square(n):
    return n*n

numbers = list(range(1,6))
print(numbers)

# Accessing the list

scores = [ 72, 85, 90, 61, 78]

print(scores[0]) # first item
print(scores[-1]) # last item
print(scores[1:4]) # items at 1, 2, 3
print(scores[:3]) # the first three items
print(scores[2:]) # items from index 2 to the end


# Modify lists

fruits = ["mangos", "pawpaw", "apples", "bananas"]
fruits[2]
# Add items

fruits.append("Ovacado")
print(fruits)

fruits.insert(0, "Pineaple")
print(fruits)

# Remove items

fruits.remove("apples") # remove by value
print(fruits)

# removes and returns last item

popped =  fruits.pop()
print(popped)

# remove and return item at index

popped =  fruits.pop(2)
print(popped)

popped  = fruits.pop(2)
print(popped)

del fruits[1]
print(fruits)


# sort, sort reverse,  len(), count()


# list comprehension is a concise way of writing code.

scores = [ 72, 85, 90, 61, 78]

# passing = []

# for score  in scores:
#     if score >= 70:
#         passing.append(score)
        
# print(passing)


# list comprehension

passing = [score for score in scores if score >=70]
print(passing)
