arr = [30, 10, 20, 40, 50]

n = len(arr)

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("After pass", i + 1, ":", arr)