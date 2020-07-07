import os #operating system
# important concept: refactor

# read file
# 1 function for doing 1 thing
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if 'item, price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products #with return, you can save the result of excecuting function

# user input
def user_input(products):
	while True:
		name = input('Enter item: ')
		if name == 'q':
			break
		price = input('Enter price: ')
		small_list = [name, price]
		products.append(small_list)
	print(products)
	return products

# print out the purchase record
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', p[1])

# Write file
def write_file(filename, products):
	with open (filename, 'w') as f:
		f.write('item, price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

#Execute mainly funciotn
def main(): 
	filename = 'products.csv'
	if os.path.isfile(filename): # check if the file is there
		print('yeah! found it')
		products = read_file(filename)		
	else:
		print('><! Cannot find it')
		
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()


