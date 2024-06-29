#bubble sorting 
i=[2,5,6,2,4,1,4,5]#unordered list
swaping=True
end=len(i)
while swaping==True: #swap until no swaps in the nested loop
    swaping=False   #to break the while loop if no swap detected
    for k in range(1,end): #from 1st index till end loop and swap if swap detected and turn swaping into true
        if i[k-1]>i[k]:
            swaping=True
            temp=i[k-1]
            i[k-1]=i[k]
            i[k]=temp
    end-=1
print(i)
# binary search
target=6
l=0
h=len(i)-1
while l<=h:
    mid=(l+h)//2
    if i[mid]==target:
        print(f"found {i[mid]} in {mid+1}th position ")
        break
    elif target>i[mid]:
        l=mid+1
    else:
        h=mid-1
if l>h:
    print(f"{target} not found")
        
