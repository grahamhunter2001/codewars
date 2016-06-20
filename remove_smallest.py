def remove_smallest(numbers):
    if len(numbers)>0:
        min_num = min(numbers)
        numbers.pop(numbers.index(min_num))
        return numbers
    else:
        return numbers
