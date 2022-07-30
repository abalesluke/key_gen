#!/usr/bin/python3
import random, string, sys, os

#5CH9-SY4A-QBWV-FX2F-MQ8S
#CNTT-8NFT-F685-GV8X-YLSX
#spchar = 'FFSC8XV'
#lizt = "".join(random.choices(f"{list(spchar),k=1}{string.ascii_uppcase,k=3}{list(spchar),k=2}{string.digits,k=2}{list(spchar),k=1}{string.ascii_uppcase,k=3}{list(spchar),k=2}{string.digits,k=2}"))

spchar = 'MQFSC8XVTGH4N59WAYL'


def generate():
	c = 0
	ui = input("Amount: ")
	total_keys = ''

	while(c<=int(ui)):
		key = []
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
			if key2.count('S') >= 1 and key2.count('S') <= 2:
				if key2.count('X') >= 1 and key2.count('X') <= 2:
					if key2.count('8') >= 1 and key2.count('8') <= 2:
						if key2.count('V') == 1:
							c+=1
							total_keys+=''.join(key)+'\n'
	if(not os.path.exists('valid_keys')):
		open('valid_keys','w')

	f = open('valid_keys','a')
	f.write(total_keys+'\n')
	f.close()


def check2(key2):
	err = '[CODE_ERR]: Invalid code'
	if(len(key2)!=24):
		return err
	if key2.count('F') != 2:
		return err
	if key2.count('S') < 1 or key2.count('S') > 2:
		print('1')
		return err
	if key2.count('X') < 1 or key2.count('X') > 2:
		print('2')
		return err
	if key2.count('8') < 1 or key2.count('8') > 2:
		print('3')
		return err
	if key2.count('V') != 1:
		return err
	return 'valid'


def check(key):
	isValid = False
	new_valid_keys = ''
	if(not os.path.exists('valid_keys')):
		open('valid_keys','w')
	for valid_key in open('valid_keys','r').read().splitlines():
		if(key == valid_key):
			isValid=True
		else:
			new_valid_keys+=valid_key+'\n'

	if(isValid):
		f = open('valid_keys','w')
		f.write(new_valid_keys)
		return True
	else:
		return False


#x=check('5YSX-VFGF-WX9A-YA4N-A88C')
x=generate()
print(x)
