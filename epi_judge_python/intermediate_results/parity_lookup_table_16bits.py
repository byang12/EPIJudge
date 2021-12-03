import pickle

def parity(x: int) -> int:
    # TODO - you fill in here.
    parityCheck = 0
    while(x):
        x = x & (x-1)
        parityCheck = parityCheck ^ 1
    return parityCheck
    
    
i = 0xFFFF
lookup_table = {}
while(i>=0):
    parityCheck = parity(i)
    lookup_table[i] = parityCheck
    i = i-1

a_file = open("parityLookupTable16Bits.pkl", "wb")
pickle.dump(lookup_table, a_file)
a_file.close()
