import wrappers
import sample_lists
from verify import verify

@wrappers.track_sort
def miracle_sort(arr):
    swaps = comparisons = 0
    for i in range(1, len(arr)):
        comparisons += 1
        if arr[i - 1] > arr[i]:
            pray()
    return swaps, comparisons, list(arr)

def pray():
    print("Dorime")

# please dont run this
if __name__ == "__main__":
    res = miracle_sort(sample_lists.RANDOM_XTRA_SMALL)
    verify(res)