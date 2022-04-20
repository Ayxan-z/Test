import sqlite3
import sys
import time
import os.path

# sys.setrecursionlimit(3000)

def findPaths(data, root, probability):
    global result, cnt, path
    
    result += probability
    for i in data:
        if root == start and i != data[0][0]:
            result = 0
            
        if i[0] == stop and i[1] != 0:
            results['-'.join(path+[i[0]])] = (result + i[1]) / len(path)

        elif i[0] not in path and i[1] != 0:
            path.append(i[0])
            cursor.execute(f"SELECT * FROM {i[0]}")
            data = cursor.fetchall()
            findPaths(data, i[0], i[1])
    
    del(path[-1])
    result -= probability


def findMaxValue(results):
    max_value = 0
    for key, value in results.items():
        if value > max_value:
            max_value = value
            max_path = key
    
    return max_path, max_value

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "DB/test10.db")
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    start = 'S0'
    stop = 'S9'
    path = [start]
    result = 0
    results = {}
    cnt = 0
    
    start_time = time.time()
    
    cursor.execute(f"SELECT * FROM {start}")
    data = cursor.fetchall()
    findPaths(data, start, 0)
    con.close()
    max_path, max_value = findMaxValue(results)
    
    finish_time = time.time()
    
    print('Time: ', finish_time - start_time)
    print('Path count: ', len(results))
    print(max_path, '-', max_value)

    