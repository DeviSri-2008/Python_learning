import csv
students =[
    {"name":"amit","math":85,"science":90,"english":78},
     {"name":"priya","math":92,"science":88,"english":95},
    {"name":"raj","math":70,"science":75,"english":80},
    ]
for student in students:
    total = student["math"]+student["science"]+student["english"]
    student["Total"] = total
headers = ["name","math","science","english","Total"]
with open('marksheet.csv','w',newline = '')as file:
    writer=csv.DictWrite(file,fieldnames = headers)
    writer.writeheader()
    writer.writerows(students)
print("files created")
