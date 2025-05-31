def SelectionSort(list):
    for unordered in range(len(list)-1):
        positionOfMin = unordered
        for item in range(unordered, len(list)-1):
            if list[item+1] < list[positionOfMin]:
                positionOfMin = item+1
        temp = list[unordered]
        list[unordered] = list[positionOfMin]
        list[positionOfMin] = temp
    return list

print(SelectionSort([1,9,32,8,5,3,7,2]))