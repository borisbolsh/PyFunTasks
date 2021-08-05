def findSmallerst(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallerst(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([6, 4, 5, 1, 2, 12, 14]))
