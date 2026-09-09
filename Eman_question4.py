# Question 4: Exponentiation
# Write a python program that takes two numbers as input and calculates the first number raised to the power of the second number (exponentiation).

def main():
    base = float(input("Enter the first number (base): "))
    power = float(input("Enter the second number (exponent): "))

    result = base ** power
    print(f"{base} raised to the power of {power} is {result}")


if __name__ == "__main__":
    main()
