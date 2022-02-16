def ArrayChallenge(arr):
    sum = 0
    value = False
    if len(arr)> 2 :
        for i in range(0,len(arr)-1):

            if sum < arr[i]:
                value = True
                sum += arr[i]
                # print(sum)        #--> # for verification in the execution.
            else:
                value = False

        if value == True :
            print("True")
        else :
            print("False")
    else:
        print("False")



testcases = [
    [10,23,34,89],
    [1,2,3,4],
    [8,12,24,46],
    [2,4,8,16],
    [1,6,5,24],
    [8,16,24,32],
    [9,18,36,72],
    [9,18,36,63]
    ]

for i in testcases:
    ArrayChallenge(i)


