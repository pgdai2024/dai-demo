# Simple Addition Calculator
def addition_calculator():
    print("Welcome to the Addition Calculator!")
    
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform addition
        result = num1 + num2
        
        # Display the result
        print(f"The result of adding {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
addition_calculator()
