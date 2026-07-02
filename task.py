menu = {
    "Pizza": 500,
    "Burger": 200,
    "Pasta": 300,
    "Sandwich": 150,
    "Fries": 100
}

print("Welcome to Our Restorant")
print("""Here is our menu for you. Please select your action from below options:
1. Pizza : Rs. 500
2. Burger : Rs. 200
3. Pasta : Rs. 300
4. Sandwich : Rs. 150
5. Fries : Rs. 100""")

total_bill = 0
item = (input("Please select your item from the menu: ")).capitalize()
if item in menu:
    total_bill += menu[item]
    print(f"Your item {item} has been added to your order.")
else:
    print(f"Item {item} is not available in the menu yet.")
print(f"Your total bill is: Rs. {total_bill}")

another_item = input("Do you want to order another item? (yes/no): ").lower()
# while another_item == "yes":
#     item = (input("Please select your item from the menu: ")).capitalize()
#     if item in menu:
#         total_bill += menu[item]
#         print(f"Your item {item} has been added to your order.")
#     else:
#         print(f"Item {item} is not available in the menu yet.")
#     another_item = input("Do you want to order another item? (yes/no): ").lower()
if another_item == "yes":
    item = (input("Please select your item from the menu: ")).capitalize()
    if item in menu:
        total_bill += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Item {item} is not available in the menu yet.")
print(f"Your total bill is: Rs. {total_bill}") 
print("Thank you for your order! Please visit again.")