weight = float(input("Enter your weight:"))
unit= input("Kilograms or Pounds? (k or L):")
if unit == "k":
    weight = weight * 2.205
    unit = 'lbs.'
    print(f" your weight {round(weight,1)}{unit}")
elif unit== "L":
    weight = weight /2.205
    unit= 'kgs'
    print(f" your weight {round(weight,1)} {unit}")
else:
    print(f"{unit} Enter Invalid  option....!")

# output:
# Enter your weight: 55
# Kilograms or Pounds? (k 0or L):k
#  your weight 121.3lbs.
# Enter your weight:180
# Kilograms or Pounds? (k 0or L):L
#  your weight 81.6 kgs

# Enter your weight:180
# Kilograms or Pounds? (k 0or L):pizzas
# pizzas Enter Invalid  option....!