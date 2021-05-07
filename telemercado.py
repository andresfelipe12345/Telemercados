import requests
from typing import Dict


URL = "https://www.telemercados.cl/api/catalog_system/pub/products/search?fq=C:349&_from=1&_to=49"


def request_url(url: str) -> list:
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.json()
    except requests.exceptions.HTTPError:
        return []


def generate_object(request_result: list) -> Dict:
    result = {
        elements["brand"]: {
            "totalProducts": sum(
                [1 for keys in request_result if keys["brand"] == elements["brand"]]
            ),
            "products": [
                {
                    "productName": keys["productName"],
                    "brand": keys["brand"],
                    "link": keys["link"],
                }
                for keys in request_result
                if keys["brand"] == elements["brand"]
            ],
        }
        for elements in request_result
    }
    return result


def example_usage() -> Dict:
    result = request_url(URL)
    return generate_object(result)

example_usage()
