
array = [1, 5, 9, 11, 15, 25, 31]


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print binary_search(array, 25)
print binary_search(array, 10)
