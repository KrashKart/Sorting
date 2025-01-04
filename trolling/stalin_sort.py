import wrappers
import sample_lists
from verify import verify

@wrappers.track_sort
def stalin_sort(arr):
    res = [arr[0]]
    swaps = comparisons = 0
    for i in range(1, len(arr)):
        comparisons += 1
        # if arr[i] is smaller than res[-1], send to gulag!
        if arr[i] >= res[-1]:
            res.append(arr[i])
    return swaps, comparisons, res

if __name__ == "__main__":
    res = stalin_sort(sample_lists.RANDOM_SMALL)
    verify(res)