import requests, re, random, string
from bs4 import BeautifulSoup

url = 'https://ip-trap.com/bait-page/?trap=0ab0ee72-3649-4f38-b5a5-8698368ba47a'

# https://ip-trap.com/bait-page/?trap=0ab0ee72-3649-4f38-b5a5-8698368ba47a
# https://ip-trap.com/bait-page/?trap=a3069664-1151-492d-b441-da8098094cc8

char_pattern = 'abcdef'
num_pattern = '0123456789'


c1 = ''.join(random.choices(char_pattern,k=random.randint(1,4)))
pad = 8-int(len(c1))
cc1 = ''.join(random.choices(string.digits,k=pad))
code1 = ''.join(random.sample(c1+cc1,len(c1+cc1)))
#print(code1)
code2 = ''.join(random.choices(string.digits,k=4))
#print(code2)
c3 = ''.join(random.choices(char_pattern))
cc3 = ''.join(random.choices(string.digits,k=3))
code3 = ''.join(random.sample(c3+cc3,len(c3+cc3)))
#print(code3)
c4 = ''.join(random.choices(char_pattern,k=random.randint(1,2)))
cc4 = ''.join(random.choices(string.digits,k=4-int(len(c4))))
code4 = ''.join(random.sample(c4+cc4,len(c4+cc4)))
#print(code4)
c5 = ''.join(random.choices(char_pattern,k=random.randint(3,4)))
cc5 = ''.join(random.choices(string.digits,k=12-int(len(c5))))
code5 = ''.join(random.sample(c5+cc5,len(c5+cc5)))
#print(code5)
code = f'{code1}-{code2}-{code3}-{code4}-{code5}'
print(code)

"""
r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")

for anchor in soup.find_all('a'):
	url = anchor['href']
	pattern = r'https://www.ipaddress.com/ipv4/'
	if(re.search(pattern,url)):
		filtered = re.sub(pattern,'',url)
		print(filtered)



162.214.193.59:3128
59.124.224.205:3128
"""
