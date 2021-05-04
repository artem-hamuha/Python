import decimal

print(decimal.getcontext())

print(decimal.localcontext())

with decimal.localcontext() as loc:
    loc.prec = 6
    loc.rounding = decimal.ROUND_HALF_UP
    print(loc)
    print(decimal.getcontext())
    print(id(loc) == id(decimal.getcontext()))



