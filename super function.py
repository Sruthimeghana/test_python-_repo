# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def display_emp(self):
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)
#
# class Manager(Employee):
#     def __init__(self, name, salary, departement):
#         super().__init__(name, salary)
#         self.department = departement
#
#     def display_emp(self):
#         super().display_emp()
#         print("Department:", self.department)
#
# emp1=Manager("Ajay kumar", 45000, "Pipeline TD")
# emp1.display_emp()


# class Student:
#      def __init__(self,name,phone_number):
#          self.name = name
#          self.phone_number = phone_number
#      def display_emp(self):
#          print("Employee Name:" ,self.name)
#          print("Employee phone_number:",self.phone_number)
# class Manager(Student):
#     def __init__(self,name,phone_number,course):
#         super().__init__(name,phone_number)
#         self.course = course
#     def display_emp(self):
#         super().display_emp()
#         print("Employee phone_number:", self.course)
#
#
# college = Manager("sruthi",9699996768,"msc computerscience")
# college.display_emp()
# output:
# C:\Users\user\Desktop\pythonfiles\.venv\Scripts\python.exe "C:\Users\user\Desktop\pythonfiles\test_python-_repo\super function.py"
# Employee Name: sruthi
# Employee phone_number: 9699996768
# Employee phone_number: msc computerscience
#