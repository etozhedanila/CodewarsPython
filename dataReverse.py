def data_reverse(data):
	result = []
	for i in range(len(data)-8,-8, -8):
		for j in range(i, i + 8):
			result.append(data[j])
	return result

data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
print(data_reverse(data1))
print(data2)