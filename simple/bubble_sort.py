import wrappers
import sample_lists
from verify import verify

@wrappers.track_sort
def bubble_sort(arr):
    n = len(arr)
    swaps = comparisons = 0
    for i in range(n):
        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swaps += 1
            comparisons += 1
    return swaps, comparisons, arr

if __name__ == "__main__":
    res = bubble_sort(sample_lists.RANDOM_XTRA_LARGE)
    verify(res)