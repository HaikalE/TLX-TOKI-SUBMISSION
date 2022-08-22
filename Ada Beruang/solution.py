def cari(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return 1 
        elif arr[mid] > x:
            return cari(arr, low, mid - 1, x)
        else:
            return cari(arr, mid + 1, high, x)
    else:
        return 0
k=list(map(int, input().split()))
ans=0
c=list(map(int, input().split()))
for s in range(k[0]):
    if (c[s]>0) : 
        ans+=cari(c,0,len(c)-1,c[s]-k[1])
print(ans)
