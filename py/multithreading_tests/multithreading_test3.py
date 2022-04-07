import time
import threading
import os

v = {}
s = 5
az_alp = ['a','b','c','ç','d','e','ə','f','g','ğ','h','x','ı','i','j','k',
        'q','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
az_alp_upper = ['A','B','C','Ç','D','E','Ə','F','G','Ğ','H','X','I','İ',
                'J','K','Q','L','M','N','O','Ö','P','R','S','Ş','T','U',
                'Ü','V','Y','Z']

nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
        25,26,27,28,29,30,31,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,
        -21,-20,-19,-18,-17,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

def encrypt(text):
    global az_alp, az_alp_upper, nums, s

    result = ''

    for t in text:
        if t in az_alp:
            result += az_alp[nums[az_alp.index(t) + s]]

        elif t.upper() in az_alp_upper:
            result += az_alp_upper[nums[az_alp_upper.index(t) + s]]

        else:
            result += chr(ord(t) + 601 + s)

    return result

def forEncrypt(data: list[str], cnt):
    global v
    l = []
    for i in data:
        l.append(encrypt(i))

    v[cnt] = l

def writeInfo(thread_names: list[str]):
    cnt = 1
    while 1:
        threads = []
        for i in threading.enumerate():
            name = i.name
            if 'forEncrypt' in name:
                threads.append(name)
        
        os.system('cls')
        for i in thread_names:
            if i in threads:
                print(f'{i[:8]}: Loading'+'.'*cnt)
                
            else: print(f'{i[:8]}: Finished!')
        
        if cnt == 3: cnt = 1
        cnt += 1
        time.sleep(0.09)

if __name__ == "__main__":
    l = []
    with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou.txt", 'r', encoding='utf-8', errors='ignore') as f:
        l = f.readlines()

    l = l[:999996]
    l = [i[:-1] for i in l]

    start = time.time()

    l_len = len(l)
    thread = 6
    x = 0
    cnt = 1
    threads = []

    for i in range(thread):
        th = threading.Thread(target=forEncrypt, args=(l[x:x+166666], str(cnt)))
        threads.append(th)
        th.start()
        x += 166666
        cnt += 1

    thread_names = [i.name for i in threading.enumerate() if 'forEncrypt' in i.name]
    tht = threading.Thread(target=writeInfo,
                            args=(thread_names,),
                            daemon=True)
    tht.start()

    for t in threads:
        t.join()

    tht.kill = True
    os.system('cls')
    for i in thread_names:
        print(f'{i[:8]}: Finished!')

    stop = time.time()

    print('\ntime:', stop-start)
    # print(v.keys())