import time
from multiprocessing import Pool
from collections import Counter


def passwordPossibility(password, passwords_sorted_list):
    cnt = 0
    for j in passwords_sorted_list:
        if password in j:
            cnt += 1
            
    return (password, cnt)

# def result(val): return val

if __name__ == "__main__":

    with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou_sort.txt", 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.readlines()
    
    passwords = [i[:-1] for i in passwords[:20000]]
    passwords_sorted = sorted(passwords, key=len)
    passwords_counted = Counter(passwords_sorted).most_common()
    passwords_dict = dict(passwords_counted)
    passwords_sorted_list = [i[0] for i in passwords_counted]

    start = time.time()
    
    # with Pool(7) as pool:
    #     x = pool.starmap_async(passwordPossibility,
    #     [(password, passwords_sorted_list[i+1:]) for i, password in enumerate(passwords_sorted_list)],
    #                                     callback=result).get()

    # ===========================================================================================
    
    with Pool(7) as pool:
        passwords_count = pool.starmap(passwordPossibility,
        [(password, passwords_sorted_list[i+1:]) for i, password in enumerate(passwords_sorted_list)])
    
    for password, cnt in passwords_count:
        passwords_dict[password] += cnt

    # ===========================================================================================

    # with Pool(7) as pool:
    #     for i, password in enumerate(passwords_sorted_list):
    #         cnt = pool.apply(passwordPossibility, args=(password, passwords_sorted_list[i+1:]))
    #         passwords_dict[password] += cnt
    
    stop = time.time()
    
    print(stop-start)
    # print(passwords_dict)