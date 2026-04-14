# functions
# functions are named and reusable block of code that designed to perform a specific task:write it once and
#call it as many times as you need. Main reason for function is to avoid repeating code
 
# parameters and a return value(Accepts input, wrks)

# parameters and return value
def square(numbers):
    return numbers * numbers
print(square(5))

result = square(9)
print(result)
 

def greet(name, language='English'):
    if language == 'english':
        print(f"hello,{name}")
    elif language == 'spanish':
        print(f"hola mi amigo!,{name}")
    else:
        print("aaahh")

greet("Diana")
greet("alice",'english')
# Create a function within a function, the first function defines temperature validations. The next function uses the first function to classify temperature
#tuples
coordinates = (-1.676767 , 34.38934)
fruits = ["mango", "ovacado", "orange", "pineaple"]
# removes and returns last item
popped = fruits.pop()
print(popped)
pop = fruits.pop(2)
print(pop)
# sort, sort reverse, len(), count()

# functions is a block of reusable code
#  place () after the function name to invoke it
# return = statement is used to end a function
#          and send a result back to the caller.
              
def myFunc(x):
  return len(x)

food = ['chapati', 'shawarma', 'biriani', 'chips', 'mahamri']

food.sort(key=myFunc)

print(food)




r = "hello, world"
print(r[7:12])


#figure out how to split dates3 = "2024-06.15"   you can replace the dot with a /
date3 = "2024-06.15"
parts = date3.replace(".","/")
print(parts)
