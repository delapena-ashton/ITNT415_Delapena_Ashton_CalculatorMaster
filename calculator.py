# Developer: Ashton Ivan Guevarra Delapena
# ITNT415 Midterm Summative Assessment

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Error: Invalid input! Please enter numeric values.")

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def main():
    while True:
        print("\n--- Python Calculator Menu ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice in ['1', '2', '3', '4']:
            print("\n")
            num1, num2 = get_numbers()
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {addition(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == '4':
                result = division(num1, num2)
                if "Error" in str(result):
                    print(result)
                else:
                    print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Invalid input handling! Please select 1-5.")

if __name__ == "__main__":
    main()
