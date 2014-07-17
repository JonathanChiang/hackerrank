#!/bin/python
def insertionSort(ar):
    for i in range(1, len(ar)):
        val = ar[i]
        j = i - 1
        while (j >= 0) and (ar[j] > val):
            ar[j+1] = ar[j]
            j = j - 1  
        ar[j+1] = val
        print " ".join(str(e) for e in ar)       
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)