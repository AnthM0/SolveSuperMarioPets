def arrZeros(length,fill=0):
    arr = []
    for i in range(0,length):
        arr.append(fill)
    return arr

def addArr(arr1, arr2):
    newArr = []
    for i in range(0,len(arr1)):
        newArr.append(arr1[i] + arr2[i])
    return newArr