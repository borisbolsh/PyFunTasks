# s = input("Enter any string: ")
s = "Llorem ipsum dollor sit amet, consectetur adipiscing ellit. Nullla ut ellit iacullis, ulltricies diam sit ametll, consecteturll magnall. Integer sodallles hendreritly orcil, nec pulllvinar orci euismod well."

dect = {}
ans = ''
anscnt = 0

for now in s:
    if now not in dect:
        dect[now] = 0
    dect[now] += 1
    if dect[now] > anscnt:
        anscnt = dect[now]
        ans = now

print("Most common character: %s (%d times)" % (ans, anscnt))
