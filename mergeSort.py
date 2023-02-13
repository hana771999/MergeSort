
from random import randint as rnd 


# list1 = [2,3,4,5,6,7,8,9]
# list2 = [1,3,5,6,9]

def mergeSort(list1,list2):
    _list=[]
    len1=len(list1)
    len2=len(list2)
    i=j=0
    while i<len1 and j<len2:
        if list1[i]<list2[j]:
            _list.append(list1[i])
            i+=1
        else:
            _list.append(list2[j])
            j+=1
    _list+=list1[i:]
    _list+=list2[j:]
    return _list      



def merge(_list):
    if len(_list)==1:
        return _list
    else:
        mid=len(_list)//2
        right= _list[mid:]
        left= _list[:mid]
        
    right=merge(right)
    left=merge(left) 
    
    return mergeSort(right,left)



length= 10 
_list= [rnd(1,length) for i in range(length)]
print(_list)
_list = merge(_list)
print(_list)