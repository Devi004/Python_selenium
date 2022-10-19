
lst=[int(x) for x in input().split()]
for i in range(len(lst)):
    for j in range(1,len(lst)-1):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp


print(lst)


