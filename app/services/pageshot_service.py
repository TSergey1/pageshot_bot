import time
import asyncwhois
from urllib import parse
from urllib.parse import urlparse

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


async def site_info(url: str, value: list[tuple]) -> str:
    """Возвращает информацию о сайте"""
    netloc = urlparse(url).netloc
    _, parsed_dict = await asyncwhois.aio_whois(netloc)

    data = {}

    for key, name in value:
        if key in parsed_dict:
            value = parsed_dict[key]
            if isinstance(value, list):
                value = ", ".join(value[:2])
            data[name] = value

    result_data = []
    for key, value in data.items():
        result_data.append(f"{key}: {value}")

    return "\n".join(result_data)


async def get_site_info(url: str):
    value = [
        ("domain_name", "Даменное имя"),
        ("registrar", "Регистратор"),
        ("creation_date", "Дата создания"),
        ("registrant_organization", "Зарегистрирован"),
    ]
    return await site_info(url, value)


async def get_info_for_foto(url: str, time_processing: str):
    """Возвращает информацию к foto"""
    domain_name = await site_info(url, [("domain_name", "Даменное имя"),])
    return (
        f"{domain_name}\n"
        f"Веб-сайт: {url}\n"
        f"Время обработки: {time_processing} с."
    )
