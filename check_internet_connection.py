import requests

while True:
	req = requests.get('http://www.google.de')
	if req.status_code == 200:
		print('**********************************')
		print('* Internet Connection available. *')
		print('**********************************')
		break