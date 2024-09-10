def missing(arr):
    if len(arr) == 0:
        return []

    arr = list(set(arr))
    arr.sort()
    
    maxi = arr[-1] #last element
    ret = []# returned array
    
    for x in range(arr[0], maxi + 1):
        if x not in arr:
            ret.append(x)
    
    return ret

print(missing([4, 6, 10, 4, 5, 1, 1, 1])) 

         






print(missing([1,4,6,2,3]))