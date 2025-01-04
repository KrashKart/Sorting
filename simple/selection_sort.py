import wrappers
import sample_lists
from verify import verify

@wrappers.track_sort
def selection_sort(arr):
    n = len(arr)
    swaps = comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            comparisons += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return swaps, comparisons, arr

if __name__ == "__main__":
    res = selection_sort(sample_lists.RANDOM_XTRA_LARGE)
    verify(res)