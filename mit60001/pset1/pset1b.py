annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of annual salary saved in fractions: "))
total_cost = float(input("Wnter the total cost of the dream House :"))
semi_annual_raise = float(input("Enter the semi annual raise :"))


portion_down_payment =  0.25 * total_cost
current_savings  = 0
month_count = 0

while portion_down_payment > current_savings:
    monthly_saving = annual_salary/12*portion_saved
    monthly_returns = current_savings*0.04/12
    current_savings = current_savings + monthly_saving + monthly_returns
    month_count = month_count + 1
    if (month_count % 6 == 0):
        annual_salary = annual_salary + semi_annual_raise*annual_salary

print("Number of Months :", month_count)

    
