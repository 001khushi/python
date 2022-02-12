def itr_fac(n):
    p=1
    for i in range(n):
        p=p*(i+1)
    return p

def recursive_fac(n):
    if n==1 or n==0:
        return 1
    return n*recursive_fac(n-1)

f=itr_fac(5)
r=recursive_fac(5)
print(f)
print(r)