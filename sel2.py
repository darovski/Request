from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def open_wikipedia_article(query, driver):
    driver.get("https://en.wikipedia.org")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for index, paragraph in enumerate(paragraphs):
        print(f"\nParagraph {index + 1}: {paragraph.text}")
        user_input = input("\nPress Enter to continue to the next paragraph, or type 'exit' to go back: ")
        if user_input.lower() == 'exit':
            break


def list_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "#bodyContent a")
    for index, link in enumerate(links):
        print(f"{index + 1}: {link.get_attribute('title') or link.text}")
    return links


def main():
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в вашем PATH
    try:
        while True:
            query = input("Enter your Wikipedia search query (or type 'exit' to quit): ")
            if query.lower() == 'exit':
                break

            open_wikipedia_article(query, driver)

            while True:
                action = input(
                    "\nChoose an action: \n1. List paragraphs\n2. Go to a linked article\n3. Exit\nYour choice: ")

                if action == '1':
                    list_paragraphs(driver)
                elif action == '2':
                    links = list_links(driver)
                    link_choice = input(
                        "\nEnter the number of the link you want to follow (or type 'back' to go back): ")
                    if link_choice.lower() == 'back':
                        continue
                    try:
                        link_index = int(link_choice) - 1
                        if 0 <= link_index < len(links):
                            links[link_index].click()
                        else:
                            print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif action == '3':
                    return
                else:
                    print("Invalid choice. Please try again.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()