import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import Phone

phones = Phone.objects.exclude(gsm_arena__isnull=True).exclude(gsm_arena__exact='')

for p in phones:

	try:

		url = p.gsm_arena
		response = requests.get(url)
		html = response.content
		soup = BeautifulSoup(html, 'html.parser')

		#Table Fields
		os = soup.find(attrs={"data-spec": "os"}).next_element.strip()
		dimensions = soup.find(attrs={"data-spec": "dimensions"}).next_element.strip()
		weight = soup.find(attrs={"data-spec": "weight"}).next_element.strip()
		sim = soup.find(attrs={"data-spec": "sim"}).next_element.strip()
		colors = soup.find(attrs={"data-spec": "colors"}).next_element.strip()
		cpu = soup.find(attrs={"data-spec": "cpu"}).next_element.strip()
		chipset = soup.find(attrs={"data-spec": "chipset"}).next_element.strip()
		gpu = soup.find(attrs={"data-spec": "gpu"}).next_element.strip()
		technology = soup.find(attrs={"data-spec": "displaytype"}).next_element.strip()
		size = soup.find(attrs={"data-spec": "displaysize"}).next_element.strip()
		resolution = soup.find(attrs={"data-spec": "displayresolution"}).next_element.strip()

		try:
			protection = soup.find(attrs={"data-spec": "displayprotection"}).next_element.strip()
		except:
			protection = ''

		builtin = soup.find(attrs={"data-spec": "internalmemory"}).next_element.strip()
		card = soup.find(attrs={"data-spec": "memoryslot"}).next_element.strip()

		main_camera = soup.find(attrs={"data-spec": "cam1modules"}).next_element.strip()
		c_qty = soup.find(attrs={"data-spec": "cam1modules"}).find_previous_sibling().get_text()
		main_camera = c_qty + ', ' + main_camera

		features = soup.find(attrs={"data-spec": "cam1features"}).next_element.strip()
		video = soup.find(attrs={"data-spec": "cam1video"}).next_element.strip()
		features = features + ', ' + video

		front_camera = soup.find(attrs={"data-spec": "cam2modules"}).next_element.strip()
		sensors = soup.find(attrs={"data-spec": "sensors"}).next_element.strip()
		battery = soup.find(attrs={"data-spec": "batdescription1"}).next_element.strip()

		release = soup.find(attrs={"data-spec": "year"}).next_element.strip()
		release = datetime.strptime(release,'%Y, %B')

		"""
		try:
			image = soup.find('div', class_='specs-photo-main')
			image = image.find('img')
			image = image['src']
			image = image.get_text()
		except:
			print(image)
		"""

		list = (os, dimensions, weight, sim, colors, cpu, chipset, gpu, technology, size, resolution, protection, builtin, card, main_camera, features, front_camera, sensors, battery, release)

		p.os = list[0]
		p.dimensions = list[1]
		p.weight = list[2]
		p.sim = list[3]
		p.colors = list[4]
		p.cpu = list[5]
		p.chipset = list[6]
		p.gpu = list[7]
		p.technology = list[8]
		p.size = list[9]
		p.resolution = list[10]
		p.protection = list[11]
		p.builtin = list[12]
		p.card = list[13]
		p.main_camera = list[14]
		p.features = list[15]
		p.front_camera = list[16]
		p.sensors = list[17]
		p.battery = list[18]
		p.release = list[19]
		p.gsm_arena = ''

		p.save()

		print('Record Saved')

	except:
		print('Not Found')