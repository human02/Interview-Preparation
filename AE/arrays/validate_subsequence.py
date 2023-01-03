def isValidSubsequence(array, sequence):
    # Write your code here.
    # Using 2-pointer technique to solve it
    arr_idx = 0
    seq_idx = 0
    while (arr_idx < len(array) and seq_idx < len(sequence)):
        if (array[arr_idx] == sequence[seq_idx]):
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)
