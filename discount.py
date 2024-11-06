class Product:
    def __init__(self, productname, price):
        self.productname = productname
        self.price = price

    def getprice(self):
        print("Original price:", self.price)

class DiscountProduct(Product):
    def __init__(self, productname, price, discount):
        # Corrected the constructor name
        super().__init__(productname, price)
        self.discount = discount

    def getprice(self):
        # Calculate the discounted price
        discount_price = self.price * (1 - self.discount)
        print(f"Discounted price: {discount_price:.2f}")

# Example usage
obj = DiscountProduct("Chocolate", 2000, 0.3)  # 30% discount
obj.getprice()







