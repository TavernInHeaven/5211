def indexint(list_l,int_i):
    for int_l in list_l:
        if int_l == int_i:
            return True
        elif int_l is not list_l[len(list_l) - 1]:
            indexint(list_l[1:], int_i)
        else:
            return False


def indexintwhile(list_l,index_num = 1):
    while len(list_l) is not 1:
        if list_l[index_num] == index_num + 1:
            return True
        elif len(list_l) == index_num:
            return False
        else:
            indexintwhile(list_l[1:], index_num)


def searchMiddle(aList,index_para):
    index_i = len(aList) // 2
    if aList[index_i] < index_para:
        searchMiddle(aList[index_i:], index_para - index_i)
    elif aList[index_i] > index_para:
        searchMiddle(aList[0:index_i],index_para)
    else:
        return index_para

def example(aList):
    def eql(l,a,b):
        mid = (a - b) // 2
        if mid == l[mid]:
            return True
        elif a == b or a == b - 1:
            return l[0] == a or l[b] == b
        elif mid < l[mid]:
            return eql(l,a,mid)
        else:
            return eql(l,mid,b)
    return eql(aList,0,len(aList) - 1)