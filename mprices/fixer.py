import requests, json
from bs4 import BeautifulSoup
from .models import Country

url = 'http://data.fixer.io/api/latest?access_key=15b662e7810082c0eef61e7c8aa0353a'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

data=json.loads(str(soup))

data=data['rates']

country = Country.objects.all()

for c in country:
	currency = c.currency
	rate = data[currency]
	c.exchange_rate = rate
	c.save()
	print ('Rates updated for ' + c.country)