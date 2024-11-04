def linear_search_v1(search_list, target_value):
   
    for index, value in enumerate(search_list):
        if value == target_value:
            return index
    raise ValueError("{0} no está en la lista".format(target_value))

def linear_search_v2(search_list, target_value):
    indices = []
    for index, value in enumerate(search_list):
        if value == target_value:
            indices.append(index)
    if not indices:
        raise ValueError("{0} no está en la lista".format(target_value))
    return indices

def linear_search_v3(search_list):
   
    if not search_list:
        raise ValueError("La lista está vacía")
    
    max_index = 0
    for index in range(1, len(search_list)):
        if search_list[index] > search_list[max_index]:
            max_index = index
    return max_index

