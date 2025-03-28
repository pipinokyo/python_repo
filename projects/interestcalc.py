principle = 0
rate = 0
Time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Please enter a positive number for the principal amount.")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Please enter a positive number for the rate of interest.")

while Time <= 0:
    Time = int(input("Enter the time in years: "))
    if Time <= 0:
        print("Please enter a positive number for the time period.")

total = principle * (1 + rate / 100) ** Time
print(f"The total amount after {Time} years is: ${total:.2f}") # 2f is to format the output to 2 decimal places
