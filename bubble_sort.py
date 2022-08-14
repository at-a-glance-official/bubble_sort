def bubble_sort(arr):
    count = 0
    while count < len(arr):
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]

        count += 1
    return arr

arr = [10,12,11,-21,100,329090,-237734]
print(bubble_sort(arr))