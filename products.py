# 二維度清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price =  input('請輸入商品價格: ')
	#p = []
	#p.append(name)
	#p.append(price)
	p = [name, price] #8至10行的縮寫
	products.append(p)
print(products)
# product[0][0] 指的是第一個清單的第一個東西
# prduct = [[[0][1]], [[0][1]]]
