from time import time
from multiprocessing import Pool

def encrypt(text):
    result = ''
    s = 5
    az_alp = ['a','b','c','ç','d','e','ə','f','g','ğ','h','x','ı','i','j','k',
            'q','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
    az_alp_upper = ['A','B','C','Ç','D','E','Ə','F','G','Ğ','H','X','I','İ',
                    'J','K','Q','L','M','N','O','Ö','P','R','S','Ş','T','U',
                    'Ü','V','Y','Z']
    
    nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
            25,26,27,28,29,30,31,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,
            -21,-20,-19,-18,-17,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    
    for t in text:
        if t in az_alp:
            result += az_alp[nums[az_alp.index(t) + s]]

        elif t.upper() in az_alp_upper:
            result += az_alp_upper[nums[az_alp_upper.index(t) + s]]

        else:
            result += chr(ord(t) + 601 + s)

    return result


if __name__ == "__main__":
    l = []
    with open("C:\\Users\\shahs\\Documents\\test\\data\\rockyou.txt", 'r', encoding='utf-8', errors='ignore') as f:
        l = f.readlines()

    l = l[:7000000]
    l = [i[:-1] for i in l]

    start = time()

    with Pool(7) as p:
        r = p.map(encrypt, l)

    stop = time()
    print(stop-start)
    print(len(r))