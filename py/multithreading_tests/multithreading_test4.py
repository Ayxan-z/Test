import threading
import time
from collections import Counter
import concurrent.futures

with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou_sorted.txt", 'r', encoding='utf-8', errors='ignore') as f:
    passwords = f.readlines()

password_per_thread = 10008
passwords = [i[:-1] for i in passwords[:password_per_thread]]
passwords_sorted = sorted(passwords, key=len)
passwords_counted = Counter(passwords_sorted).most_common()
passwords_dict = dict(passwords_counted)
passwords_sorted_list = [i[0] for i in passwords_counted]
threads_count = 7
x = int(password_per_thread / threads_count)


def passwordPossibility(passwords):
    global passwords_dict
    
    for i, password in enumerate(passwords):
        # print(password)
        cnt = 0
        for j in passwords_sorted_list[i+1:]:
            if password in j:
                cnt += 1

        passwords_dict[password] += cnt


if __name__ == '__main__':

    start = time.time()

    cnt = 0
    threads = []

    for tn in range(threads_count):
        # print(cnt, cnt+x)
        th = threading.Thread(target=passwordPossibility, args=(passwords_sorted_list[cnt:cnt+x],))
        threads.append(th)
        th.start()
        cnt += x

    for t in threads: t.join()

    stop = time.time()

    print(stop-start)

    with open("C:\\Users\\shahs\\Documents\\test\\data\\test.txt", 'w', encoding='utf-8') as f: 
        for key, value in passwords_dict.items(): 
            f.write('%s-%s\n' % (key, value))