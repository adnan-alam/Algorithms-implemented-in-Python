
def insertionSort(array):
    size = len(array)
    
    for index in range(1,size):
        temp = array[index]
        hole = index
        while hole > 0 and array[hole-1] > temp:
            array[hole] = array[hole-1]
            hole -= 1
        array[hole] = temp
        
    return array
