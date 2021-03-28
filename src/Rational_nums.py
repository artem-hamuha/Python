import fractions

print(fractions.Fraction(1, 2))
print(fractions.Fraction('1/3'))
print(fractions.Fraction(3.14))
print(fractions.Fraction('3.14'))

x = fractions.Fraction(12, -24)
print(x)
print(x.denominator)

x = fractions.Fraction(0.3)
print(x)
print(x.limit_denominator(10))
print(x.limit_denominator(10000000000000000))
