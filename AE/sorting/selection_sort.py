"""
The idea to create 2 list: (1st is sorted and 2nd unsorted)
Next, select element from ith index and search till the end of the list
If we find 
"""

# O(n^2) | O(1) space
def selectionSort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    print(array)


selectionSort([3, 2, 8, 5, 1])
