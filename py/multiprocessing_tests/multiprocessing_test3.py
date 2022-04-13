import time
from multiprocessing import Pool, Manager, Process, Queue
from collections import Counter


def passwordPossibility(password, password_list):
    print(password)
    cnt = 0
    for j in password_list:
        if password in j:
            cnt += 1

    return cnt

if __name__ == "__main__":

    with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou.txt", 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.readlines()

    x = 10000
    passwords = [i[:-1] for i in passwords[:x]]
    passwords_sorted = sorted(passwords, key=len)
    # passwords_counted = Counter(passwords_sorted).most_common()
    # passwords_dict = dict(passwords_counted)
    # passwords_sorted_list = [i[0] for i in passwords_counted]

    start = time.time()

    threads_count = 7
    y = x // threads_count
    for i, password in enumerate(passwords_sorted):
        data = []
        for j in range(threads_count - 1):
            data.append((password, passwords_sorted[y*j:y*(j+1)]))
    
        data.append((password, passwords_sorted[y*(j+1):]))

        with Pool(threads_count) as pool:
            passwords_count = pool.starmap(passwordPossibility, data)
        break

    stop = time.time()
    print(passwords_count)
    print(stop-start)
    # while not q.empty():
    #     print(q.get())