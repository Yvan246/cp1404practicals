"""
The program allows the user to enter the number of items and the price of each different item.
Then the program displays the total price of those items.
If the total price is over $100, then a 10% discount is applied
If the number of items is less than zero, the message "Invalid number of items!"
quantity must be re-entered by the user until it is valid
"""

total_price = 0

number_of_items = int(input("Number of Items: "))

while number_of_items <= 0:
    print("You must inter a valid Item")
    number_of_items = int(input("Number of Items: "))

for item in range(number_of_items):
    item_price = float(input("price of Item: "))
    total_price += item_price

if total_price >= 100:
    discount = total_price * 0.10
    total_price -= discount
print(f"Total price for {number_of_items} items is:  {total_price:.2f}")
