import wrappers
import sample_lists
import time
import multiprocessing as mp
from verify import verify

# zzzzzzz
def wait(res, x, offset):
    time.sleep((x + offset) / 5000)
    res.append(x)

@wrappers.track_sort
def sleep_sort(arr):
    pool = mp.Pool(len(arr))
    res = mp.Manager().list()
    offset = abs(min(arr))

    pool.starmap(wait, [(res, i, offset) for i in arr])
    res = list(res)
    return 0, len(arr), res # len(arr) comparisons to find minimum

# beware, a list too long may result in not enough cpus!
if __name__ == "__main__":
    res = sleep_sort(sample_lists.RANDOM_XTRA_SMALL)
    print(verify(res))