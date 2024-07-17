import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()

browser.get("http://www.google.com") #Sitelere istek göderirirken kullanılır
arama= browser.find_element(By.ID,"APjFqb")
arama.send_keys("yapay zeka")
arama.send_keys(Keys.ENTER) #enter ile arama ayptık

gorseller= browser.find_element(By.XPATH,"//*[@id=\"hdtb-sc\"]/div/div/div[1]/div/div[2]/a")
gorseller.send_keys(Keys.ENTER) #enter ile arama ayptık

browser.set_window_size(800,600)
browser.refresh() #Bunun sayesinde sayfanın yenilenmesini sağlar

#hdtb-sc > div > div > div.crJ18e > div > div:nth-child(2) > a
#//*[@id="hdtb-sc"]/div/div/div[1]/div/div[3]/a

#APjFqb
input()