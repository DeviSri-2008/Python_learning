import csv
dict_data = [{"name":"alice","fruit":"apple","price":20},
             {"name":"bob","fruit":"olive","price":40}]
headers = ["name","fruit","price"]
with open('data.csv','w',newline='') as file:
    h = csv.DictWriter(file,fieldnames = headers)
    h.writeheader()
    h.writerows(dict_data)
print("file created")
