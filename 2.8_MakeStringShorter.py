someString = "AAAABBBCCCDDZZZYYYYYYYYYAAAAABBBBBBBBBBBBBBBBCCCCDDDAAAAASSSSSSSS"


def rle(someString):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = someString[0]
    lastpos = 0
    ans = []
    for i in range(len(someString)):
        if someString[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = someString[i]
    ans.append(pack(someString[lastpos], len(someString) - lastpos))
    return ''.join(ans)


print(rle(someString))


# def shortersomeStringing(someString):
#     lastsym = someString[0]
#     ans = []
#     for i in range(len(someString)):
#         if someString[i] != lastsym:
#             ans.append(lastsym)
#             lastsym = someString[i]
#     ans.append(lastsym)
#     return ''.join(ans)


# print(shortersomeStringing(someString))
