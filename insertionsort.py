lst=[3,1,6,2,8]
temp=0
j=0
for i in range(1,len(lst)):
    temp=lst[i]
    j=i
    while(j>0 and lst[j-1]>temp):
      lst[j]=lst[j-1]
      j=j-1
    lst[j]=temp
print(lst)







