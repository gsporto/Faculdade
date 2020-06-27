def a(m,n):
    if m is 0:
        return n+1
    elif m > 0 and n is 0:
        return a(m-1,1)
    else:
        return a(m-1,a(m,n-1))
print(a(2,2))