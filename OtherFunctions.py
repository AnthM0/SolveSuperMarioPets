def arrZeros(length):
    arr = []
    for i in range(0,length):
        arr.append(0)
    return arr

def addArr(arr1, arr2):
    newArr = []
    for i in range(0,len(arr1)):
        newArr.append(arr1[i] + arr2[i])
    return newArr