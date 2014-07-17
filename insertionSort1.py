#!/bin/python
def insertionSort(ar):
    v = ar[-1]
    ar.pop()
    index = len(ar)
    for x in ar[::-1]:
        if x > v:
            ar.insert(index, x)
            index -= 1
            print " ".join(str(e) for e in ar)
            ar.pop(index)
        else:
            ar.insert(index, v)
            print " ".join(str(e) for e in ar)
            break
    return ""

m = input()
ar = [int(i) for i in raw_input().split()]
insertionSort(ar)