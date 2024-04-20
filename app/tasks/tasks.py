# import asyncio
import time
from pyppeteer import launch
# from selenium import webdriver
from urllib.parse import urlparse

from app import config
# from app.misc.msg import SEND_PAGESHOT
# # from app.tasks.celery import celery_worker

# driver = webdriver.Firefox()


# @celery_worker.task(name="create_pageshot")
# def create_pageshot(url: str, chat_id: int, user_id: int, date_msg: str):
#     driver = webdriver.Firefox()
#     url_info = urlparse(url)
#     driver.get(url)
#     start_processing = time.perf_counter()
#     path_pageshot = conf.PATH_PAGESHOT.format(url_info.netloc,
#                                               user_id,
#                                               date_msg)
#     driver.save_screenshot(path_pageshot)
#     finish_processing = time.perf_counter()
#     driver.close()
#     time_processing: str = str(finish_processing - start_processing)
#     return path_pageshot, time_processing, chat_id


# @celery_worker.task(name="update_message")
# async def handlers_bot(path_pageshot: str, time_processing: str,
#                        chat_id: int, bot):
#     pageshot = open(path_pageshot, 'rb')
#     await bot.send_photo(chat_id, pageshot, caption=SEND_PAGESHOT)


async def create_pageshot(url: str, chat_id: int, user_id: int, date_msg: str):
    url_info = urlparse(url)
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    start_processing = time.perf_counter()
    await page.setViewport(dict(width=1280, height=900))
    path_pageshot = config.PATH_PAGESHOT.format(url_info.netloc,
                                                user_id,
                                                date_msg)
    await page.screenshot(path="path_pageshot.png")
    await browser.close()
    finish_processing = time.perf_counter()
    time_processing: str = str(finish_processing - start_processing)
    return path_pageshot, time_processing, chat_id
