
array = [-3, 5, 0, -8, 99, 21, 2, 1, 10]
N = len(array)

for i in range(1, N):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
