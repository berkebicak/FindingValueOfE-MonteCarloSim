from CalculateE_numba import findingValueOfE
from threading import Thread
import random


if __name__ == "__main__":
    
    findE = findingValueOfE()
    n = 1000000
    threads = []

    for i in range(random.randint(2,8)*2):
        threads.append(Thread(target=findE.value_of_e(n), args=(n,)))
        print("Started %d.thread " % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    e = findE.get_e()

    print("E = %8.6f | N = %d " % (e, findE.n))
