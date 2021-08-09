list1 = [7, 5, -8, 9, 6, 3, 10, 1]


def bubbleSort(list1):
    for i in range(0, len(list1)-1):
        for j in range(0, len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1


print(bubbleSort(list1))
