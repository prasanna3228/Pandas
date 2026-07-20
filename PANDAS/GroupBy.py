import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'HR', 'IT', 'HR', 'Sales'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Salary': [50000, 40000, 60000, 45000, 55000]
})

# Group by 'Department' and calculate the mean salary

# print(df.groupby('Department')['Salary'].sum()) # Groups the DataFrame by the 'Department' column and calculates the sum of the 'Salary' column for each group
# print(df.groupby('Department').count()) # Groups the DataFrame by the 'Department' column and calculates the count of rows for each group

print(df.groupby('Department').agg(
    
        Total_salary= ('Salary', 'sum') ,
        Average_salary= ('Salary', 'mean'),
        employee_count= ('Employee', 'count'),
        Maximum_salary=('Salary','max')
))



