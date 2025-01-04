import wrappers
import sample_lists
from itertools import permutations
from verify import verify

@wrappers.track_sort
def bogo_sort(arr):
    comparisons = 0
    perms = permutations(arr)
    while verify(arr) != "List is sorted!":
        arr = next(perms)
        comparisons += 1
    return 0, comparisons, list(arr)

# !!! long lists could stall the machine
if __name__ == "__main__":
    res = bogo_sort(sample_lists.RANDOM_XTRA_SMALL)
    verify(res)