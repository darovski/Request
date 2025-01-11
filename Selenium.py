from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
print ("Введите Ваш запрос")
search_box = browser.find_element(By.ID, "searchInput")
req = input()
search_box.send_keys(req)
time.sleep(2)
search_box.send_keys(Keys.RETURN)
print ("Что Вы хотите сделать? Нажмите 1, чтобы пролистать параграфы. 2 - перейти по связанной ссылке. 3 - закрыть браузер")
choice = int(input())
if choice == 3:
    browser.quit()
if choice == 1:
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()
if choice == 2:
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "mw-content-ltr mw-parser-output":
            hatnotes.append(element)
            hatnote = random.choice(hatnotes)
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
