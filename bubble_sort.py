def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
data = [4, 2, 2, 8, 3, 3, 1,45,65,67,87,98,34,56,7788]
bubblesort(data)
