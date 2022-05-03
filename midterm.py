import random


def main():
   loop = True

   balance = 0.0
   efees = 0.0
   tfees = 0.0
   tboxfees = 0.0
   eboxfees = 0.0
   won = 0.0
   wonE = 0
   wonEb = 0
   wonT = 0
   wonTb = 0
   lostE = 0
   lostEb = 0
   lostT = 0
   lostTb = 0

   Horses = []
   n = int(input("How many Horses do you want?: "))
   print("Enter " + str(n) + " horse names: ")

   for i in range(0, n):
       ele = input(str(i) + ": ")
       Horses.append(ele)

   def readysetgo():
       random.shuffle(Horses)
       print("Winning Horse List: " + str(Horses))

   while loop:

       print_menu()

       choice = input("Please enter your choice: ")
       if choice == "1":
           print("--Exacta Bet--")
           efees += 10
           readysetgo()
           guess = list(map(str, input("Enter your guess: ").split()))

           answer = Horses[0:2]
           if answer == guess:
               print("Congrats your bet was correct, you won $100")
               won += 100
               wonE += 1
           else:
               print("Sorry you lost")
               lostE += 1

       elif choice == "2":
           print("--Exactabox Bet--")
           eboxfees += 5
           readysetgo()
           guess = list(map(str, input("Enter your guess: ").split()))

           answer = Horses[0:2]
           answer1 = Horses[0:2]
           answer1.reverse()
           if guess == answer:
               print("Congrats your bet was correct, you won $50")
               won += 50
               wonEb += 1
           elif guess == answer1:
               print("Congrats your bet was correct, you won $50")
               won += 50
               wonEb += 1
           else:
               print("Sorry you lost")
               lostEb += 1

       elif choice == "3":
           print("--Trifecta bet--")
           tfees += 25
           readysetgo()
           guess = list(map(str, input("Enter your guess: ").split()))

           answer = Horses[0:3]
           if answer == guess:
               print("Congrats your bet was correct, you won $200")
               won += 200
               wonT += 1
           else:
               print("Sorry you lost")
               lostT += 1

       elif choice == "4":
           print("--Trifectabox bet--")
           tboxfees += 20
           readysetgo()
           guess = list(map(str, input("Enter your guess: ").split()))

           answer = Horses[0:3]

           if set(answer).issubset(guess):
               print("Congrats your bet was correct, you won $200")
               won += 150
               wonTb += 1

           else:
               print("Sorry you lost")
               lostTb += 1

       elif choice == "5":
           balance = 200 - efees - eboxfees - tfees - tboxfees + won
           print("Your balance is:", balance)

       elif choice == "6":
           print("|     Exact bet     | Won:" + str(wonE) + " Lost:" + str(lostE))
           print("|    Exactbox bet   | Won:" + str(wonEb) + " Lost:" + str(lostEb))
           print("|    Trifecta bet   | Won:" + str(wonT) + " Lost:" + str(lostT))
           print("|  Trifectabox bet  | Won:" + str(wonTb) + " Lost:" + str(lostTb))

       elif choice == "7":
           print("Exiting program...")
           loop = False
           quit()
       else:
           print("Invalid number. Try again...")


def print_menu():
   print(16 * '-' + "Menu" + 16 * '-')
   print("Welcome to Horse Betting!")
   print(" Please select from the following options 1-6")
   print("     1. Place an exacta bet")
   print("     2. Place an exactabox bet")
   print("     3. Place an trifecta bet")
   print("     4. Place an trifectabox bet")
   print("     5. See your USD balance")
   print("     6. Betting History")
   print("     7. Exit")
   print(37 * '-')


main()
