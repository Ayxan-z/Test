import time

start = time.time()

cnt = 0
for i in range(100000000):
    cnt += i

stop = time.time()
print(cnt, stop-start)