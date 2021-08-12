import collections

queue = collections.deque()

queue.append(5)
queue.append(15)
queue.append(20)
queue.popleft()

for i in queue:
    print(i)
