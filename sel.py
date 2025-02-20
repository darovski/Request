from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def setup_driver():
    options = Options()
    options.add_argument('--headless')  # Запуск в фоновом режиме
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path='path/to/chromedriver')  # Укажите путь к chromedriver
    driver = webdriver.Firefox()
    return driver


def search_wikipedia(driver, query):
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    for idx, paragraph in enumerate(paragraphs):
        print(f"Paragraph {idx + 1}: {paragraph.text[:100]}...")  # Выводим первые 100 символов
        next_action = input("Press Enter to continue or 'q' to stop: ")
        if next_action.lower() == 'q':
            break


def list_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    for idx, link in enumerate(links):
        print(f"Link {idx + 1}: {link.get_attribute('title')}")
    return links


def main():
    driver = setup_driver()
    try:
        while True:
            query = input("Enter your search query: ")
            search_wikipedia(driver, query)
            while True:
                print("\nChoose an action:")
                print("1. List paragraphs of the current article")
                print("2. Go to a related page")
                print("3. Exit the program")
                choice = input("Enter your choice: ")

                if choice == "1":
                    list_paragraphs(driver)
                elif choice == "2":
                    links = list_links(driver)
                    link_choice = int(input("Enter the number of the link you want to follow: ")) - 1
                    if 0 <= link_choice < len(links):
                        links[link_choice].click()
                    else:
                        print("Invalid link number.")
                elif choice == "3":
                    print("Exiting the program.")
                    return

                else:
                    print("Invalid choice. Please try again.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()