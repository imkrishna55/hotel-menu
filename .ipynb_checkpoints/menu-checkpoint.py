menu={

    "Pizza":40,
    "Pasta":50,
    "Burger":150,
    "Salad":60,
    "Coffee":80
}
#Greeting
print("Welcome to the New Heaven Resort.")

# for the menu to get in throw
for item,price in menu.items():
    print(f"{item}:Rs.{price}")

Order_total=0
#lets add coffee in the order

item_1=input("Enter the name of the item you want to order=")
if item_1 in menu:
    Order_total +=menu[item_1]     #0+50
    print(f"Your item {item_1} has been added to order.")
else:
    print("Sorry, we donot have this item")

Another_order= input("Do you want to add sommething else? (YES/NO)")
if Another_order=="YES":
    item_2=input("Enter the name of the second item=")
    if item_2 in menu:
        Order_total +=menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Sorry, we donot have {item_2} !")

print(f"The total amount of items to pay={Order_total}")

