import random
start = input('請輸入隨機範圍起始整數: ')
end = input('請輸入隨機範圍結束整數: ')
start = int(start)
end = int(end)

r = random.randint(start, end)

n = 0
while True:
	i = input('請猜一整數: ')
	i = int(i)
	n += 1
	if i > r:
		print('比正確答案大,這是你猜的第', n, '次')
	elif i < r:
		print('比正確答案小,這是你猜的第', n, '次')
	else :
		print('猜對了,這是你猜的第', n, '次')
		break
