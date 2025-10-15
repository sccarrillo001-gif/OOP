import pickle
class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""
    def get_product_details(self):
        self.pid = input("Enter the Product ID: ")
        self.pname = input("Enter the Product Name: ")
        self.price = input("Enter the Product price: ")
        self.description = input("Enter the Product description: ")

    def display_product_info(self) :
        print("\nProduct Information:")
        print("Product ID: ", self.pid)
        print("Product Name: ", self.pname)
        print("Product price: ", self.price)
        print("Product description: ", self.description)

# Main Code-----------------------------------------------------------
while 1:
    print("1. Create a product object")
    print("2. Get information for the product")
    print("3. Display the product")
    print("4. Write the product into a file")
    print("5. Read from the file and display the product information")
    print("8. Quit")

    option = input("Enter your choice: ")

    if option == "1":
        product_obj = Product()

    elif option == "2":
        product_obj.get_product_details()

    elif option == "3":
        product_obj.display_product_info()

    elif option == "4":
        file1 = open("product_inventory.dat", "ab" )
        pickle.dump(product_obj, file1)
        file1.close()

    elif option == "5":
        file2 = open("product_inventory.dat", "rb")
        while 1:
            try:
                received_product = pickle.load(file2)
                received_product.display_product_info()
                print(received_product.pname)

            except EOFError:
                break

        file2.close




