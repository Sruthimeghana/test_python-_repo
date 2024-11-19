import json
class Bill:
    def __init__(self,name,amount,due_date):
        self.name=name
        self.amount=amount
        self.due_date= due_date
    def __str__(self):
        return (f"{self.name:<20} {self.amount:<10} {self.due_date}")
class BillManager:
    BILL_FILE = 'bills.json'

    def __init__(self):
        self.bills = self.load_bills()

    def load_bills(self):
        try:
            with open(self.BILL_FILE, 'r') as file:
                bill_data = json.load(file)
                return [Bill(bill['name'], bill['amount'], bill['due_date']) for bill in bill_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading the bills: {e}")
            return []

    def save_bills(self):
        # The method is properly indented here.
        bill_data = [{"name": bill.name, "amount": bill.amount, "due_date": bill.due_date} for bill in self.bills]
        with open(self.BILL_FILE, 'w') as file:
            json.dump(bill_data, file, indent=4)
    def add_bill(self,bill):
         self.bills.append(bill)
         self.save_bills()
    def view_bills(self):
         if not self.bills:
             print("NO bills found:")
         else:
             print(f"{'Name:<20'}{'amount':<10}{'Due Date'}")
             print("-"*40)
         for bill in self.bills :
             print(bill)
    def delete_bill(self,name):
         self.bills =[bill for bill in self.bills if bill.name!=name]
         self.save_bills()
class BillManagementApp:
    def __init__(self):
         self.bill_manager = BillManager()
    def display_menu(self):
         print("\n=== Bill Management System===")
         print("1.Add a Bill")
         print("2. View All Bills")
         print("3.Delete a Bill")
         print("4.Exit")
         Choice = input("Enter Your Choice:")
         return Choice
    def add_bill(self):
        name = input("Enter bill name:")
        amount = float(input("Enter bill amount:"))
        due_date = input("Enter due date (YYYY-MM-DD):")
        bill = Bill(name,amount,due_date)
        self.bill_manager.add_bill(bill)
        print(f"Bill '{name}' added Sucessfully.")
    def delete_bill(self):
         name = input("Enter the bill name to delete:")
         self.bill_manager.delete_bill(name)
         print(f"Bill'{name}' Deleted Suceessfully.")
    def run(self):
         while True:
             Choice = self.display_menu()
             if Choice == "1":
                 self.add_bill()
             elif Choice == "2":
                 self.bill_manager.view_bills()
             elif Choice == "3":
                 self.delete_bill()
             elif Choice == "4":
                  print("exiting.....")
                  break
             else:
                  print("Invalid Choice ,Please try again.....")
if __name__ =="__main__":
    app = BillManagementApp()
    app.run()


