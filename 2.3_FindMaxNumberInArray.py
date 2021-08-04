seq = [11, 22, 3, 44, 5, 29, 3, 5, 3, 6, 123, 99, 21, 100, 54]


def findmax(seq):
    ans = seq[0]
    for i in range(len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans


print(findmax(seq))
