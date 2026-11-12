x = int(input("enter number from list : "))
n = ( 1,2,33,34,21,13,3,342,131,41,141,344,44,2)
idx = 0
while idx<len(n):
    if n[idx]==x:
        print("found at index : ",idx)
    idx += 1