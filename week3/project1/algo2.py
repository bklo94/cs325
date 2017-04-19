"""
Maximum Sum Subarray, Algorithm 2: Better Enumeration. 
Victor Ness
CS325
4/19/2017
"""


def max_sum_subarray(input_list):

    """
    This implementation of max sum subarray takes a list as input and finds the sum of the max sum
    subarray within. It utilizes bottom-up dynamic programming with hash maps to store previously computed
    sums for more efficiency compared to the naive enumeration algorithm.
    """

    if len(input_list) != 0:
        max_sum = input_list[0]
        max_list = input_list[0:1]
    current_sum = 0
    sums_dict = {}

    for idx_out, val_out in enumerate(input_list):
        for idx_in, val_in in enumerate(input_list):
            if idx_in >= idx_out:
                if idx_out == idx_in:
                    sums_dict[(idx_out, idx_in)] = val_in
                    current_sum += val_in
                else:
                    current_sum = sums_dict[(idx_out, (idx_in - 1))] + val_in
                    sums_dict[(idx_out, idx_in)] = current_sum

                if current_sum > max_sum:
                    max_sum = current_sum
                    max_list = input_list[idx_out:(idx_in+1)]

                current_sum = 0

    return max_list, max_sum

test_input = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

print max_sum_subarray(test_input)