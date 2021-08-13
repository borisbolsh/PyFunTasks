setsize = 10
myset = [[] for _ in range(setsize)]


def add(x):
    if not find(x):
        myset[x % setsize].append(x)


def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return


add(1)
add(5)
add(10)
add(2)
add(3)
add(4)
add(333)
add(100)

print(myset)  # [[10, 100], [1], [2], [3, 333], [4], [5], [], [], [], []]

delete(333)
print(myset)  # [[10, 100], [1], [2], [3], [4], [5], [], [], [], []]

print(find(100))  # True
