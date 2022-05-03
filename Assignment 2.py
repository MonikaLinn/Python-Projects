#Part 1:
print("Tickets Cost 14 Dollars")
a = 18
b = 65
ageCheck = int(input("What is your age?: "))
if (ageCheck < a):
    print("Your age is less than 18, you qualify for a discount. Your ticket is now $10.")
elif (ageCheck >= b):
    print("Since you are a senior citizen, you qualify for a discount. Your ticket is now $10.")
else:
    print("You do not qualify for a discount, your ticket price is $14.")

#Part 2:
score = float(input('Input your score (1-100): '))
if 100 >= score >= 90:
    print('no you got an A!')
elif 89 >= score >= 80:
    print('no you got a B!')
elif 79 >= score >= 70:
    print("it's a C!")
elif 69 >= score >= 60:
    print("it's a D")
elif 59 >= score >= 1:
    print("Yeah you did fail, I'm sorry.")

#Part 3:
print('out how', end=' ')
for x in range(5): print('low', end=' ')
print('')
print('can you', end=' ')
i = 1
while i < 6:
    y = ('go')
    print (y, end=' ')
    
    i += 1

#Part 4:
import random
print('Please pick a number between 0 and 100.')
x = int(input())
print('You choose: ' + str(x))
y = int(random.randint(0, 100))
print('Dealer has: ' + str(y))
c = 21
a = x - c
b = y - c
abs(a)
abs(b)
if a > b:
    print('Dealer Wins, ' + str(y) + ' is closer to 21.')
else:
    print('You win, ' + str(x) + ' is closer to 21.')

#Part 5:
import random
dealer = 0
player = 0
i = 21
c = 21
x = 0
while i != x:
    print('Please pick a number between 0 and 100.')
    x = int(input())
    print('You choose: ' + str(x))
    y = int(random.randint(0, 100))
    print('Dealer has: ' + str(y))
    a = x - c
    b = y - c

    abs(a)
    abs(b)

    if a > b or a == 21:
        print('Dealer Wins, ' + str(y) + ' is closer to 21.\n')
        dealer += 1
    elif b > a or b == 21:
        print('You win, ' + str(x) + ' is closer to 21.\n')
        player += 1
        
        hands = dealer + player

if x == 21:
    print('Number of hands played: ' + str(hands))
    print('Dealer won: ' + str(dealer) + ' Player won: ' + str(player))
    print("You're " + str(player) + " for " + str(dealer) + ". Come back to the CS 87a Casino soon")
    i += 3
