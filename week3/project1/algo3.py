import sys

def maxArraySub(arr,left,right):
    if left == right:
        return [arr[left], left, right + 1]
    middle = (left+right)/2
    leftAnswer = maxArraySub(arr,left,middle)
    rightAnswer = maxArraySub(arr,middle+1,right)
    return max(max(leftAnswer,rightAnswer),maxSubArrayHelper2(arr,left,middle,right))

def maxSubArrayHelper2(arr,left,middle,right):
    leftSum = -sys.maxint
    leftIndex = middle
    tempSum = runningSum = 0
    for i in range(middle,-1,-1):
        tempSum += arr[i]
        if tempSum > leftSum:
            leftSum = tempSum
            leftIndex = i
    rightSum = -sys.maxint
    rightIndex = middle+1
    tempSum = runningSum = 0
    for i in range(middle+1,right+1):
        tempSum += arr[i]
        if tempSum > rightSum:
            rightSum = tempSum
            rightIndex = i+1
    total = leftSum+rightSum
    return total,leftIndex,rightIndex

def convertAnswer():
    inputfile = open('MSS_Problems.txt')
    outputfile = open('MSS_Results.txt', 'a')
    outputfile.write('ALGORITHM 3 RESULTS \n')
    for line in inputfile:
        arr,arr2 = [],[]
        string = line
        arr = map(int,string.strip().split(' '))
        n = len(arr)
        answers = maxArraySub(arr,0,n-1)
        end = answers[2]
        begin = answers[1]
        for i in range(begin,end):
            arr2.append(arr[i])
        outputfile.write(string.rstrip('\n')+ '\n')
        arr2 = str(arr2).replace('[','').replace(']','')
        outputfile.write(arr2.replace(',','') + '\n')
        outputfile.write(str(answers[0])+ '\n')
        outputfile.write('\n')
    inputfile.close()
    outputfile.close()