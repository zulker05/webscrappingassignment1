from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests
# using time module
import time

# ts stores the time in seconds
ts = time.time()

html_page = requests.get("https://stackoverflow.com/jobs")
html_image = urllib3.PoolManager()
url = "https://stackoverflow.com/jobs"
soup = BeautifulSoup(html_page.content, "html.parser")
file = open('jobs\joblisting'+str(ts)+'.txt', 'w')
# Text Content Body
#print("Body: Job Lisiting ")
for textcontent in soup.find_all(["div"], class_="js-result"):
	#print(textcontent.text)
	file.write(textcontent.find(["a"], class_="s-link").text)
	file.write("\n")


file.close()