# pizza cost 

pizza_size= []
pizza_toppings = []
delivery_distance = []
prices = []
total = 0 

while True:
    pizza_size = input("enter pizza size(q to quit):")
    if pizza_size.lower() == "q" :
        break
  
    if pizza_size == "small":
        price = 8
    elif pizza_size == "large":
        price = 12
    else:
        print("Invalid size")
        continue

    toppings = int(input("Enter number of toppings: "))
    distance = float(input("Enter delivery distance: "))

    # toppings cost
    price += toppings * 1
    toppings = int(input("Enter number of toppings: "))
    if toppings <=0:
            print("invalid input.")
            continue

    # delivery fee
    if distance <= 5:
        price += 2
    else:
        price += 2 + (distance - 5)
    distance = float(input("Enter delivery distance: "))
    if distance <=0:
            print("invalid input.")
            continue

    total += price

    print(f"total cost:${price}")

