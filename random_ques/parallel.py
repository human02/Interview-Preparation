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



