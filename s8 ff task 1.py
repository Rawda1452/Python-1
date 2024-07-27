def is_sorted(l):
    x=l[:]
    x.sort()
    if l==x :
        return True 
    else:
        return False
l=list(input("enter your list items: ").split())
print(is_sorted(l))
