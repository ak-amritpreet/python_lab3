Shopping_Cart = {}

def Add_Product():
    if len(Shopping_Cart) >= 5:
        print("Cart is full.")
    else:
        Product = input("Enter the product name: ")
        Brand_Name = input("Enter the brand of the product: ")
        Shopping_Cart[Product] = Brand_Name
        print("Product added to cart.")

def Search_Product():
    Product_Name = input("Enter the name of the product to search: ")
    if Product_Name in Shopping_Cart:
        print(f"{Product_Name} found in cart. Brand: {Shopping_Cart[Product_Name]}.")
    else:
        print("No product exists with the name mentioned.")

def Delete_Product():
    if len(Shopping_Cart) == 0:
        print("Cart is empty ... No items found.")
    else:
        productName = input("Enter the name of the product for deleting: ")
        if productName in Shopping_Cart:
            del Shopping_Cart[productName]
            print(f"{productName} removed from cart.")
        else:
            print("No product exists with the name mentioned.")

# MAIN_MENU
while True:
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("A. Add product to the cart.")
    print("B. Search the product.")
    print("C. Delete the product from the cart.")
    print("D. Quit.")
    choice = input("Enter your choice (A/B/C/D): ")

    if choice.lower() == 'a':
        Add_Product()
    elif choice.lower() == 'b':
        Search_Product()
    elif choice.lower() == 'c':
        Delete_Product()
    elif choice.lower() == 'd':
        print("Thank you for using Amando Shopping Site!")
        break
    else:
        print("Invalid choice. Please enter a valid choice (A..B..C..D).")
