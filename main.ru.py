import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#WebDriverWait(webdriver, 60).until(EC.presence_of_element_located((By.ID, "someElementID")))


# Инициализация веб-драйвера
driver = webdriver.Firefox()
#driver.set_page_load_timeout(30)

# Открытие веб-страницы
url = "https://www.divan.ru/ekaterinburg/category/svet"

driver.get(url)
time.sleep(5)

# Ожидание загрузки страницы
#time.sleep(30)

# Поиск элементов
svet = driver.find_elements(By.CLASS_NAME, '_Ud0k U4KZV')
parsed_data = []

for lampa in svet:
    try:
        # Извлечение данных
        title = lampa.find_element(By.CSS_SELECTOR, 'span.ui-GPFV8').text
        price = lampa.find_element(By.CSS_SELECTOR, 'span.q5Uds').text
        link = lampa.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')

        # Добавление данных в список
        parsed_data.append([title, price, link])
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

# Закрытие браузера
driver.quit()

# Запись данных в CSV
with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название изделия', 'Цена изделия', 'Ссылка на изделие'])
    writer.writerows(parsed_data)