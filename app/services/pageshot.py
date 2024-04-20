import time
from selenium import webdriver
from urllib.parse import urlparse

from app import config as conf


driver = webdriver.Firefox()


def pageshot(url: str, user_id: int, date_msg: str):
    url_info = urlparse(url)
    driver.get(url)
    start_processing = time.perf_counter()
    driver.save_screenshot(conf.PATH_PAGESHOT.format(url_info.netloc,
                                                     user_id,
                                                     date_msg))
    finish_processing = time.perf_counter()
    driver.close()
    return str(finish_processing - start_processing)


if __name__ == "__main__":
    pageshot("https://mail.ru/", 3, "65")
