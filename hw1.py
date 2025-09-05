data_tuple = (23, 77.7, "Data", ["data", 100, 5, "hello"], {"name": "Viktoria"}, -301)  # O(1)
print("Элементы:")  # O(1)
for i in range(len(data_tuple)):    # O(N) где N = 6 раз
    a = data_tuple[i]   # O(1)
    if type(a) == int or type(a) == float:  # O(1)
        print(a)    # O(1)

# Линейная сложность O(N)
