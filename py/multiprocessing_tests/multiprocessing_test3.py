import time
from multiprocessing import Pool, Manager, Process, Queue
from collections import Counter


# def passwordPossibility(passwords):
#     l = []
#     for i, p in enumerate(passwords):
#         cnt = 0
#         for j in passwords[i+1:]:
#             if p in j:
#                 cnt += 1

#         l.append((p, cnt))
#     return l

def passwordPossibility(password, passwords_sorted_list):
    cnt = 0
    for j in passwords_sorted_list:
        if password in j:
            cnt += 1

    return (password, cnt)

# def passwordPossibility(password, passwords_sorted_list, q):
#     cnt = 0
#     for j in passwords_sorted_list:
#         if password in j:
#             cnt += 1

#     q.put((password, cnt))

def result(val): return val

if __name__ == "__main__":

    with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou_sorted.txt", 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.readlines()

    passwords = [i[:-1] for i in passwords[:1000]]
    passwords_sorted = sorted(passwords, key=len)
    passwords_counted = Counter(passwords_sorted).most_common()
    passwords_dict = dict(passwords_counted)
    passwords_sorted_list = [i[0] for i in passwords_counted]

    # manager = Manager()
    # l = manager.list()

    start = time.time()

    # processes = []
    # cnt = 1
    # q = Queue()
    # for j, p in enumerate(passwords_sorted_list):
    #     p = Process(target=passwordPossibility, args=(p, passwords_sorted_list[j+1:], q))
    #     processes.append(p)
    #     p.start()
    #     cnt += 1

    #     if cnt % 7 == 0:
    #         for p in processes:
    #             p.join()
    #         processes = []

    # for p in processes:
    #     p.join()

    # with Pool(7) as pool:
    #     x = pool.starmap(passwordPossibility, [(passwords_sorted_list,)])

    # ===========================================================================================

    # with Pool(7) as pool:
    #     x = pool.starmap_async(passwordPossibility,
    #     [(password, passwords_sorted_list[i+1:]) for i, password in enumerate(passwords_sorted_list)],
    #                                     callback=result).get()

    # ===========================================================================================

    with Pool(7) as pool:
        passwords_count = pool.starmap(passwordPossibility,
        [(password, passwords_sorted_list[i+1:]) for i, password in enumerate(passwords_sorted_list)])

    # for password, cnt in passwords_count:
    #     passwords_dict[password] += cnt

    # ===========================================================================================

    # with Pool(7) as pool:
    #     for i, password in enumerate(passwords_sorted_list):
    #         cnt = pool.apply(passwordPossibility, args=(password, passwords_sorted_list[i+1:]))
    #         passwords_dict[password] += cnt

    stop = time.time()

    print(stop-start)
    # while not q.empty():
    #     print(q.get())