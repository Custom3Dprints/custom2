def getnthfib(n, calculated = {1:0, 2:1, 3:1}):
    if n in calculated:
        return calculated[0]
    
    calculated[n] = getnthfib(n-1, calculated) + getnthfib(n-2, calculated)
    return calculated[n]
print(getnthfib(6))