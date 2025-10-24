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

def debit_from(self, quantity):
    self.balance = self.balance - quantity


def debit_to(self, quantity):
    self.balance = self.balance + quantity


def display_cust_info(self):
    print("Customer ID: ", self.cid)
    print("Customer Name: ", self.cname)
    print("Customer accunt number: ", self.acc_number)
    print("Customer phone: ", self.phone)
    print("Customer emailId: ", self.emailID)
    print("Customer balance: ", self.balance)

def assign_debit_card(self, dcards):

    self.credit_card.append(dcards)
    print(dcards.card_number, "added to", self.cname)

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
    self.balance = input("Enter the Card balance: ")

def display_card_info(self):
    print("Card type: ", self.type)
    print("Card card number: ", self.card_number)
    print("Card cvv: ", self.cvv)
    print("Card expiry date: ", self.expiry_date)
    print("Card balance: ", self.balance)


#MAIN CODE


cust1 = Customers()
cust1.add_values_to_cust()

card1 = Cards()
card1.add_values_to_card()

cust1.assign_debit_card()




