import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Загрузка драйвера браузера
driver = webdriver.Chrome()  # Для Chrome, используйте webdriver.Firefox() для Firefox

# Открытие сайта

driver.get("https://songbpm.com/")
result = []
for song in open('data.txt', encoding='utf8'):
    song = " ".join(song.strip().split())
    try:
        search_box = driver.find_element(By.XPATH, "//honox-island//input")
        search_box.send_keys(song)
        search_box.send_keys(Keys.ENTER)

        href = driver.find_elements(By.XPATH, "//div//a")[1].get_attribute('href')
        bpm = driver.find_elements(By.XPATH, "//div//a//span")[5].text

        result.append((bpm, href))
        print((bpm, href))
    except:
        print('error')

# Подождать загрузки результатов поиска (необязательно)
# import time
# time.sleep(5)

# Закрыть браузер
driver.quit()

with open('res.txt', 'w', encoding='utf8') as f:
    json.dump(result, f, ensure_ascii=False)