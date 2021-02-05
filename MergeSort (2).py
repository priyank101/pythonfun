def merge_two_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=lst[:mid]
    right=lst[mid:]

    left=merge_two_sort(left)
    right=merge_two_sort(right)

    return mergesort(left,right)

def mergesort(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=j=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    while j < len_b:
            sorted_list.append(b[j])
            j+= 1
    return sorted_list

#if __name__=='__main__':
lst=[10,3,15,7,8,23,98]
print(merge_two_sort(lst))


















