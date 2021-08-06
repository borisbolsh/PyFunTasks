words = ["aaa", "bb", "top", "xxx", "a", "sport", "lot",
         "mazda", "kia", "car", "jet", "zero", "z", "road", "nissan"]


def findShortestWords(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(word)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)


print(findShortestWords(words))
