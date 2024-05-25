"""
First Demos for CP1404
"""
# name = input("What is your name? ")
# print("Hello ", name)

"""
Cost_per_year = 12 
Get monthly_cost
Calculate = Cost_per_year  * monthly_cost
Print calculate

"""
# cost_per_year = 12
# monthly_cost = float(input("TV streaming Monthly Cost service?  "))
# calculate = cost_per_year * monthly_cost
# # print(f"yearly total is , ${calculate:.2f}")
# print("yearly total is ${}".format(calculate))


"""Python Code to Calculate users pay
get tax rate 
get gross Pay 
Tax amount = gross pay * tax rate
net pay = gross pay - tax amount
print net pay
"""
# tax_rate = float(input("Enter tax rate (e.g. 0.3 is 30%): "))
# gross_pay = float(input("Whats the gross pay: "))
# tax_amount = tax_rate * gross_pay
# net_pay = gross_pay - tax_amount
# print(f"Your net pay after tax deducting is: ${net_pay:.2f}")


""" for loop example
"""
# # this will print a list
# for subject in ["1401", "cp1404", "cp2406"]:
#     print("I like", subject)
#
# # this will print a row
# for number in [2, 4, -8, 99]:
#     print(number, end="")
#
# for character in "Python":
#     print(character, end="_")

"""
  get number of age
  for n in [number of age]:
  get  
"""
# total_age = 0
# number_of_age = int(input("Enter number of age: "))
# for n in range(number_of_age):
#     age = int(input("Enter age: "))
#     total_age += age
# print(total_age)

"""
Nested Loops
"""
# for i in range(3):
#     for j in range(4):
#         print(i, "_", j)

# for round_number in range(1, 4):
#     for name in ["Miles", "Ella", "Chet"]:
#         print("round", round_number, "_", name)
#     print("_______________")

"""
Test the program 
"""
total_age = 0
number_of_people = 0
age = int(input("Age: "))
while age > 0:
    total_age = total_age + 1
    number_of_people += 1
    age = int(input("Age:"))
if number_of_people == 0:
    print("No total or average")
else:
    average = total_age / number_of_people
    print(f"Average age of {number_of_people} people is {average}")
