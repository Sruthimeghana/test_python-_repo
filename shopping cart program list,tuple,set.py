# # shopping cart program by using list, tuples, sets:
# ===================================================
foods = []
prices=[]
total=0
while True:
      food =input("Enter food items names to quit q or quit: ")
      if food == "q":
          food .lower()
          break
      else:
          price = float( input(f" enter a {food}  amont: $ " ))
          foods.append(food)
          prices.append(price)
print("__________YOUR CART________")

for food in foods:
    print(food , end=" ")
for price in prices:
   total += price

print()
print("total amount:",{total})

output:
Enter food items names to quit q or quit: pizaa
 enter a pizaa  amont: $ 8
Enter food items names to quit q or quit: hotdog
 enter a hotdog  amont: $ 6
Enter food items names to quit q or quit: burger
 enter a burger  amont: $ 6
Enter food items names to quit q or quit: q
__________YOUR CART________
pizaa hotdog burger
total amount: {20.0}

