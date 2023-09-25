# Constants
TAX_RATE = 18  # 18% tax rate

# Input from the user
hours_worked = input("Enter the hours worked in a week: ")
hourly_rate = input("Enter the hourly pay rate: ")

# Convert input strings to floats
hours_worked = float(hours_worked)
hourly_rate = float(hourly_rate)

# Calculate Gross Pay
gross_pay = round(hours_worked * hourly_rate, 2)

# Calculate Taxes to be withheld
tax_amount = round(gross_pay * (TAX_RATE / 100), 2)

# Calculate Take Home Pay
take_home_pay = round(gross_pay - tax_amount, 2)

# Display the results
print(f"Gross Pay: ${gross_pay}")
print(f"Taxes to be withheld: ${tax_amount}")
print(f"Take Home Pay: ${take_home_pay}")
