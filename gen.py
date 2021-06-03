#!/usr/bin/python3
import random, string, sys

ui = input("Amount: ")
#5CH9-SY4A-QBWV-FX2F-MQ8S
#CNTT-8NFT-F685-GV8X-YLSX
#spchar = 'FFSC8XV'
#lizt = "".join(random.choices(f"{list(spchar),k=1}{string.ascii_uppcase,k=3}{list(spchar),k=2}{string.digits,k=2}{list(spchar),k=1}{string.ascii_uppcase,k=3}{list(spchar),k=2}{string.digits,k=2}"))

spchar = 'MQFSC8XVTGH4N59WAYL'
key = []
c = 0
while(c<=int(ui)):

	for x in range(5):
		r = random.choices(list(spchar), k=4)
		r = ''.join(r)
		key.append(r)
		if len(key) >= 9:
			pass
		else:
			key.append('-')
	#sys.stdout.write(f'\rYour License key: {"".join(key)}')
	key2 = ''.join(key)

	if key2.count('F') == 2:
		if key2.count('S') == 1 or key2.count('S') == 2:
			if key2.count('X') <= 2 and key2.count('X') >= 1:
				if key2.count('8') == 1 or key2.count('8') ==2:
					if key2.count('V') == 1:
						print(''.join(key))
						c+=1
	key = []
