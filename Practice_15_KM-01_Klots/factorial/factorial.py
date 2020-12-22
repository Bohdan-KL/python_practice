def fac(n):
    if int(n)!=n or n<0:
        return 'number should be a natural.'
    elif n == 0:
        return 0
    else:
        n=int(n)
        d = 1
        for i in range(1, n + 1):
            d *= i
        return d
