import pickle

class Customers:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_number = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = []

    def add_values_to_cust (self):
        self.cid = input("Enter the Customer ID: ")
        self.cname = input("Enter the Customer Name: ")
        self.acc_number = input("Enter the Customer account number: ")
        self.phone = input("Enter the Customer phone: ")
        self.emailID = input("Enter the Customer email: ")
        self.balance = float(input("Enter the Customer balance: "))

    def debit_from(self, quantity):
        self.balance = self.balance - quantity

    def credit_to(self, quantity):
        self.balance = self.balance + quantity

    def display_cust_info(self):
        print("Customer ID: ", self.cid)
        print("Customer Name: ", self.cname)
        print("Customer account number: ", self.acc_number)
        print("Customer phone: ", self.phone)
        print("Customer emailId: ", self.emailID)
        print("Customer balance: ", self.balance)
        
        print("Debit Cards:")
        for d in self.debit_card:
            d.display_card_info()

        print("Credit Cards:")
        for c in self.credit_card:
            c.display_card_info()
         
    def assign_debit_card(self, dcard):
        self.debit_card.append(dcard)
        print(dcard.card_number, "added to", self.cname)

    def assign_credit_card(self, ccards):
        self.credit_card.append(ccards)
        print(ccards.card_number, "added to", self.cname)

class Cards:
    def __init__(self):
        self.type = ""
        self.card_number = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0.0

    def add_values_to_card (self):
        self.type = input("Enter the Card type: ")
        self.card_number = input("Enter the Card number: ")
        self.cvv = input("Enter the Card cvv: ")
        self.expiry_date = input("Enter the Card expiry date: ")


    def display_card_info(self):
        print("Card type: ", self.type)
        print("Card card number: ", self.card_number)
        print("Card cvv: ", self.cvv)
        print("Card expiry date: ", self.expiry_date)
        print("Card balance: ", self.balance)


#MAIN CODE
customers = {}
cards = {}

while 1:
    print("1. Create customer")
    print("2. Create cards")
    print("3. Transfer funds")
    print("4. Assign credit card")
    print("5. Assign debit card")
    print("6. Display customer info")
    print("7. Display card info")
    print("8. Commit")
    print("9. Quit")

    option = input("Enter your choice: ")

    if option == "1":
        cust1 = Customers()
        cust1.add_values_to_cust()
        customers[cust1.cid] = cust1

    elif option == "2":
        card1 = Cards()
        card1.add_values_to_card()
        cards[card1.card_number] = card1

    elif option == "3":
        cust_id1 = input("Enter customer ID that will send money: ")
        cust_id2 = input("Enter Customer ID that will receive money: ")
        quantity = float(input("Enter amount to transfer: "))

        if cust_id1 in customers and cust_id2 in customers:
            customers[cust_id1].debit_from(quantity)
            customers[cust_id2].credit_to(quantity)
        
        else:
            print("Customers not found.")

    elif option == "4":
        cust_id = input("Enter Customer ID: ")
        card_number = input("Enter Credit Card Number: ")

        if cust_id in customers and card_number in cards and cards[card_number].type == "credit":
            customers[cust_id].assign_credit_card(cards[card_number])
            print("Credit card assigned successfully.")
        else:
            print("Customer or Card not found.")


    elif option == "5":
        cust_id = input("Enter Customer ID: ")
        card_number = input("Enter Debit Card Number: ")

        if cust_id in customers and card_number in cards and cards[card_number].type == "debit":
            customers[cust_id].assign_debit_card(cards[card_number])
            print("Debit card assigned successfully.")
        else:
            print("Customer or Card not found.")

    elif option == "6":
        for cid in customers:
            customers[cid].display_cust_info()

    elif option == "7":
        for card_number in cards:
            cards[card_number].display_card_info()

    elif option == "8":
        file = open("bankDictionaries.dat", "wb")
        pickle.dump({"customers": customers, "cards": cards}, file)
        print("Data saved successfully to bankDictionaries.dat")
    
    elif option == "9":
        print("Thank you for using the program")
        break



