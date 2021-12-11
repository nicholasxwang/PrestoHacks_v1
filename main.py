import requests
from bs4 import BeautifulSoup as bS
def main_program(image):
  return get_image_name(image)
def get_image_name(image_url):
  myRequest = requests.get("https://www.google.com/searchbyimage?site=search&sa=X&image_url="+image_url)
  parsed = bS(myRequest.text, 'html.parser')
  return parsed
print(main_program("https://cdn.discordapp.com/attachments/905242375549509675/919289010122280980/IMG_2872.jpeg"))


