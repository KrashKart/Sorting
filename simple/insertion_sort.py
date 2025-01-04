import wrappers
import sample_lists
from verify import verify

@wrappers.track_sort
def insertion_sort(arr):
    n = len(arr)
    swaps = comparisons = 0
    for i in range(1, n):
        curr = arr[i]
        j = i - 1

        while j > -1 and curr < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
        swaps += 1

    return swaps, comparisons, arr

if __name__ == "__main__":
    res = insertion_sort(sample_lists.RANDOM_XTRA_LARGE)
    verify(res)