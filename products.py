# 二維度清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price =  input('請輸入商品價格: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	p = [name, price] #8至10行的縮寫
	products.append(p)
print(products)
# product[0][0] 指的是第一個清單的第一個東西
# prduct = [[[0][1]], [[0][1]]]
for p in products:
	print(p[0], '的價格是', p[1])

#字串的加、乘
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

