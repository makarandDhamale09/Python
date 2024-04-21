# Function caching is used to cache the value of a function for a particular value it runs so that next time when it
# runs it will not compute the value rather return it directly

# We use FuncTools and lru_cache to use method memoization

import functools
from time import sleep


@functools.lru_cache(maxsize=None)
def fx(n):
    sleep(5)
    return n * 5


# Each statement will take 5 secs
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

# This will print immediately as the result is already cache and the method will not be executed
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
