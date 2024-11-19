"""
Aksa Vinod
19-11-2024
"""
inventory =[
    ("Laptop", 5, 30000.00),
    ("Headphones", 15, 500.00),
    ("Mouse", 50,150.00),
    ("Keyboard", 20, 150.00),
    ("Monitor", 10, 300.00)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,price=item
    stock_value=quantity*price
    print(f"Item Name:{item_name},the total value is:{stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value= item_name
print(f"Highest stock value is {highest_stock_value}")
print(f"The item with highest stock value is {item_with_highest_stock_value}")

