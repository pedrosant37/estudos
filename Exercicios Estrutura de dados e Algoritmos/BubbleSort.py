def BubbleSort(list: list) -> list:
    if len(list) <= 1:
        return list
    unorderedElements = len(list)
    while unorderedElements > 1:
        for idx in range(len(list)-1):
            if list[idx] >= list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
            if idx == unorderedElements -1:
                break
            print(list)
        unorderedElements -= 1
    return list

lista = [325,46,64,8325,8796,325,86]
print(BubbleSort(lista))