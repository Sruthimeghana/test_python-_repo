# class Product:
#     def __init__(self, productname, price):
#         self.productname = productname
#         self.price = price
#
#     def getprice(self):
#         originalPrice=4000
#         self.originalPrice
#         print(" self.originalPrice")
#
# class DiscountProduct(Product):
#     def __init__(self, productname, price, discount):
#         # Corrected the constructor name
#         super().__init__(productname, price)
#         self.discount = discount
#
#     def getprice(self):
#         super().originalPrice
#
# # Example usage
# obj = DiscountProduct("Chocolate", 2000, 0.3)  # 30% discount


# class Product:
#     def __init__(self, productname, price):
#         self.productname = productname
#         self.price = price  # Store the price in self.price
#
#     def getprice(self):
#         originalPrice = self.price  # Declare originalPrice within getprice method
#         print(f"Original Price: {originalPrice}")
#         return originalPrice
#
# class DiscountProduct(Product):
#     def __init__(self, productname, price, discount):
#         super().__init__(productname, price)  # Call parent constructor
#         self.discount = discount  # Discount for the product
#
#     def getprice(self):
#         originalPrice = super().getprice()  # Get original price from parent method
#         discounted_price = originalPrice * (1 - self.discount)  # Apply discount
#         print(f"Discounted price: {discounted_price}")

# Example usage:
# obj = DiscountProduct("Chocolate", 2000, 0.3)
# obj.getprice()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)  # Initialize name and price
        self.discount = discount

    def get_price(self):
        original_price = super().get_price()  # Call Product's get_price
        return original_price * (1 - self.discount / 100)


discounted_item = DiscountedProduct("Laptop", 1000, 10)
print(f"Price after discount: ${discounted_item.get_price():.2f}")

# output:
# Price after discount: $900.00




