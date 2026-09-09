# Question 2: Gross Pay Calculation
# Write a python program that takes hours worked and hourly rate as an input from the user, then calculates and displays the gross pay.

def main():
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))

    gross_pay = hours * rate
    print(f"Gross Pay: {gross_pay:.2f}")


if __name__ == "__main__":
    main()
