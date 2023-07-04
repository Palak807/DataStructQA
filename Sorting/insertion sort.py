def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while temp < arr[j] and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

arr = [1,6,7,2,3]
print(insertionSort(arr))