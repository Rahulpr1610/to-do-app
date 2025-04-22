wating_list = ["ben","san","john"]
wating_list.sort()

for index,item in enumerate (wating_list):
    row=f"{index+5}.{item.capitalize()}"
    print(row)