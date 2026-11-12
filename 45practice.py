
p = input("Enter  : ")
k = [p]
copy_k = k.copy()
copy_k.reverse()
if k == copy_k :
    print("palindrome")
else :
    print("not palindrome")    