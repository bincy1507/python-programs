# Selection sort in Python

def selection_sort(array,size):
    for step in range(size):
        min_idx = step
        for i in range(step+1,size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step],array[min_idx]) = (array[min_idx],array[step])
list = [32,17,45,39,76,58,21]
n = len(list)
selection_sort(list,n)
print(list)
