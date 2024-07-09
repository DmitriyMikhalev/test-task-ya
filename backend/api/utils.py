import logging
from urllib3 import Retry

import requests
from requests.adapters import HTTPAdapter
from requests import exceptions
from django.conf import settings
from lxml import etree


def get_requests_session(
    retries: int = 3,
    backoff_factor: float = 0.3,
    status_forcelist: tuple[int] = (500, 502, 504)
) -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def get_response(url: str) -> requests.Response | None:
    try:
        with get_requests_session() as session:
            return session.get(url=url)
    except exceptions.RequestException as e:
        logging.info(e)


def get_cbr_rate() -> float | None:
    url = settings.API_URL
    if response := get_response(url=url):
        return retrieve_rate(response.content)

    logging.error("Could not get response from an external API")


def retrieve_rate(xml_content: bytes) -> float | None:
    try:
        root = etree.fromstring(xml_content)
        valute_data = root.xpath(f"Valute [@ID='{settings.API_USD_CODE}']")

        if not valute_data:
            return None

        text_value = valute_data[0].find("Value").text
        rate = text_value.replace(",", ".")

        return float(rate)
    except Exception as e:
        logging.error(e)
