import time

def track_sort(func):
    def wrapper(*args):
        arr = None
        for a in args:
            if type(a) == type([]):
                arr = a
        if not a:
            raise ValueError("Input an array!")
    
        start_time = time.time()
        if len(arr) > 100:
            print("List is too big to be displayed!")
        else:
            print(f"Initial: {arr}")

        swaps, comparisons, res = func(*args)

        if len(arr) > 100:
            print("List is too big to be displayed!")
        else:
            print(f"After: {res}")
            
        print(f"Swaps: {swaps}")
        print(f"Comparisons: {comparisons}")
        print(f"Time taken ({func.__name__}): {time.time() - start_time}")
        return res
    
    return wrapper
        

def count_swaps(func):
    def wrapper(arr):
        swaps, res = func(arr)
        print(f"Swaps: {swaps}")
        return res
    
    return wrapper

def time_sort(func):
    def wrapper(arr):
        start_time = time.time()
        res = func(arr)
        print(f"Time taken for {func.__name__}: {time.time() - start_time}")
        return res

    return wrapper

def time_and_print(func):
    def wrapper(arr):
        start_time = time.time()
        print(f"Initial: {arr}")
        res = func(arr)
        print(f"After: {res}")
        print(f"Time taken for {func.__name__}: {time.time() - start_time}")
        return res

    return wrapper