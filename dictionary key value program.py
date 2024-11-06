 # menu items  program
# menu = {
#     "Pasta": 12.99,
#     "Burger": 9.99,
#     "Caesar Salad": 7.99,
#     "Margherita Pizza": 10.49,
#     "Soda": 1.99,
#     "Coffee": 2.49,
#     "Cheesecake": 4.99
# }
#
# cart = []
# total = 0
#
# print("---------------- Menu ----------------")
# for item, price in menu.items():
#     print(f"{item:20}: ${price:.2f}")
# print("--------------------------------------")
#
# # Input loop for selecting food items
# while True:
#     food = input("Select an item for food (or 'q' to quit): ").strip()
#     if food.lower() == 'q':
#         break
#     elif food in menu:  # Check if the food item exists in the menu
#         cart.append(food)  # Add the item to the cart
#         print(f"Added {food} to cart.")
#     else:
#         print("Item not found. Please select from the menu.")
#
# # Display the cart contents
# print("\nItems in your cart:")
# for food in cart:
#     total += menu[food]  # Calculate the total using the item price from the menu
#     print(food, end=" ")
#
# print()
# print(f"\nTotal amount: ${total:.2f}")  # Print the total amount



menu = {
    "Pasta": 12.99,
    "Burger": 9.99,
    "Caesar Salad": 7.99,
    "Margherita Pizza": 10.49,
    "Soda": 1.99,
    "Coffee": 2.49,
    "Cheesecake": 4.99
}
cart=[]
total =0
print("----------------menu-----------")
for key,value in menu.items():
     print(f" {key:20}: ${value :.2f}")
print("--------------------------------------")
while True:
     food = input("select an item for food q or quit:").lower()
     if food == 'q':
        break
     elif menu.get(food) is not None:
          cart.append(food)
print(cart)
for food in cart:
    total += menu.get(food)
    print(food,end=" ")
print()
print(f"Total amount:,${total:.2f}")
