def bucketsort(arr):
    bucket=[]
    n=len(arr)
    for i in range(n):
        bucket.append([])
    for j in arr:
        index=int(n*j)
        bucket[index].append(j)
    for i in range(n):
        bucket[i]=sorted(bucket[i])
    k=0
    for i in range(n):
        for j in range(len(bucket[i])):
            arr[k]=bucket[i][j]
            k+=1
    return arr
x = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434]  
bucketsort(x)
