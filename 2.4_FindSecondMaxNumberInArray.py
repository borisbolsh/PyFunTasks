seq = [11, 22, 3, 44, 5, 29, 3, 5, 3, 6, 123, 99, 21, 100, 54]


def findSecondMax(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return (max1, max2)


print(findSecondMax(seq))
