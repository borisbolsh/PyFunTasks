seq = list(map(int, input().split()))
seqmax = 0

if len(seq) == 0:
    print('-inf')
else:
    seqmax = seq[0]
    for i in range(len(seq)):
        if seq[i] > seqmax:
            seqmax = seq[i]
    print(seqmax)
