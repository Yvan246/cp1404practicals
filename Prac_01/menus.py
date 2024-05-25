"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task

    elif choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed

"""
name = input("Enter name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()

print("")
