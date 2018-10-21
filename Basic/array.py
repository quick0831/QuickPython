# List (so do tuple)
a=[1,2,3,4,5]
len(a) # 5 (The length of the list)
a[3] # 4
a[0]=5
print(a[:3])
a[:3]=[] # delete[:3]
print(a)
# Use + to Merge List

print("")

data=[[3,4,5],[6,7,8]]
print(data[0][1])
data[0][0:2]=[5,5,5]
print(data[0])