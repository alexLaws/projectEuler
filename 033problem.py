def newFraction(numerator,denominator):
    stringNum = str(numerator)
    stringDen = str(denominator)
    nA = stringNum[0]
    nB = stringNum[1]
    dA = stringDen[0]
    dB = stringDen[1]
    if nA == dA:
        return((int(nB), int(dB)))
    elif nA == dB:
        return((int(nB), int(dA)))
    elif nB == dA:
        return((int(nA), int(dB)))
    elif nB == dB:
        return((int(nA), int(dA)))

success = []

for n in range(11,100):
    for d in range(n+1,100):
        newDiv=0
        dividend = n/d
        new = newFraction(n,d)
        if new:
            try:
                newDiv = new[0]/new[1]
            except:
                newDiv = 0
        if dividend == newDiv:
            if n % 10 > 0:
                success.append((n,d))

numerator = 1
denominator = 1
for fraction in success:
    numerator *= newFraction(fraction[0],fraction[1])[0]
    denominator *= newFraction(fraction[0],fraction[1])[1]
print(numerator)
print(denominator)
print(denominator/numerator)
