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
		try:
			os = soup.find(attrs={"data-spec": "os"}).next_element.strip()
		except:
			os = ''
		try:
			dimensions = soup.find(attrs={"data-spec": "dimensions"}).next_element.strip()
		except:
			dimensions = ''
		try:
			weight = soup.find(attrs={"data-spec": "weight"}).next_element.strip()
		except:
			weight = ''
		try:
			sim = soup.find(attrs={"data-spec": "sim"}).next_element.strip()
		except:
			sim = ''
		try:
			colors = soup.find(attrs={"data-spec": "colors"}).next_element.strip()
		except:
			colors = ''
		try:
			cpu = soup.find(attrs={"data-spec": "cpu"}).next_element.strip()
		except:
			cpu = ''
		try:
			chipset = soup.find(attrs={"data-spec": "chipset"}).next_element.strip()
		except:
			chipset = ''
		try:
			gpu = soup.find(attrs={"data-spec": "gpu"}).next_element.strip()
		except:
			gpu = ''
		try:
			technology = soup.find(attrs={"data-spec": "displaytype"}).next_element.strip()
		except:
			technology = ''
		try:
			size = soup.find(attrs={"data-spec": "displaysize"}).next_element.strip()
		except:
			size = ''
		try:
			resolution = soup.find(attrs={"data-spec": "displayresolution"}).next_element.strip()
		except:
			resolution = ''
		try:
			protection = soup.find(attrs={"data-spec": "displayprotection"}).next_element.strip()
		except:
			protection = ''
		try:
			builtin = soup.find(attrs={"data-spec": "internalmemory"}).next_element.strip()
		except:
			builtin = ''
		try:
			card = soup.find(attrs={"data-spec": "memoryslot"}).next_element.strip()
		except:
			card = ''
		try:
			main_camera = soup.find(attrs={"data-spec": "cam1modules"}).next_element.strip()
		except:
			main_camera = ''
		try:
			c_qty = soup.find(attrs={"data-spec": "cam1modules"}).find_previous_sibling().get_text()
		except:
			c_qty = ''
		main_camera = c_qty + ', ' + main_camera
		try:
			features = soup.find(attrs={"data-spec": "cam1features"}).next_element.strip()
		except:
			features = ''
		try:
			video = soup.find(attrs={"data-spec": "cam1video"}).next_element.strip()
		except:
			video = ''
		features = features + ', ' + video
		try:
			front_camera = soup.find(attrs={"data-spec": "cam2modules"}).next_element.strip()
		except:
			front_camera = ''
		try:
			sensors = soup.find(attrs={"data-spec": "sensors"}).next_element.strip()
		except:
			sensors = ''
		try:
			battery = soup.find(attrs={"data-spec": "batdescription1"}).next_element.strip()
		except:
			battery = ''
			
		"""
		This date code is fuctional and working

		release = soup.find(attrs={"data-spec": "year"}).next_element.strip()
		release = datetime.strptime(release,'%Y, %B')

		This code snippet for image is not tested

		try:
			image = soup.find('div', class_='specs-photo-main')
			image = image.find('img')
			image = image['src']
			image = image.get_text()
		except:
			print(image)
		"""

		list = (os, dimensions, weight, sim, colors, cpu, chipset, gpu, technology, size, resolution, protection, builtin, card, main_camera, features, front_camera, sensors, battery)

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
		p.gsm_arena = ''
		p.save()

		model = p.phone_model.title()
		print(model + '   ======= Data Saved')
	except:
		model = p.phone_model.title()
		print(model + '   ======= Data Not Found')