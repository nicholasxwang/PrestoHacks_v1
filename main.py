from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 
start_time = time.time()
options = Options()
options.headless = True
browser = Firefox(executable_path="./geckodriver",options=options)

ignore = [
  "wallpaper",
  "picture",
  "landscape",
  "mac",
  "macos",
  "os",
  "windows",
  "windowsos",
  "linux",
  "linuxos",
  "profile",
  "avatar"
]
def main_program(image):
  a = str(get_image_name(image))
  #Check if it exists
  if a == "n":
    return "Sorry, I could not find any song related to your picture. How about, try Head Up by The Score!"
  #split into words
  word = a.split(" ")
  songs = []
  ignored = []
  for i in word:
    if i.lower() in ignore:
      ignored.append(i.lower())
      continue
    #Find Synonyms
    import nltk
    nltk.download('wordnet')
    from nltk.corpus import wordnet
    synonyms = []
    antonyms = []
      
    for syn in wordnet.synsets(a):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
      
    synonyms = set(synonyms)
    #Search for songs
    synonyms = list(synonyms)
    synonyms = [a]+synonyms
    
    for i in synonyms:
      temp = find_music(i)
      if not (temp=="n"):
        for i in temp:
          songs.append(i.text)

  if len(songs) == 0:
    return "I found what your picture is thanks to my smart AI but I could not find any songs. How about, try AJR's Bang? Synonyms include "+str(synonyms)+"\n We ignored: "+ignored
  else:
    return "Yay! The best result is \""+str(songs[0])+"\" \nOur Synonym list include: " + str(synonyms)+"\nOther results include: "+str(songs[1:len(songs)])+"\n We ignored: "+ignored

def get_image_name(image_url):
  browser.get("https://www.google.com/searchbyimage?site=search&sa=X&image_url="+image_url)
  time.sleep(2)
  try:
    parsed = browser.find_elements_by_class_name("fKDtNb")[0].text
  except Exception as e:
    parsed = "n"
  return parsed

def find_music(query):
  browser.get(f"https://www.musixmatch.com/search/{query}/tracks")
  time.sleep(2)
  try:
    a = browser.find_elements_by_class_name("title")
  except:
    return "n"
  return a
  
link = input("put a link: ")
print(main_program(link))

#Permissions Fix: chmod +x geckodriver