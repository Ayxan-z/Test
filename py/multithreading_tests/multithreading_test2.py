from collections import Counter
import time


with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou.txt", 'r', encoding='utf-8', errors='ignore') as f:
    passwords = f.readlines()

passwords = [i[:-1] for i in passwords]

start = time.time()

s = []

for i in passwords:
    for j in i:
        s.append(j)
        
s_count = Counter(s).most_common()

for i, j in enumerate(s_count):
    x = j[0]
    cnt = 0
    for k in passwords:
        if x in k:
            cnt += 1
    s_count[i] += (cnt,)
    print(i)

with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou_data.txt", 'w', encoding='utf-8') as f:
    for i in s_count: 
        f.write(f'{i[0]}-{i[1]}-{i[2]}\n')
        
stop = time.time()
print(stop-start)