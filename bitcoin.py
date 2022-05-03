import random
from datetime import datetime
class ledger():
    def __init__(self):
        self.trans = []

    def add(self, tran):
        self.trans.append(tran)

    def multiadd(self, *tranargs):
        self.trans.extend(tranargs)

    def multiadd2(self, tranargs):
        self.trans.extend(tranargs)

    def getTrans(self):
        return self.trans

    def printTrans(self):
        print(self.trans)

    def prettyPrint1(self):

        for each in self.trans:
            for item in each:
                print(item)

    def prettyPrint2(self):
        print()
        print("Purchase history")

        for each in self.trans:
            for item in each:
                print(" >> ", item, end="")

            print()

class MyDate():
    def print_Date(self):
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        return dt_string

def print_menu():
    print(16 * '-' + "Menu" + 16 * '-')
    print("Welcome to Raining Tigers Crypto!")
    print(" Please select from the following options 1-6")
    print(" 1. Price of BTC")
    print(" 2. Buy BTC")
    print(" 3. Sell BTC")
    print(" 4. Check Balance")
    print(" 5. Purchase History")
    print(" 6. Exit")
    print(37 * '-')

def main():
    bought = 0
    loop = True
    balance = 0
    sell = 0
    sold = 0
    bought = 0.0
    buy = 0.0
    buying = 0.0
    selling = 0.0

    T = ledger()
    date = MyDate()

    def wallet(z, s):
        wallet_bal = 75000 - bought + sold
        return wallet_bal

    def get_live(x, y):
        value = random.randint(x, y)
        return value

    while loop:
        print_menu()
        choice = input("Please enter your choice: ")
        if choice == "1":
            value = get_live(54000, 60000)
            print(value)

        if choice == "2":
            bought = 0
            value = get_live(54000, 60000)
            print("The current value of BTC is:", value)
            buy = float(input("How many BTC would you like to purchase: "))
            buying += buy
            bought = buying * value
            theDate = date.print_Date()
            item = "Bought " + "{:.2f}".format(buy) + " bitcoin(s)"
            T.add([theDate, "bought " + "{:.2f}".format(buy) + " bitcoin(s)"])
            print(item)
        
        if choice == "3":
            sold = 0
            value = get_live(54000, 60000)
            print("The current value of BTC is:", value)
            sell = float(input("How many BTC would you like to sell: "))
            selling += sell
            sold = selling * value
            theDate = date.print_Date()
            item = "Sold " + "{:.2f}".format(sell) + " bitcoin(s)"
            T.add([theDate, "sold " + "{:.2f}".format(sell) + " bitcoin(s)"])
            print(item)
        
        if choice == "4":
            wallet_bal = wallet(bought, sold)
            print(wallet_bal)
        
        if choice == "5":
            T.prettyPrint2()
        
        if choice == "6":
            break


main()