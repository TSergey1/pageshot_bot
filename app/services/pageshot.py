from selenium import webdriver
# from selenium.webdriver import FirefoxOptions
import whois
import time

driver = webdriver.Firefox()


def pageshot(url: str, user_id: int):
    whois = whois.whois(url)
    driver.get(url)
    start_processing = time.perf_counter()
    driver.save_screenshot(f'pageshots/{msg.date}_{uid}_{url}.png')

    # element = driver.find_element_by_class_name('card-columns')
    # element.screenshot("screenshot_full.png")
    driver.close()


if __name__ =="__main__":
    pageshot("https://mail.ru/")
