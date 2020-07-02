def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
def quicksort(arr,low,high):
    if low<=high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
data = [4, 2, 2, 8, 3, 3, 1,45,65,67,87,98,34,56,7788]
n=len(data)
quicksort(data,0,n-1)
