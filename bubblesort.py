def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = list(map(int, input("Enter numbers separated by space: ").split()))


bubble(arr)


print("Sorted Array:", arr)
