print("Hello, welcome to Starbucks")
name = input("What is your name? ")

print ("Hello, " + name + ", thank you so much for coming in today!\n")

menu = "Black Coffee, Espresso, Latte, Cappuccino"

print (name + ", what would you like from our menu today? Here is what we are serving:\n" + menu)

order = input ()
price = 8
quantity = input("How many coffees would you like?\n")
total = price * int(quantity)

print ("Sounds good, " + name + ", your " + order + " will be ready in a few minutes!")
print ("Great, that will be " + str(total) + "$")
print ("Enjoy your coffee, " + name + "!")





