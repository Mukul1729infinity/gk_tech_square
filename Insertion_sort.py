def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        val=arr[i]
        pos=i-1
        while pos>=0 and arr[pos]>val:
            arr[pos+1]=arr[pos]
            pos=pos-1
        arr[pos+1]=val
    return arr
data = [4, 2, 2, 8, 3, 3, 1,45,65,67,87,98,34,56,7788]
insertionsort(data)
