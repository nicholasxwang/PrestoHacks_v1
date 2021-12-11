import requests
from bs4 import BeautifulSoup as bS
def main_program():
  return get_image_name
def get_image_name(image_url):
  myRequest = requests.get("https://www.google.com/searchbyimage?site=search&sa=X&image_url="+image_url)
  parsed = bS(myRequest.text, 'html.parser')
  return parsed
  


