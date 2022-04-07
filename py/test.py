import time
from multiprocessing import Pool


def sum_of_cubes(x, y):
    print(f"start process {x}, {y}")
    time.sleep(1)
    print(f"end process {x}, {y}")
    return x * x * x + y * y * y


if __name__ == "__main__":
    pool = Pool(processes=4)
    print(pool.starmap(sum_of_cubes, [(19, 19), (13, 19), (1, 5)]))
    print("HERE!")
    print("HERE AGAIN!")
    pool.close()
    pool.join()
