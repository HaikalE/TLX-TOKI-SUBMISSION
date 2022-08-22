def binarySearch(arr,x, n):
        l = 0 
        r = n - 1
        while (l <= r):
            m = l + (r - l) // 2
            res = -1000   
            if (x == (arr[m])):
                res = 0
            if (res == 0) :
                return m
            if (x > (arr[m])):
                l = m + 1
            else:
                r = m - 1
        return -1
kontak = {
  "nama": [],
  "hape": []
}
c,v=input().split()
for s in range(int(c)):
    cs=input().split()
    kontak["nama"].append(cs[0])
    kontak["hape"].append(cs[1])
hasil=[]
for se in range(int(v)):
    siapa=input()
    ans=binarySearch(kontak["nama"],siapa,len(kontak["nama"]))
    hasil.append(kontak["hape"][ans])
for c in hasil :
    print (c)
