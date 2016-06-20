def comp(array1, array2):
    if array1==None or array2==None or len(array1) != len(array2):
        return False
    elif len(array1) ==0 or len(array2)==0:
        return True
    sq_array = []
    for elem in array1:
        sq_array.append(elem**2)
    for item in array2:
        if item not in sq_array: return False
    return True
