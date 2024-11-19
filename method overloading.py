# class Test:
#     def my_method1(self):
#         print("Parent class my method1")
#
#     def my_method2(self):
#         print("Parent class my method2")
#
# class ChClass(Test):
#     def my_method1(self):
#         super().my_method1()
#         print("Child class my method1")
#
# chobj = ChClass()
# chobj.my_method1()

class Hotel:
    def veg(self):
        print(f" order vegtable rice")
    def nonveg(self):
        print("f order Briyani")
class  Starters(Hotel):
     def veg(self):
         super().veg()
         print("Staters Menu Please")
obj = Starters()
obj.veg()