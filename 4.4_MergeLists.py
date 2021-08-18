arrayOne = [-1, 1, 4, 8, 10, 11]
arraySec = [2, 2, 3, 3, 4, 8, 15, 19]
arrayThe = []

N = len(arrayOne)
M = len(arraySec)

i = 0
j = 0

while i < N and j < M:
    if arrayOne[i] <= arraySec[j]:
        arrayThe.append(arrayOne[i])
        i += 1
    else:
        arrayThe.append(arraySec[j])
        j += 1

arrayThe += arrayOne[i:] + arraySec[j:]

print(arrayThe)
