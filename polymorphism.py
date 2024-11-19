# class Office:
#     def person(self):
#         print("In office behaviour is different..")
#
# class Friends:
#
#     def person3(self):
#         print("In Friends meet behaviour is different..")
#
# class Home:
#
#     def person(self):
#         print("In home behaviour is different..")
#
# def fmain(tobj):
#     tobj.person()
#
# class_list = [Office(), Friends(), Home()]
#
# for obj in class_list:
#     fmain(obj)

# ofObj = Office()
# fmain(ofObj)
#
# frobj = Friends()
# fmain(frobj)

# hasattr(obj,'attributename')

# class Office:
#     def person(self):
#         print("In office behaviour is different..")
#
# class Friends:
#
#     def person3(self):
#         print("In Friends meet behaviour is different..")
#
# class Home:
#
#     def person(self):
#         print("In home behaviour is different..")
#
# def fmain(tobj):
#     if hasattr(tobj, 'person'):
#         tobj.person()
#     elif hasattr(tobj, 'person3'):
#         tobj.person3()
#
# class_list = [Office(), Friends(), Home()]
#
# for obj in class_list:
#     fmain(obj)


# class Developer:
#      def person(self):
#          print("Developer person  develop the code:")
# class Desiging:
#      def person(self):
#          print("Interface a Code ")
# class Manager:
#      def person(self):
#          print("managing the team")
# def fmain(tobj):
#     tobj.person()
# list=[Developer(),Desiging(),Manager()]
# for obj in list:
#    fmain(obj)


   # class Person:
   #     def __init__(self, name, age):
   #         self.name = name
   #         self.age = age


   # person = Person("Alice", 30)
   #
   # # Check if the person object has a 'name' attribute
   # if hasattr(person, 'name'):
   #     print("Person has the 'name' attribute.")
   # else:
   #     print("Person does not have the 'name' attribute.")
   #
   # # Check if the person object has a 'height' attribute
   # if hasattr(person, 'height'):
   #     print("Person has the 'height' attribute.")
   # else:
   #     print("Person does not have the 'height' attribute.")

# class Person:
#      def __init__(self, name,age):
#            self.name = name
#            self.age = age
# person = Person("alice",30)
# if hasattr(person,'name'):
#     print("Person name having in list ")
# else :
#     print("person name not having in list")
# if hasattr(person ,'age'):
#     print("person age having in the list")
# else:
#     print("person age not having in the list")
# if hasattr(person,'height'):
#     print("person height having in the list")
# else:
#     print("person  height not having in the list")

class CreditCardPayment:
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment:
    def pay(self, amount):
        print(f"Processing bank transfer payment of ${amount}")

def process_payment(payment_method, amount):
    payment_method.pay(amount)
# # Using different payment methods
process_payment(CreditCardPayment(), 50)   # Credit card payment
process_payment(PayPalPayment(), 75)       # PayPal payment
process_payment(BankTransferPayment(), 100)  # Bank transfer payment
