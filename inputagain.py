def add_numbers():
    num1 = int(input("Enter the first number to add: "))
    num2 = int(input("Enter the second number to add: "))
    print(f"The sum is: {num1 + num2}\n")

def multiply_numbers():
    num1 = int(input("Enter the first number to multiply: "))
    num2 = int(input("Enter the second number to multiply: "))
    print(f"The product is: {num1 * num2}\n")

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Nice to meet you!\n")

# Main program loop
while True:
    print("Choose an option:")
    print("1. Add numbers")
    print("2. Multiply numbers")
    print("3. Greet user")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_numbers()
    elif choice == '2':
        multiply_numbers()
    elif choice == '3':
        greet_user()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.\n")
