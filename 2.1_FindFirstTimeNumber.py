seq = [11, 22, 3, 44, 5, 29, 6]


def findx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


print(findx(seq, 3))
print(findx(seq, 55))
