def segregate0and1(arr, size):

    mapper = {0: 0, 1: 0}

    for i in arr:
        mapper[i] += 1

    count_0 = mapper[0]

    for i in range(count_0):
        arr[i] = 0

    for i in range(count_0, size):
        arr[i] = 1

    return arr

arr = [0, 1, 0, 1, 1, 1]
arr_size = len(arr)
print("Array after segregation")
print(segregate0and1(arr, arr_size))
