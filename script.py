# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Get user input for the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
result = add_numbers(num1, num2)

# Print the result
print(f"The sum of {num1} and {num2} is {result}")
