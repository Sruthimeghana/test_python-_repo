opertor = input("Enter an  opertor(+ ,_, *, /):")
num1 = float(input("Enter a 1 st number:"))
num2 = float(input("Enter a  2 nd number:"))
if opertor == '+':
     result= num1 +num2
     print(round(result,3))
elif opertor == '-':
     result= num1 -num2
     print(round(result, 3))
elif opertor == '*':
     result = num1 * num2
     print(round(result, 3))
elif opertor == '/':
     result= num1 /num2
     print(round(result, 3))
else:
    print("Enter invalid Opertor .....")

# output:
# Enter an  opertor(+ ,_, *, /):+
# Enter a 1 st number:45
# Enter a  2 nd number:999
# 1044.0

# Enter an  opertor(+ ,_, *, /):-
# Enter a 1 st number:440
# Enter a  2 nd number:4200
# -3760.0
#
# Process finished with exit code 0



# Enter an  opertor(+ ,_, *, /):*
# Enter a 1 st number:345
# Enter a  2 nd number:56
# 19320.0
#
# Process finished with exit code 0
# Enter an  opertor(+ ,_, *, /):/
# Enter a 1 st number:450
# Enter a  2 nd number:330
# 1.364
# Enter an  opertor(+ ,_, *, /):pizza
# Enter a 1 st number:55
# Enter a  2 nd number:77
# Enter invalid Opertor .....