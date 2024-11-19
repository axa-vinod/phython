"""
Aksa Vinod
19-11-2024
"""
employee_detalis=[
    ("Aksa","software engineering",30000),
    ("Uthara","doctor",60000),
    ("Aish","engineering",50000),
    ("nandana","bba",25000)
]
specific_value=int(input("Enter your specific value"))
for employee in employee_detalis:
    name,department,salary=employee
    if salary>specific_value:
        print(f"The employee who got salary above specific value are {name}")
total_annual_payroll=salary*12
print(f"The total annual payroll expense for all employee is {total_annual_payroll}")