def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero")
        result /= num
    return result

while True: 
    print("\n===== CALCULATOR MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Select an operation (1-5) : ")
    if choice in ['1','2','3','4']:
        try:
            numbers = list(map(float, input("Enter numbers separated by space: ").split()))
            if choice == '1':
                print("Result : ", add(numbers))
            elif choice == '2':
                print("Result : ", subtract(numbers))
            elif choice == '3':
                print("Result : ", multiply(numbers))
            elif choice == '4':
                print("Result : ", divide(numbers))

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid operation.")