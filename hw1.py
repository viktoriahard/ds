data_tuple = (23, 77.7, -301, "Data", ["data", 100, 5, "hello"], {"name": "Viktoria"})
print("Элементы:")
for i in range(6):
    a = data_tuple[i]
    if type(a) == int or type(a) == float:
        print(a)