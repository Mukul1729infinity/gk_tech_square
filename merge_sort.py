def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i<len(l) and j <len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1
    return arr
data = [4, 2, 2, 8, 3, 3, 1,45,65,67,87,98,34,56,7788]
mergesort(data)
