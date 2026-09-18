# 0 0 0 5
# 1 0 0 3
# 2 7 0 0

# matrix = [
#     [0,0,5],
#     [0,0,0],
#     [3,0,0]
# ]

# print("Spare Matrix")

# for row in matrix:
#     print(row)

# print("\nNon - zero elements: ")

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] !=0:
#             print("Row: ",i,"column: ",j,"Value: ",matrix[i][j])


arr = [5,2,4,1]
n = len(arr)
for i in range(n):
    for j in range(0,n-i-1):
       if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1],arr[j]

print("Sorted array:",arr)