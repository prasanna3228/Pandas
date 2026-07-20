import pandas as pd
Sheet1=pd.DataFrame({
    'ID':[1,2,3,4],
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,30,35,40]
})
Sheet2 =pd.DataFrame({
    'ID':[3,4,5,6],
    'City':['New York','Los Angeles','Chicago','Houston'],
    'Salary':[50000,60000,70000,80000]
})

# Merging_Two_Sheets = pd.merge(Sheet1,Sheet2) 
Merging_Two_Sheets = pd.merge(Sheet1,Sheet2,on="ID",how="outer") # outer join
Merging_Two_Sheets = pd.merge(Sheet1,Sheet2,on="ID",how="inner") # inner join
Merging_Two_Sheets_left = pd.merge(Sheet1,Sheet2,on="ID",how="left") # left join
Merging_Two_Sheets_right = pd.merge(Sheet1,Sheet2,on="ID",how="right") # right   join



print(Merging_Two_Sheets_left)