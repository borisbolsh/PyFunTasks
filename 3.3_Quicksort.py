someArray = [2, 1, 5, 7, 3, 10, 4, 6, 11, 15, 8, 20, 9]


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(someArray))
