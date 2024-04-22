import json
import socket
import time
from urllib import parse, request

from pyppeteer import launch

from app import config


async def create_pageshot(url: str, user_id: int, date_msg: str):
    url_info = parse.urlparse(url)
    browser = await launch(
        {'dumpio': True,
         'headless': True,
         'args': ['--no-sandbox', '--disable-setuid-sandbox']}
    )
    page = await browser.newPage()
    start_time = time.perf_counter()
    await page.goto(url)
    await page.setViewport(dict(width=1280, height=900))
    path_pageshot = config.PATH_PAGESHOT.format(url_info.netloc,
                                                user_id,
                                                date_msg.replace(':', '-'))
    await page.screenshot(path=path_pageshot)
    await browser.close()
    finish_time = time.perf_counter()
    time_processing: str = "{:.2f}".format(finish_time - start_time)
    return path_pageshot, time_processing


def get_site_info(url: str):
    """Возвращает информацию о сайте"""
    ip = socket.gethostbyname(url)
    url_ip = f'http://ipinfo.io/{ip}/json' 
    data = json.load(request.urlopen(url_ip))
    org = data.get("org")
    city = data.get("city")
    country = data.get("country")
    timezone = data.get("timezone")
    return (
        f"ip -{ip}, "
        f"org -{org}, "
        f"city -{city}, "
        f"country -{country}, "
        f"timezone -{timezone}"
    )
