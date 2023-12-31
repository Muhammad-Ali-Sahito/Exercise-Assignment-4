def calculate_square_sum_if_odd(num1, num2):
    if num1 % 2 == 1 and num2 % 2 == 1:  # Check if both numbers are odd
        sum_of_squares = num1**2 + num2**2
        print(f"The sum of the squares of {num1} and {num2} is: {sum_of_squares}")
    else:
        print("Calculation not performed. Please enter two odd numbers.")

# Get input from the user
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    # Call the function with the input values
    calculate_square_sum_if_odd(num1, num2)

except ValueError:
    print("Please enter valid integers.")
