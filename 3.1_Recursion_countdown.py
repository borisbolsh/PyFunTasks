def countdown(i):
    print(i)
    if i <= 1:
        return i
    else:
        countdown(i - 1)


countdown(5)
