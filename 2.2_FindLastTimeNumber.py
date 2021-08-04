seq = [11, 22, 3, 44, 5, 29, 3, 5, 3, 6, 123]


def findlastx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans


print(findlastx(seq, 3))
print(findlastx(seq, 55))
