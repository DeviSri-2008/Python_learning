def fun(task,data):
    if task == "add":
        return sum(data)
    elif task == "reverse":
        return data[::-1]
    else:
        return "unknown task"
print(fun("add",[1,2,3]))
print(fun("reverse","hello"))
