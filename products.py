products = []
while True:
	name = input('Enter item: ')
	if name == 'q':
		break
	price = input('Enter price: ')
	small_list = [name, price]
	products.append(small_list)
print(products)

for p in products:
	print('The price of', p[0], 'is', p[1])