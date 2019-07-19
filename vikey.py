vp=str(input())
count=0
for i in vp:
    if i.isnumeric() or i.isalpha():
        pass
    else:
        count+=1
print(count)
