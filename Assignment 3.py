import random
print("Good Luck!")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo','violet']
print("Try to get the '+' to the other side")
print("In order to move answer the questions correctly")

correct = 0
lines = int
x = 6
tries = 1
pancake = True
soup = True
pudding = True
waffle = True
mocha = True
coffee = True
tea = True
incorrect = 0

print(" " * 8 + "+" + " " * 8)
for lines in range(x):
    print("-" * 17)
while pancake:
    guess = input("What is one color in the rainbow? : ")
    if guess in colors:
        x -= 1
        print("Correct!")
        print("-" * 8 + "+" + "-" * 8)
        
        for lines in range(x):
            print("-" * 17)
            pancake = False

    if guess not in colors:
        print("Incorrect")
        tries += 1
        print(" " * 8 + "+" + " " * 8)
        
        for lines in range(x):
            print("-" * 17)

    if tries >= 5:
        print("Game Over")
        exit()

while soup:
    guess = input("What is another color in the rainbow? : ")
    if guess in colors:
        x -= 1
        correct += 1
        print("Correct!")
        
        for lines in range(correct):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)
        
        for lines in range(x):
            print("-" * 17)
            soup = False

    if guess not in colors:
        print("Incorrect!")
        incorrect += 1
        tries += 1

        for lines in range(incorrect):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)
        for lines in range(x):
            print("-" * 17)
        if tries >= 5:
            print("Game Over")
            exit()

compass = ['west', 'north', 'east', 'south']

while pudding:
    guess1 = input("What is one of the 4 major compass directions? : ")
    if guess1 in compass:
        x -= 1
        correct += 1
        print("Correct!")
        
        for lines in range(correct):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)
        
        for lines in range(x):
            print("-" * 17)
        pudding = False
    
    if guess1 not in compass:
        print("Incorrect!")
        incorrect += 1
        tries += 1
        
        for lines in range(incorrect):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)

        for lines in range(x):
            print("-" * 17)
    if tries >= 5:
        print("Game Over")
        exit()

while waffle:
    guess2 = input("What is another one of the 4 major compass directions? : ")
    if guess2 in compass:
        x -= 1
        correct += 1
        print("Correct!")

        for lines in range(correct):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)

        for lines in range(x):
            print("-" * 17)
            waffle = False

    if guess2 not in compass:
        print("Incorrect!")
        incorrect += 1
        tries += 1

        for lines in range(incorrect):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)

        for lines in range(x):
            print("-" * 17)

    if tries >= 5:
        print("Game Over")
        exit()

primary = ['red', 'yellow', 'blue']

while mocha:
    guess3 = input("What is one of the primary colors? : ")
    if guess3 in primary:
        x -= 1
        correct += 1
        print("Correct!")

        for lines in range(correct):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)

        for lines in range(x):
            print("-" * 17)
            mocha = False

    if guess3 not in primary:
        print("Incorrect!")
        incorrect += 1
        tries += 1
        
        for lines in range(incorrect):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)

        for lines in range(x):
            print("-" * 17)
    
    if tries >= 5:
        print("Game Over")
        exit()

military = ['space force', 'army', 'air force', 'marine corps',
'coast guard', 'navy']

while coffee:
    guess4 = input("What is one of 6 military branches? : ")
    if guess4 in military:
        x -= 1
        correct += 1
        print("Correct!")

        for lines in range(correct):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)

        for lines in range(x):
            print("-" * 17)
        coffee = False

    if guess4 not in military:
        print("Incorrect!")
        incorrect += 1
        tries += 1
        
        for lines in range(incorrect):
            print("-" * 17)
        print("-" * 8 + "+" + "-" * 8)
        
        for lines in range(x):
            print("-" * 17)

    if tries >= 5:
        print("Game Over")
        exit()

military = ['space force', 'army', 'air force', 'marine corps', 'coast guard', 'navy']
while tea:
    guess4 = input("What is another one of 6 military branches? : ")
    if guess4 in military:
        x -= 1
        correct += 1
        print("Correct! Congratulations you beat the game")
        
        for lines in range(correct):
            print("-" * 17)
        print(" " * 8 + "+" + " " * 8)
        tea = False
        
        if guess4 not in military:
            print("Incorrect!")
            incorrect += 1
            tries += 1

        for lines in range(incorrect):
            print("-" * 17)

        print("-" * 8 + "+" + "-" * 8)
        for lines in range(x):
            print("-" * 17)

    if tries >= 5:
        print("Game Over")
        exit()