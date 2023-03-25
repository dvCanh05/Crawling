import requests
import sys
from bs4 import BeautifulSoup

def get_nums():
	response = requests.get('https://ketqua.vn/')
	if response.status_code == 200:
		result = []
		tree = BeautifulSoup(markup=response.text, features = 'html.parser')
		special = tree.find('td', attrs = {'class': 'txt-special-prize'})
		result.append(special.text.strip()[-2:])
		board = tree.find('div', attrs = {'class': 'result-board'})
		normal_nums = board.findAll('td', attrs = {'class': 'txt-normal-prize'})
		for num in normal_nums:
			result.append(num.text.strip()[-2:])
		return result
	else:
		print("HTTP Error: {}.\nAccess: https://http.cat/ for more information".format(response.status_code))
		return None

your_nums = sys.argv[1:]
results = get_nums()

if results is None:
	print('Khong xem duoc ket qua. Thu lai sau!')
else:
	for num in your_nums:
		if num[-2:] == results[0]:
			print('Ban da trung con de: ', num[-2:])
		elif num[-2:] in results and num[-2:] != results[0]:
			c = results.count(num[-2:])
			print('Con {} ve {} nhay. Chuc mung ban!'.format(num[-2:], c))
		elif num[-2:] not in results:
			print('Con {} khong trung.'.format(num[-2:]))
print('Ket qua hom nay la:')
print(' '.join(results))
		


