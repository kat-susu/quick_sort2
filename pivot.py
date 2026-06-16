import random

def get_pivot(arr, low, high, strategy="random"):
    if strategy == "random":
        idx = random.randint(low, high)
        return idx
    
    elif strategy == "median_of_three":
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        if (a <= b <= c) or (c <= b <= a):
            idx = mid
        elif (b <= a <= c) or (c <= a <= b):
            idx = low
        else:
            idx = high
        return idx