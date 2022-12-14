import collections

free_apps_list = []

new_price_list = []

cnt = Counter ()

for app in list_of_csv[1:]:

    name = app [0]
    price = app [7]   
    new_price_value = price.replace ("$", "")
    
    if new_price_value != '0':
    
        new_price_list.append (name)
        new_price_list.append (new_price_value)
    
#print(Counter (new_price_list))
print (new_price_list)

for i in new_price_list:
    csv_file.append(new_price_list)