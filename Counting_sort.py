def countingsort(arr,lar):
    c=[0]*(lar+1)
    for i in range(len(arr)):
        c[arr[i]]+=1
    c[0]=c[0]-1
    for i in range(1,lar+1):
        c[i]=c[i]+c[i-1]
    result=[None]*(len(arr))
    for x in reversed(arr):
        result[c[x]]=x
        c[x]-=1
    print(result,end="")
data=[4, 2, 2, 8, 3, 3, 1,4, 2, 2, 8, 3, 3, 1,45,65,67,87,98,34,56,7788,23]
lar=max(data)
countingsort(data,lar)
