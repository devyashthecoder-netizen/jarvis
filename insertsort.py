arr = [10, 20, 30, 40, 50]

key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Element not found")