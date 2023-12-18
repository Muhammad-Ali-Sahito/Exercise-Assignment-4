def calculate_factorial(number):
    if number < 0:
        print("Factorial is undefined for negative numbers.")
        return
    
    factorial_result = 1
    while number > 1:
        factorial_result *= number
        number -= 1

    print(f"The factorial is: {factorial_result}")

# Get input from the user
try:
    input_number = int(input("Enter a number to calculate its factorial: "))
    
    # Call the function with the input value
    calculate_factorial(input_number)

except ValueError:
    print("Please enter a valid integer.")
