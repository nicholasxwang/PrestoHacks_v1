from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
start_time = time.time()
options = Options()
browser = webdriver.Firefox(executable_path="./geckodriver",options=options)
def main_program(image):
  a = str(get_image_name(image))
  s = ""
  s+=str(a)
  s+="\n Best Match: "
  b = str(find_music(a))
  s+=str(b)
  return s
def get_image_name(image_url):
  browser.get("https://www.google.com/searchbyimage?site=search&sa=X&image_url="+image_url)
  time.sleep(2)
  try:
    parsed = browser.find_elements_by_class_name("fKDtNb")[0].text
  except Exception as e:
    parsed = "No Results! (Exception: "+str(e)+")"
  return parsed
def find_music(query):
  browser.get(f"https://www.musixmatch.com/search/{query}/tracks")
  time.sleep(2)
  a = browser.find_elements_by_class_name("title")[0].text
  return a
  
print(main_program("https://media.discordapp.net/attachments/905242375549509675/919289010122280980/IMG_2872.jpeg"))

#Permissions Fix: chmod +x geckodriver