

def list_of_even_num(lst):
    temp_list = []
    for i in lst:
        if i % 2 == 0:
            temp_list.append(i)
    return temp_list
