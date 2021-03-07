for i in range(1, 10):
	for j in range(1, 10):
		print ('i=',i,'j=',j)
		if  i == 1 and j == 1 :
			print('Continues inner loop at i = 1 j = 1')
			continue
		if  i == 5 and j == 5 :
			print('Continues inner loop at i = 1 j = 1')
			break