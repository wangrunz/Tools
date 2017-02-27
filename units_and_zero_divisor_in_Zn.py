from fractions import gcd
while(True):
    inputmod = input("Enter your mod: ")
    mod = int(inputmod)
    units=[]
    zerodivisor=[]
    for i in range(mod):
        if gcd(i,mod)==1:
            units.append(i)
    for i in range(1,mod):
        if i not in units:
            zerodivisor.append(i)
    print("Units: {}, Zero Divisor: {}".format(sorted(units),sorted(zerodivisor)))
