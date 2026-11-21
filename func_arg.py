def calculate_salary(basic_salary,bonus = 2000):
    Total_Salary = basic_salary + bonus
    return Total_Salary

#Positional Arguments  
print("Employee 1 Salary: ",  calculate_salary(30000))
#keyword Arguments
print("Employee 2 Salary: ",   calculate_salary(basic_salary = 33000,bonus = 2000))
#Default Argument
print("Employee 3 Salary: ",calculate_salary(25000))
    
    
    
    




    