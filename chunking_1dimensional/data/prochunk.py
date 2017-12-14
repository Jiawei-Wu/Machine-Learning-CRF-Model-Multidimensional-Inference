f = open('chunk_train.data')
f2 = open('chunk_test.data')

w = open('train.data', 'w')
w2 = open('test.data', 'w')

buf = []
for i in f:
	if len(i)>2:
		w.write(i.split(' ')[0]+' '+i.split(' ')[2])
	else:
		w.write('\n')

for i in f2:
	if len(i)>2:
		w2.write(i.split(' ')[0]+' '+i.split(' ')[2])
	else:
		w2.write('\n')

w.close()
w2.close()