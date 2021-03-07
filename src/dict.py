dict = {'name' : 'Bob' , 'ref' : 'Python ' , 'sys' : 'Win'}
print('Dictionary:' ,dict)
print('\nReferense:' ,dict[ 'ref'] )
print('\nKeys:' ,dict.keys() )
del dict['name']
dict['user'] = Tom
print('\nDictionary:' ,dict)
print('\nIs There A name Key?:' , 'name' in dict)