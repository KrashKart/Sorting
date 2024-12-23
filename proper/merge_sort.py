import wrappers
import sample_lists
from verify import verify

def merge(left: list[int], right: list[int]) -> list[int]:
    res = []
    swaps = comparisons = 0
    while left and right:
        comparisons += 1
        if right[0] < left[0]:
            res.append(right.pop(0))
            swaps += 1 # simulates an "in-place" swap on the left array, so if the right array element is smaller, count it as a swap
        else:
            res.append(left.pop(0))
    res.extend(left)
    res.extend(right)
    return swaps, comparisons, res

def merge_sort(arr: list[int]) -> tuple[int, int, list[int]]:
    if len(arr) < 2:
        return 0, 0, arr
    mid = len(arr) // 2
    lswaps, lcomparisons, left = merge_sort(arr[:mid])
    rswaps, rcomparisons, right = merge_sort(arr[mid:])
    mswaps, mcomparisons, merged = merge(left, right)
    return lswaps + rswaps + mswaps, lcomparisons + rcomparisons + mcomparisons, merged

@wrappers.track_sort
def start_merge_sort(arr):
    return merge_sort(arr)

if __name__ == "__main__":
    res = start_merge_sort(sample_lists.RANDOM_SMALL)
    print(verify(res))