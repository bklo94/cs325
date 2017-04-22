import sys


def linearFindSubMax(arr):
    n = len(arr)
    leftIndex = rightIndex = currentIndex = 0
    maxSum = -sys.maxint
    tempSum = 0
    for i in range(0, n):
        if arr[i] >= (tempSum + arr[i]):
            tempSum = arr[i]
        #
        elif arr[i] < (tempSum + arr[i]):
            tempSum = (tempSum + arr[i])
        if tempSum > maxSum:
            right = i
            left = currentIndex
            maxSum = tempSum
        elif tempSum == arr[i]:
            currentIndex = i
    return maxSum, left, right+1


def convertAnswer():
    inputfile = open('MSS_Problems.txt')
    outputfile = open('MSS_Results.txt', 'a')
    outputfile.write('ALGORITHM 4 RESULTS \n')
    for line in inputfile:
        arr, arr2 = [], []
        string = line
        arr = map(int, string.strip().split(' '))
        n = len(arr)
        answers = linearFindSubMax(arr)
        end = answers[2]
        begin = answers[1]
        for i in range(begin, end):
            arr2.append(arr[i])
        outputfile.write(string.rstrip('\n') + '\n')
        arr2 = str(arr2).replace('[', '').replace(']', '')
        outputfile.write(arr2.replace(',', '') + '\n')
        outputfile.write(str(answers[0]) + '\n')
        outputfile.write('\n')
    inputfile.close()
    outputfile.close()
