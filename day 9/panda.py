import pandas as pd
data = {
    "name":["A","B","C","D","E","F","G","H"],
    "Age":[25,30,35,12,40,24,32,20],
    "Score":[85,60,95,56,78,9,6,90]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("students1.csv",index=False)
print("\nSaved to students.csv")
 
