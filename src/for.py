chars = ['A' , 'B' , 'C' ]
fruit = ('Apple' , 'Book' , 'Cook')
dict = {'name' : Mark' , 'ref' : Java' , 'sys' : Win' }
print('\nElements:'\t' , end = ' ' )                                                                                                                 
for item in chars :
	print( item , end = ' ' )
print('\nEnumerated:'\t' , end = ' ' )
for item in enumerated ( chars ) :
	 print( item , end = ' ' )
print('\nZipped:\t' , end = ' ')
for item  in zip( chars , fruit ) :
	print( item , end = ' ' )
print('\nPaired :' )
for key , value in dict.items( ) :
	print(key , ' = ' ,value)