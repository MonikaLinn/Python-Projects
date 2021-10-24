import random

print("Question 1. ")
x = input("Enter your name: ")
i = 1

while i < 11:
    print(str(i) + ":" + x, end=' ')
    i += 1

print("\n\nQuestion 2. ")
number = int(input("Now please enter a number: "))

if number > 50:
    print("Your number, " + str(number) + " is greater than 50.")

if number <= 50:
    print("Your number, " + str(number) + " is not greater than 50.")

print("\nQuestion 3. ")
absNum = int(input("Please enter a negative number: "))
absValue = abs(absNum)
print("The Absolute Value of " + str(absNum) + " is " + str(absValue))


print("\nQuestion 4. ")
randomNum = int(random.randint(100, 200))
print("Here's a random number, " + str(randomNum) + ".")

print("\nQuestion 5. ")
math = int(input("Please enter a number: "))
print("The Alternating Series is ")
for k in range(1, math):
    result = (-1)**(k) * k
    print(str(result), end=', ')
k = math
result = (-1)**(k) * k
print(result)

print("\nQuestion 6. ")
volts = int(input("Please enter a number (1-100): "))
if 1 <= volts <= 30:
    print(str(volts) + ", is a low voltage number.\n")

elif 30 <= volts <= 60:
    print(str(volts) + ", is a medium voltage number.\n")

elif 61 <= volts <= 100:
    print(str(volts) + ", is a high voltage number.\n")

print("Question 7.")
y = input("Enter your name: ")
i = 1
z = 0
while i < 11:
    print(str(i) + ":" + y + " " + str(z), end=' | ')
    i += 1
    z += 1

print("\n\nQuestion 8.")
i = 0
z = 0
g = 0
k = 0
while i < 1:
    g = int(input("Please enter a number: "))
    if g == 0:
        print("You have entered " + str(z) + " numbers over 50")
        i += 1
    elif g > 50:
        print("Your number, " + str(g) + " is greater than 50.")
        z += 1
    else:
        print("Your number, " + str(g) + " is not greater than 50.")

