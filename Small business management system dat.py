# Small Business Management System

# General things
import pickle
from datetime import datetime

def get_date():
    return datetime.now()

def load_dict(filename):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except:
        return {}

def save_dict(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def get_next_id(d):
    biggest = 0
    for i in d:
        number = int(i)
        if number > biggest:
            biggest = number
    return biggest + 1 

# CUSTOMER MODULE
class CustomerManager:
    def __init__(self):
        self.filename = "customers.dat"
        self.customers = load_dict(self.filename)

    def add_customer(self):
        cname = input("Name: ")
        cemail = input("Email: ")
        cphone = input("Phone: ")
        caddress = input("Address: ")
        cid = str(get_next_id(self.customers))
        self.customers[cid] = {
            "name": cname,
            "email": cemail,
            "phone": cphone,
            "address": caddress,
            "purchase_history": [],
            "date": get_date()
        }
        save_dict(self.filename, self.customers)
        print("You added a customer")

    def show_customers(self):
        if not self.customers:
            print("No customers found")
        else:
            for cid in sorted(self.customers):
                c = self.customers[cid]
                print("ID:", cid)
                print("Name:", c["name"])
                print("Email:", c["email"])
                print("Phone:", c["phone"])
                print("Address:", c["address"])
                print("Total Purchases:", len(c["purchase_history"]))
                
    def update_customer(self):
        cid = input("Enter customer ID to update: ")
        if cid not in self.customers:
            print("Customer not found")
            return
        c = self.customers[cid]
        new_name = input("Enter new name: ")
        new_email = input("Enter new email: ")
        new_phone = input("Enter new phone: ")
        new_address = input("Enter new address: ")
        if new_name:
            c["name"] = new_name
        if new_email:
            c["email"] = new_email
        if new_phone:
            c["phone"] = new_phone
        if new_address:
            c["address"] = new_address
        self.customers[cid] = c # para que se guarde en el dict
        save_dict(self.filename, self.customers)
        print("You updated a customer")

    def delete_customer(self):
        cid = input("Enter customer ID to delete: ")
        if cid in self.customers:
            del self.customers[cid]
            save_dict(self.filename, self.customers)
            print("You deleted a customer")
        else:
            print("Customer not found")

    def search_customer(self):
        cattribute = input("Enter name OR email OR phone: ")
        found = False
        for cid in self.customers:
            c = self.customers[cid]
            if (cattribute.lower() in c["name"].lower() or
                cattribute.lower() in c["email"].lower() or
                cattribute in c["phone"]):
                print("ID:", cid)
                print("Name:", c["name"])
                print("Email:", c["email"])
                print("Phone:", c["phone"])
                print("Address:", c["address"])
                found = True
        if not found:
            print("No matching customers")

    def link_sale_to_customer(self, cid, sid):
        c = self.customers[cid]
        c["purchase_history"].append(sid)
        self.customers[cid] = c
        save_dict(self.filename, self.customers)

    def display_customer_purchases(self, sales_manager):
        cid = input("Enter customer ID: ")
        if cid not in self.customers:
            print("Customer not found")
            return
        c = self.customers[cid]
        history = c["purchase_history"]
        if not history:
            print("This customer has no purchases")
            return
        for sid in history:
            if sid in sales_manager.sales:
                s = sales_manager.sales[sid]
                print("Sale ID:", sid)
                print("Product:", s["product_name"])
                print("Quantity:", s["quantity"])
                print("Total:", s["total"])
                print("Date:", s["date"])

    def calculate_total_spent(self, sales_manager): 
        cid = input("Enter customer ID: ")
        if cid not in self.customers:
            print("Customer not found")
            return
        history = self.customers[cid]["purchase_history"]
        total = 0
        for sid in history:
            if sid in sales_manager.sales:
                total += sales_manager.sales[sid]["total"]
        print("Total spent:", total)

    def total_customers(self):
        return len(self.customers)

def customer_menu(cm, sm):
    while True:
        print("\n Customers Menu")
        print("1. Add customer")
        print("2. View all customers")
        print("3. Update customer")
        print("4. Delete customer")
        print("5. Search customer")
        print("6. Show customer purchases")
        print("7. Calculate total spent")
        print("8. Back")
        choice = input("Choose one of the options: ")
        if choice == "1": 
            cm.add_customer()
        elif choice == "2": 
            cm.show_customers()
        elif choice == "3": 
            cm.update_customer()
        elif choice == "4": 
            cm.delete_customer()
        elif choice == "5": 
            cm.search_customer()
        elif choice == "6": 
            cm.display_customer_purchases(sm)
        elif choice == "7": 
            cm.calculate_total_spent(sm)
        elif choice == "8": 
            break

#INVENTORY MODULE
class InventoryManager:
    def __init__(self):
        self.filename = "inventory.dat"
        self.products = load_dict(self.filename)

    def add_product(self):
        pname = input("Product name: ")
        pdesc = input("Description: ")
        pprice = float(input("Price: "))
        pquantity = int(input("Quantity: "))
        pcategory = input("Category: ")
        pid = str(get_next_id(self.products))
        self.products[pid] = {
            "name": pname,
            "description": pdesc,
            "price": pprice,
            "quantity": pquantity,
            "category": pcategory,
            "date": get_date()
        }
        save_dict(self.filename, self.products)
        print("You added a product")

    def show_products(self):
        if not self.products:
            print("No products")
        else:
            for pid in sorted(self.products):
                p = self.products[pid]
                print("ID:", pid)
                print("Name:", p["name"])
                print("Description:", p["description"])
                print("Price:", p["price"])
                print("Quantity:", p["quantity"])
                print("Category:", p["category"])
                

    def update_product(self):
        pid = input("Enter product ID: ")
        if pid not in self.products:
            print("Product not found")
            return
        p = self.products[pid]
        new_name = input("Enter the new product name: ")
        new_desc = input("Enter the new product name: ")
        new_price = input("Enter the new product name: ")
        new_qty = input("Enter the new product name: ")
        new_cat = input("Enter the new product name: ")
        if new_name: 
            p["name"] = new_name
        if new_desc: 
            p["description"] = new_desc
        if new_price: 
            p["price"] = float(new_price)
        if new_qty: 
            p["quantity"] = int(new_qty)
        if new_cat: 
            p["category"] = new_cat
        self.products[pid] = p
        save_dict(self.filename, self.products)
        print("You have updated a product")
        
    def delete_product(self):
        pid = input("Enter product ID: ")
        if pid in self.products:
            del self.products[pid]
            save_dict(self.filename, self.products)
            print("Product deleted")
        else:
            print("Product not found")

    def search_product(self):
        pattribute = input("Search by name OR category: ")
        found = False
        for pid in self.products:
            p = self.products[pid]
            if (pattribute.lower() in p["name"].lower() or
                pattribute.lower() in p["category"].lower()):
                print("ID:", pid)
                print("Name:", p["name"])
                print("Description:", p["description"])
                print("Price:", p["price"])
                print("Quantity:", p["quantity"])
                print("Category:", p["category"])
                found = True
        if not found:
            print("No matching products")

    def total_inventory_value(self):
        total = 0
        for pid in self.products:
            p = self.products[pid]
            total += p["price"] * p["quantity"]
        return total


def inventory_menu(im):
    while True:
        print("\n Inventory Menu")
        print("1. Add product")
        print("2. View products")
        print("3. Update product")
        print("4. Delete product")
        print("5. Search product")
        print("6. Total inventory value")
        print("7. Back")
        choice = input("Choose one of the options: ")
        if choice == "1": 
            im.add_product()
        elif choice == "2": 
            im.show_products()
        elif choice == "3": 
            im.update_product()
        elif choice == "4": 
            im.delete_product()
        elif choice == "5": 
            im.search_product()
        elif choice == "6": 
            print("Inventory value:", im.total_inventory_value())
        elif choice == "7": 
            break

# CAMPAIGNS MODULE
class CampaignManager:
    def __init__(self):
        self.filename = "campaigns.dat"
        self.campaigns = load_dict(self.filename)

    def add_campaign(self):
        caname = input("Name: ")
        cabudget = float(input("Budget: "))
        caexpenses = float(input("Expenses: "))
        carevenue = float(input("Revenue: "))
        castart = input("Start date: ")
        caend = input("End date: ")
        caid = str(get_next_id(self.campaigns))
        self.campaigns[caid] = {
            "name": caname,
            "budget": cabudget,
            "expenses": caexpenses,
            "revenue": carevenue,
            "start_date": castart,
            "end_date": caend,
        }
        save_dict(self.filename, self.campaigns)
        print("You added a campaign")

    def update_campaign(self):
        caid = input("Enter campaign ID: ")
        if caid not in self.campaigns:
            print("Campaign not found")
            return
        ca = self.campaigns[caid]
        new_name = input("Enter the new campaign name: ")
        new_budget = input("Enter the new campaign budget: ")
        new_expenses = input("Enter the new campaign expenses: ")
        new_revenue = input("Enter the new campaign revenue: ")
        new_start = input("Enter the new campaign start: ")
        new_end = input("Enter the new campaign end: ")
        if new_name: 
            ca["name"] = new_name
        if new_budget: 
            ca["budget"] = float(new_budget)
        if new_expenses: 
            ca["expenses"] = float(new_expenses)
        if new_revenue: 
            ca["revenue"] = float(new_revenue)
        if new_start: 
            ca["start_date"] = new_start
        if new_end: 
            ca["end_date"] = new_end
        self.campaigns[caid] = ca
        save_dict(self.filename, self.campaigns)
        print("Campaign updated")

    def delete_campaign(self):
        caid = input("Enter campaign ID: ")
        if caid in self.campaigns:
            del self.campaigns[caid]
            save_dict(self.filename, self.campaigns)
            print("Campaign deleted")
        else:
            print("Campaign not found")

    def show_campaigns(self):
        if not self.campaigns:
            print("No campaigns")
        else:
            for caid in sorted(self.campaigns):
                ca = self.campaigns[caid]
                ROI = 0
                if ca["expenses"] > 0:
                    ROI = (ca["revenue"] - ca["expenses"]) / ca["expenses"] * 100
                print("ID:", caid)
                print("Name:", ca["name"])
                print("Budget:", ca["budget"])
                print("Expenses:", ca["expenses"])
                print("Revenue:", ca["revenue"])
                print("ROI:", ROI)

    def search_campaign(self):
        caattribute = input("Search campaign name: ")
        found = False
        for caid in self.campaigns:
            ca = self.campaigns[caid]
            if caattribute.lower() in ca["name"].lower():
                print("ID:", caid)
                print("Name:", ca["name"])
                print("Budget:", ca["budget"])
                print("Expenses:", ca["expenses"])
                print("Revenue:", ca["revenue"])
                found = True
        if not found:
            print("No matching campaigns")

    def average_roi(self):
        total = 0
        count = 0
        for caid in self.campaigns:
            ca = self.campaigns[caid]
            if ca["expenses"] > 0:
                ROI = (ca["revenue"] - ca["expenses"]) / ca["expenses"] * 100
                total += ROI
                count += 1
        if count == 0: 
            return 0
        return total / count


def campaigns_menu(cam):
    while True:
        print("\nCampaigns Menu ")
        print("1. Add campaign")
        print("2. View campaigns")
        print("3. Update campaign")
        print("4. Delete campaign")
        print("5. Search campaign")
        print("6. Show average ROI")
        print("7. Back")
        choice = input("Choose one of the options: ")
        if choice == "1": 
            cam.add_campaign()
        elif choice == "2": 
            cam.show_campaigns()
        elif choice == "3": 
            cam.update_campaign()
        elif choice == "4": 
            cam.delete_campaign()
        elif choice == "5": 
            cam.search_campaign()
        elif choice == "6": 
            print("Average ROI:", cam.average_roi())
        elif choice == "7": 
            break

# SALES MODULE
class SalesManager:
    def __init__(self, inventory, customers):
        self.filename = "sales.dat"
        self.sales = load_dict(self.filename)
        self.inventory = inventory
        self.customers = customers  # da acceso a las funciones de los objects

    def add_sale(self):
        if not self.inventory.products:
            print("No products")
            return
        print("These are the products available: ")
        self.inventory.show_products()
        pid = input("Enter product ID: ")
        if pid not in self.inventory.products:
            print("Product not found")
            return
        if not self.customers.customers:
            print("No customers")
            return
        print("These are the posible customers: ")
        self.customers.show_customers()
        cid = input("Enter customer ID: ")
        if cid not in self.customers.customers:
            print("Customer not found")
            return

        quantity_sold = int(input("Quantity sold: "))
        product = self.inventory.products[pid]

        if quantity_sold > product["quantity"]:
            print("Not enough stock")
            return

        unit_price = product["price"]
        total_price = unit_price * quantity_sold
        sid = str(get_next_id(self.sales))

        self.sales[sid] = {
            "product_id": pid,
            "product_name": product["name"],
            "customer_id": cid,
            "quantity": quantity_sold,
            "unit_price": unit_price,
            "total": total_price,
            "date": get_date()
        }

        product["quantity"] -= quantity_sold
        self.inventory.products[pid] = product

        save_dict(self.inventory.filename, self.inventory.products)
        save_dict(self.filename, self.sales)

        self.customers.link_sale_to_customer(cid, sid)

        print("You recorded a sale")

    def show_sales(self):
        if not self.sales:
            print("No sales recorded")
        else:
            for sid in sorted(self.sales):
                s = self.sales[sid]
                print("Sale ID:", sid)
                print("Product:", s["product_name"])
                print("Customer ID:", s["customer_id"])
                print("Quantity:", s["quantity"])
                print("Total:", s["total"])
                print("Date:", s["date"])

    def total_revenue(self):
        total = 0
        for sid in self.sales:
            total += self.sales[sid]["total"]
        return total


def sales_menu(sm):
    while True:
        print("\nSales Menu")
        print("1. Record sale")
        print("2. View sales")
        print("3. Back")
        choice = input("Choose one of the options: ")
        if choice == "1": 
            sm.add_sale()
        elif choice == "2": 
            sm.show_sales()
        elif choice == "3": 
            break


# MAIN CODE
cm = CustomerManager()
im = InventoryManager()
sm = SalesManager(im, cm)
cam = CampaignManager()

while True:
    print("SMALL BUSINESS MANAGEMENT SYSTEM")
    print("1. Customers")
    print("2. Inventory")
    print("3. Sales")
    print("4. Campaigns")
    print("5. Exit")
    choice = input("Choose one of the options: ")
    if choice == "1": 
        customer_menu(cm, sm)
    elif choice == "2": 
        inventory_menu(im)
    elif choice == "3": 
        sales_menu(sm)
    elif choice == "4": 
        campaigns_menu(cam)
    elif choice == "5": 
        break
