def sort(array):
    for i in range(0, len(array) -1):
        for j in range(0, len(array) -1 -i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return(array)

lista = [34,56,87,12,6,9,2,4,5]

print(sort(lista))

