
array = [-3, 5, 0, -8, 99, 21, 2, 1, 10]
N = len(array)

for i in range(N-1):
    min = array[i]
    pIndex = i
    for j in range(i+1, N):
        if min > array[j]:
            min = array[j]
            pIndex = j

    if pIndex != i:
        temp = array[i]
        array[i] = array[pIndex]
        array[pIndex] = temp

print(array)
