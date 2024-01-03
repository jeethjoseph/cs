starting_annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000 
semi_annual_raise = .07
invenstment_annual_return_rate = 0.04
investment_monthly_return_rate = invenstment_annual_return_rate/12


portion_down_payment =  0.25 * total_cost
max_month_count = 36
low_portion_saved = 0
high_portion_saved = 1
current_savings = 0
while (abs(current_savings - portion_down_payment)) > 100:
    portion_saved = (low_portion_saved + high_portion_saved)/2.0
    current_savings  = 0
    print(portion_saved)
    for month in range(1,37):
        annual_salary = starting_annual_salary
        monthly_salary = annual_salary/12
        monthly_invenstment = monthly_salary*portion_saved
        current_savings = current_savings + monthly_invenstment
        + current_savings*investment_monthly_return_rate
        if(month % 6 == 0):
            annual_salary = annual_salary + annual_salary*semi_annual_raise

    if (current_savings > portion_down_payment):
        high_portion_saved = portion_saved
        print("Changed High")
    else:
        low_portion_saved = portion_saved
        print("Changed low")
    print(current_savings)
    

print("Best saving rate :", portion_saved)
