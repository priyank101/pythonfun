a=[3,8,1,2,9]
n=len(a)
temp=0
def heapify(a,n,i):
    largest=i
    li=2*i+1
    ri=2*i+2
    if li<n and a[largest]<a[li]:
        largest=li
    if ri<n and a[largest]<a[ri]:
        largest=ri
    if largest!=i:
        temp=a[i]
        a[i]=a[largest]
        a[largest]=temp
        heapify(a,n,i)


def sort(a):
    for i in range(n,-1,-1):
        heapify(a,n,i)
    for i in range(n-1,0,-1):
        temp=a[0]
        a[0]=a[i]
        a[i]=temp
        heapify(a,i,0)
sort(a)
for i in range(n):
 print(a[i],end=" ")


