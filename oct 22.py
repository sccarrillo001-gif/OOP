class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0

def add_values_to_cust (self):
    self.cid = input("Enter the Customer ID: ")
    self.cname = input("Enter the Customer Name: ")
    self.acc_no = input("Enter the Customer account number: ")
    self.phone = input("Enter the Customer phone: ")
    self.emailID = input("Enter the Customer email: ")


def debit_from(self, amount):
    self.balance = self.balance - amount


def debit_to(self):
    self.balance = self.balance + amount


def display_cust_info(self):
    print("Customer ID: ", self.cid)
    print("Customer Name: ", self.cname)
    print("Customer accunt number: ", self.acc_no)
    print("Customer phone: ", self.phone)
    print("Customer emailId: ", self.emailID)
    print("Customer balance: ", self.balance)



#MAIN CODE

c1 = Customer()
c2 = Customer()
c1.add_values_to_cust()
c2.add_values_to_cust()

amount = float(input("Enter the amount"))

c1.debit_from(amount)
c2.credit_to(amount)

c1.display_cust_info()
c2.display_cust_info()