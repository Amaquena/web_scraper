import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import shutil
from pathlib import Path

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

Path('files/').mkdir(exist_ok=True)

count = 1;
for one_tag in soup.findAll('a'):
	if count > 37:
		link = one_tag['href']
		download_url = 'http://web.mta.info/developers/' + link
		file_name = link[link.find("turnstile_"):]
		with urllib.request.urlopen(download_url) as res, open("files/"+file_name, 'wb') as out_file:
			shutil.copyfileobj(res, out_file)
		time.sleep(1)
		print(file_name, " succesfully downloaded")
	count += 1
