seq = [11, 22, 3, 44, 5, 29, 3, 5, 3, 6, 123, 99, 21, 100, 54]


def findMinEven(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
            ans = seq[i]
    return ans


print(findMinEven(seq))


def findMinEven2(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return flag


print(findMinEven2(seq))
