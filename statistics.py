"""Python project to perform some simple statistics on a list of values.""" 
def list_statistics(my_list):
    import numpy as np
    return np.mean(my_list), np.median(my_list), np.std(my_list), np.var(my_list)

#print(list_statistics([2,8,6,7,6,4,12,56]))  