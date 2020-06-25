import os

# read file
products = []
if os.path.isfile('products.csv'): # check if the file is there
	print('yeah! found it')
	with open('products.csv', 'r') as f:
		for line in f:
			if 'item, price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('><! Cannot find it')

# user input
while True:
	name = input('Enter item: ')
	if name == 'q':
		break
	price = input('Enter price: ')
	small_list = [name, price]
	products.append(small_list)
print(products)

# print out the purchase record
for p in products:
	print('The price of', p[0], 'is', p[1])

# Write file
with open ('products.csv', 'w') as f:
	f.write('item, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')