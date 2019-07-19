numl=int(input())
nums1=list(map(int,input().split()))
tem=0
div=len(nums1)
for i in range(numl):
    tem+=nums1[i]
res=tem//div
print(res)
