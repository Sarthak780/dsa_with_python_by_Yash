from collections import deque
queue2=deque(["amar",'akbar',"anthony"])
queue2.append("yash")
queue2.append("yashu")
queue2.append("yashv")
queue2.append("yashw")
queue2.append("yashx")
queue2.append("yashy")

print(queue2)
queue2.popleft()
queue2.popleft()
queue2.popleft()

print(queue2)


