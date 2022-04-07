from collections import Counter
import time


with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou_sort.txt", 'r', encoding='utf-8', errors='ignore') as f:
    passwords = f.readlines()

passwords = [i[:-1] for i in passwords[:20000]]
passwords_sorted = sorted(passwords, key=len)
passwords_counted = Counter(passwords_sorted).most_common()
passwords_dict = dict(passwords_counted)
passwords_sorted_list = [i[0] for i in passwords_counted]

def passwordPossibility(i, password):
    global passwords_dict, passwords_sorted_list

    for j in passwords_sorted_list[i+1:]:
        if password in j:
            passwords_dict[password] += 1

start = time.time()
for i, password in enumerate(passwords_sorted_list):
    passwordPossibility(i, password)
stop = time.time()

print(stop-start)
# print(passwords_dict)