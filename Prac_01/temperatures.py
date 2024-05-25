"""
CP1404 - Practical
display MENU
get choice
while choice != Quit option
    if choice == C
        get celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        display result
    elif choice == f
        get fahrenheit
        celsius= 5 / 9 * fahrenheit - 32
        display result
    else:
    print Invalid option
display menu
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":

        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
