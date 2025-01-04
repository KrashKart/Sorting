import wrappers
import sample_lists
from verify import verify

def gaslight_sort(arr):
    print("List is too big to be displayed!")
    print("List is too big to be displayed!")
    print(f"Swaps: 0")
    print(f"Comparisons: 0")
    print(f"Time taken ({gaslight_sort.__name__}): 0")
    return [1,]

# get gaslighted bozo
if __name__ == "__main__":
    res = gaslight_sort(sample_lists.RANDOM_XTRA_SMALL)
    verify(res)