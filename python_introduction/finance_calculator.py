
income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

income = float(income)
monthly_expenses = float(monthly_expenses)

monthly_savings = income - monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${round(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${round(projected_savings)}.")
