import random
start = input('首要數字： ')
end = input('結束數字： ')
start = int(start)
end = int(end)

r = random.randint(start, end) #隨機數字
count = 0 #次數
while True:
	count += 1
	num = input('請猜數字： ')
	num = int(num)
	if num == r:
		print('答對了！')
		print('這是你猜得第', count, '次')
		break
	if num > r:
		print('猜小一點！')
	if num < r:
		print('猜大一點！')
	print('這是你猜得第', count, '次')