'''
Part 1: You are cleaning a dataset and want to return back a dataset with only valid elements. Someone has already implemented a function which can take in a single element and tell you if its valid.

Part 2: Now we want to use parallelism to speed up this cleaning process to faster than linear time


You have access to a function parallel such that


a,b = parallel(foo, x, bar, y)


is equivalent to


a = foo(x)
b = bar(y)


except in parallel


You can use shared memory if you want by creating a global variable and just assume that all your parallel jobs have access to this shared variable.

'''

def validation_fn(element) -> bool:
    return True

# Example usage of parallel function to clean a dataset
def parallel_clean(data):
    if len(data) == 0:
        return []
    if len(data) == 1:
        return [data[0]] if validation_fn(data[0]) else []
    mid = len(data) // 2
    left, right = parallel(parallel_clean, data[:mid], parallel_clean, data[mid:])
    return left + right

# Usage:
cleaned = parallel_clean(data)
def clean_dataset(data: list) -> list:
    n = len(data)
    solution =[]
    for i in data:
        # performing  a validation check
        if validation_fn(i):
            solution.append(i)
    return solution 



# Maybe useful later. Maybe not. Depends

def parallel(foo, x, bar, y):
    return foo(x), bar(y)

