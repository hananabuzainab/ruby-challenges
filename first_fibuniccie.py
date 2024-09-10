def fibuniccie(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibuniccie(n - 1) + fibuniccie(n - 2)
    

print(fibuniccie(9))
print(fibuniccie(10))