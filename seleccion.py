from random import randint
import timeit
import sys


# lista_sin_ordenar = [randint(0,100) for i in range(10)]
m = [randint(0,100000) for i in range(int(sys.argv[1]))]
sys.setrecursionlimit(max(sys.getrecursionlimit(), len(m)+100000))


def sort_by_selection(m):
    lista_sin_ordenar = list(m)
    lista_ordenada = []
    min = lista_sin_ordenar[0]
    for j in range(0,len(lista_sin_ordenar)):
        for i in lista_sin_ordenar:
            if i < min:
                min = i
        lista_ordenada.append(min)
        lista_sin_ordenar.remove(min)
        try:
            min = lista_sin_ordenar[0]
        except Exception:
            pass
    return lista_ordenada

def sort_by_insertion(m):
    for i in range(0,len(m)):
        pos = i
        valor = m[i]
        while (pos > 0) and ( valor < m[pos - 1] ):
            m[pos] = m[pos - 1]
            pos = pos - 1
        m[pos] = valor
    return m

def sort_by_bubble(m):
    m = list(m)
    for i in range(0,len(m) - 1):
        for j in range(0,len(m) - 1):
            if m[j] > m[j+1]:
                tmp = m[j]
                m[j] = m[j+1]
                m[j+1] = tmp
    return m

def sort_by_quicksort(m):
    quickSortHelper(m, 0, len(m) - 1)

def quickSortHelper(alist, first, last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

start_time = timeit.default_timer()
sort_by_selection(m)
print timeit.default_timer() - start_time

start_time = timeit.default_timer()
sort_by_insertion(m)
print timeit.default_timer() - start_time

start_time = timeit.default_timer()
sort_by_bubble(m)
print timeit.default_timer() - start_time

start_time = timeit.default_timer()
sort_by_quicksort(m)
print timeit.default_timer() - start_time
