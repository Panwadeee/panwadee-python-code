"""
Personal Finance Calculator
Student: Pannawadee Jongpadklang
Date: 2025-07-24
Purpose: Calculate monthly budget and savings
"""

# รับข้อมูล
monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your monthly rent (THB): "))
food_budget = int(input("Enter your monthly food budget (THB): "))
transportation_cost = float(input("Enter your monthly transportation cost (THB): "))
entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))
emergency_percent = float(input("Enter percentage for emergency fund (e.g., 10.0): "))
investment_percent = float(input("Enter percentage for investment (e.g., 15.0): "))

# คำนวณ
fixed_expenses = rent_cost + transportation_cost
variable_expenses = food_budget + entertainment_budget
total_expenses = fixed_expenses + variable_expenses

emergency_fund = monthly_income * (emergency_percent / 100)
investment = monthly_income * (investment_percent / 100)
savings = monthly_income - (total_expenses + emergency_fund + investment)
expense_ratio = (total_expenses / monthly_income) * 100
remaining_income = monthly_income - total_expenses

# แสดงผล
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"{'Income:':25s} {monthly_income:10.2f} THB")
print(f"{'Fixed Expenses:':25s} {fixed_expenses:10.2f} THB")
print(f"{'Variable Expenses:':25s} {variable_expenses:10.2f} THB")
print(f"{'Total Expenses:':25s} {total_expenses:10.2f} THB")
print(f"{'Remaining:':25s} {remaining_income:10.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"{f'Emergency Fund ({emergency_percent:.0f}%):':25s} {emergency_fund:10.2f} THB")
print(f"{f'Investment ({investment_percent:.0f}%):':25s} {investment:10.2f} THB")
print(f"{'Available for Savings:':25s} {savings:10.2f} THB")

print("\n=== ANALYSIS ===")
print(f"{'Expense Ratio:':25s} {expense_ratio:10.2f}%")