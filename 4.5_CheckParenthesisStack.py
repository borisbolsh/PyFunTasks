str = input("Enter string: ")
stack = []
flVerify = True

for i in str:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and i == ')':
            continue
        if br == '[' and i == ']':
            continue
        if br == '{' and i == '}':
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:
    print("Yes")
else:
    print("No")
