def bubble_sort(L):
    for i in range(len(L)):
        for k in range(len(L)-1,i,-1):
            if L[k]>L[k-1]:
                swap(L,k,k-1)
    print L
def swap(L,x,y):
    t=L[x]
    L[x]=L[y]
    L[y]=t

bubble_sort([22,51,1245,1,1234,55,78,96,458])
