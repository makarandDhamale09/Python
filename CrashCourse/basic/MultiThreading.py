import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Indicates some task being done
def func(seconds: int) -> int:
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    # Normal Code
    start_time = time.perf_counter()
    func(4)
    func(2)
    func(1)
    end_time = time.perf_counter()
    print(end_time - start_time)

    # Code using Threads
    start_time = time.perf_counter()
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    end_time = time.perf_counter()
    print(end_time - start_time)


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())


poolingDemo()
