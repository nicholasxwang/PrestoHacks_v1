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
  return get_image_name(image)
def get_image_name(image_url):
  browser.get("https://www.google.com/searchbyimage?site=search&sa=X&image_url="+image_url)
  time.sleep(5)
  parsed = browser.find_elements_by_class_name("fKDtNb")[0]
  return parsed
def find_music(query):
  #rishaan
  return #something #RISHAAN CODE HERE literally only like 3 lines of code ://
print(main_program("https://media.discordapp.net/attachments/905242375549509675/919289010122280980/IMG_2872.jpeg?width=1100&height=825"))

#Permissions Fix: chmod +x geckodriver