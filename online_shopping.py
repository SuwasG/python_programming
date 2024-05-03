'''
Question: write the code for this question: Online Shopping Cart: Develop a Python program to simulate an online shopping cart system. Create classes for products, customers, and orders. Implement methods for adding items to the cart, calculating total order value, handling discounts and promotions, and generating invoices.
'''

class Product:
    def __init__(self, title, price):
        self.title=title 
        self.price=price

class Customer:
    def __init__(self, name, email):
        self.name=name
        self.email=email

class Order:
    def __init__(self, customer):
        self.customer=customer 
        self.items=[]

    def add_items(self, product, quantity=1):
        self.items.append((product, quantity))
    
    def calculate_total(self):
        total=0 
        for product, quantity in self.items:
            total+= product.price * quantity
        return total
    
    def generate_invoice(self):
        invoice =f"Invoice for {self.customer.name}\n"
        for product,quantity in self.items:
            invoice+=f"{product.title}: {product.price} X {quantity}\n"
        invoice+=f"Total: {self.calculate_total()}"
        return invoice

# create products
product1 = Product("Laptop", 1000)
product2 = Product("Phone", 500)

# Create customer
customer1 = Customer("Suwas", "suwas@gmail.com")
customer2 = Customer("Sagar", "sagar@gmail.com")

# create order
order1=Order(customer1)


# Add items to the cart
order1.add_items(product1, 2)
order1.add_items(product2)

# Calculate total order value
total = order1.calculate_total()
print("Total order value:", total)

# Generate invoice
invoice = order1.generate_invoice()
print("Invoice:")
print(invoice)


