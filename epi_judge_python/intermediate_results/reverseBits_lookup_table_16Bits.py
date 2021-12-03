def swap_bits(x, i, j):
    # TODO - you fill in here.
    if(x>>i & 1)!=(x>>j & 1):
        mask = (1<<i)|(1<<j)
        return x^mask
    else:
        return x

aList = []

for x in range(65536):
    for i in range(8):
        x = swap_bits(x, i, 15-i)
    aList.append(x)
    
print(aList)
