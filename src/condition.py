a=1

b=2

print('\nVariable a is:','one'if (a == 1) else'Not one')
print('Variable a is:','even'if (a % 2 == 0) else'Odd')

print('\nVariable b is:','three'if (b == 3) else'Not three')
print('Variable b is:','even'if (b % 2 == 0) else'Odd')

max = a if(a > b) else b

print('\nGreatter Value is:',max)