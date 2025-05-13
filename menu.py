menu={

    "Pizza":40,
    "Pasta":50,
    "Burger":150,
    "Salad":60,
    "Coffee":80
}
#Greeting
print("\nWelcome to the New Heaven Resort.")

# for the menu to get in display
print("\nHere is the menu for today:")
for item,price in menu.items():
    print(f"{item}:Rs.{price}")

Order_total=0
#lets add coffee in the order

while True:

    item=input("\nEnter the name of the item you want to order=").strip().title()
    if item in menu:
        Order_total +=menu[item]     #0+50
        print(f"Your item '{item}' has been added to order.")
    else:
        print("Sorry, we donot have this item")
    # lets add another item
    #ask the user if he wants to add another item
    Another_order = input("Do you want to add another item? (YES/NO): ").strip().upper()
    if Another_order!="YES":
        break
print(f"The total amount of items to pay={Order_total}")