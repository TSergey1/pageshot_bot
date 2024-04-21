import time
from urllib.parse import urlparse

from pyppeteer import launch

from app import config


async def create_pageshot(url: str, chat_id: int, user_id: int, date_msg: str):
    url_info = urlparse(url)
    browser = await launch(
        {'dumpio': True,
         'headless': True,
         'args': ['--no-sandbox', '--disable-setuid-sandbox']}
    )
    page = await browser.newPage()
    await page.goto(url)
    start_processing = time.perf_counter()
    await page.setViewport(dict(width=1280, height=900))
    path_pageshot = config.PATH_PAGESHOT.format(url_info.netloc,
                                                user_id,
                                                date_msg.replace(':', '-'))
    await page.screenshot(path=path_pageshot)
    await browser.close()
    finish_processing = time.perf_counter()
    time_processing: str = str(finish_processing - start_processing)
    return path_pageshot, time_processing, chat_id
