def verify(arr):
    for i, j in zip(arr, arr[1:]):
        if j < i:
            return "Error! List is not sorted"
    return "List is sorted!"

# sanity check
if __name__ == "__main__":
    sorted_array = [i for i in range(100)]
    print(verify(sorted_array))