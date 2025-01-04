def verify(arr):
    for i, j in zip(arr, arr[1:]):
        if j < i:
            print("Error! List is not sorted")
            return
    print("List is sorted!")

# sanity check
if __name__ == "__main__":
    sorted_array = [i for i in range(100)]
    verify(sorted_array)