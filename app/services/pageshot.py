
from selenium import webdriver
from urllib.parse import urlparse

import time

driver = webdriver.Firefox()


def pageshot(url: str, user_id: int, date_msg: str):
    url_info = urlparse(url)
    driver.get(url)
    start_processing = time.perf_counter()
    # driver.save_screenshot(
    #     f'pageshots/{url_info.netloc}_{user_id}_{date_msg}.png')
    driver.save_screenshot('pageshots/111.png')
    finish_processing = time.perf_counter()
    driver.close()
    return str(finish_processing - start_processing)


if __name__ == "__main__":
    pageshot("https://mail.ru/", 3, "65")
