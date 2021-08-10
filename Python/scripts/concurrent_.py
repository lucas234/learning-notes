# @Time    : 2021/3/5 16:36
# @Author  : lucas
# @File    : concurrent_.py
# @Project : pyqt
# @Software: PyCharm
# from concurrent.futures import ThreadPoolExecutor, wait, as_completed
# from time import sleep
# from random import randint
#
#
# def return_after_5_secs(num):
#     sleep(randint(1, 5))
#     return "Return of {}".format(num)
#
#
# pool = ThreadPoolExecutor(5)
# futures = []
# for x in range(5):
#     futures.append(pool.submit(return_after_5_secs, x))
#
# # for x in as_completed(futures):
# #     print(x.result())
# print(wait(futures)[0].pop().result())


import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()