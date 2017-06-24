import requests

req = requests.get('http://www.google.de')

while True:
	if req.status_code == 200:
		print('**********************************')
		print('* Internet Connection available. *')
		print('**********************************')
		break