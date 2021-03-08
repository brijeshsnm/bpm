import aiohttp
import os


class WebReferencePriceSource:

    def __init__(self, url):
        self._url = url
        self._logger = LogHelper.get_logger("WebReferencePriceSource")

    async def get_reference_price(self, security_id):
        url = self._url.format(security_id=security_id)
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.request(method='GET', url=url)
                response.raise_for_status()
                price_text = await response.text()
                price = float(price_text)
                return price
        except ValueError:
            self._logger.error(f"An error occurred: {ValueError}")
            return -1
        except Exception as err:
            self._logger.error(f"An error occurred: {err}")
            return -1
