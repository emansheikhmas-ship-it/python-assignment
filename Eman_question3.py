# Question 3: Temperature Conversion
# Write a pyhton program that takes tempurature in Celsius as input from the user and converts it to Fahrenheit.

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} C is equal to {fahrenheit} F")


if __name__ == "__main__":
    main()
