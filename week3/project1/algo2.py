"""
Maximum Sum Subarray, Algorithm 2: Better Enumeration. 
Victor Ness
CS325
4/19/2017
"""


def max_sum_subarray(arr):

    """
    This implementation of max sum subarray takes an array as input and finds the sum of the max sum
    subarray within. It utilizes bottom-up dynamic programming with hash maps to store previously computed
    sums for more efficiency compared to the naive enumeration algorithm.
    """

    if len(arr) != 0:
        max_sum = arr[0]
        max_subarray = arr[0:1]
    current_sum = 0
    sums_dict = {}

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == j:
                sums_dict[(i, j)] = arr[i]
                current_sum += arr[i]
            else:
                current_sum = sums_dict[(i, (j - 1))] + arr[j]
                sums_dict[(i, j)] = current_sum

            if current_sum > max_sum:
                max_sum = current_sum
                max_subarray = arr[i:(j+1)]

            current_sum = 0

    return max_subarray, max_sum


def process_input():

    """
    reads input from file MSS_Problems.txt and converts each line to an array. Finds the maximum sum subarray 
    for the input array and outputs the original array, max subarray, and max sum into file
    MSS_Results.txt
    """

    inputfile = open('MSS_Problems.txt')
    outputfile = open('MSS_Results.txt', 'a')
    outputfile.write('ALGORITHM 2 RESULTS \n')
    for line in inputfile:
        input_array = map(int, line.strip().split(' '))
        outputs = max_sum_subarray(input_array)

        outputfile.write(str(input_array) + '\n')
        outputfile.write(str(outputs[0]) + '\n')
        outputfile.write(str(outputs[1]) + '\n\n')

    inputfile.close()
    outputfile.close()