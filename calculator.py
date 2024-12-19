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


# Simple Multiplication Calculator with a Function
def multiply(num1, num2):
    """
    Function to multiply two numbers.
    """
    return num1 * num2

def multiplication_calculator():
    print("Welcome to the Multiplication Calculator!")
    
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Call the multiply function
        result = multiply(num1, num2)
        
        # Display the result
        print(f"The result of multiplying {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
multiplication_calculator()
