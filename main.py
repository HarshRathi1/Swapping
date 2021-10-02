list=[32,56,18,92,90,55,71]
n=len(list)
def swapping(list):
    temp=list[0]
    list[0]=list[n-1]
    list[n-1]=temp
    return list
print(swapping(list))
