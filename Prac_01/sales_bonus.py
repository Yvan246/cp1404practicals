"""
a Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# sales = float(input("Enter sales: $"))
# if sales < 1000:
#     user_bonus = sales * 0.10
# else:
#     user_bonus = sales * 0.15
# print(f"Your bonus is, {user_bonus:.2f}")

"""
its a loop, so it repeatedly asks for the user's sales
 and prints the bonus until they enter a negative number.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        sales_bonus = sales * 0.10
        print("Your bonus is", sales_bonus)
    else:
        sales_bonus = sales * 0.15
        print("Your bonus is", sales_bonus)
    sales = float(input("Enter sales: $"))
print("You must enter a positive value")
