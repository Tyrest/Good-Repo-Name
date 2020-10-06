import time
import random

def profile(f):
    def g(x):
        t0 = time.time()
        value = f(x)
        print(time.time() - t0)
        return value
    return g

def rate_limited(f):
    f.last_called = 0
    def g(x):
        time_since_last = time.time() - f.last_called
        if time_since_last < 1:
            time.sleep(1 - time_since_last)
        f.last_called = time.time()
        return f(x)
    return g

def retry(f):
    def g():
        value = f()
        return value if value else f()
    return g

@profile
def strip_evens(n):
    return [i * 2 + 1 for i in range(n // 2)]

@profile
def flatten(nested_list):
    current_list = []
    @rate_limited
    def flatten_rec(nested_list):
        if not isinstance(nested_list, list):
            current_list.append(nested_list)
        else:
            for i in nested_list:
                flatten_rec(i)
        return current_list
    return flatten_rec(nested_list)

@retry
def flip_coin():
    return random.random() < 0.5

# print(strip_evens(23423))
# print(flatten([[1, 2, [3, 4]], [5, 6], 7]))
flips = []
n = 10000
for i in range(n):
    flips.append(flip_coin())
print(sum(flips)/n)
