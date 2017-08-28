
def bubbleSort(array):
    size = len(array)
    for passnum in range(size-1,0,-1):
        for index in range(passnum):
            if array[index] > array[index+1]:
                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp
    
    return array
    
    
# more efficient than the above one

def shortBubbleSort(array):
    
    exchanges = True
    passnum  = len(array) - 1
    
    while passnum > 0 and exchanges:
        exchanges = False
        for index in range(passnum):
            if array[index] > array[index+1]:
                exchanges = True
                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp
        passnum -=1
    
    return array
    
