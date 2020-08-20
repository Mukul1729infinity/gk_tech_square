def shell_sort(arr):
    n=len(arr)
    gap=n//2
    while gap > 0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while j >= gap and arr[j-gap] > temp:
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap=gap//2
    return arr
arr=[2,-9,7,1,-1,-2,78,1,15,98,-78,58]
shell_sort(arr)
