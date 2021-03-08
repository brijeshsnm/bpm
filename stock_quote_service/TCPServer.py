import asyncio
from price_calculation.PriceCalculationFactory import PriceCalculationFactory
from reference_price.ReferencePriceFactory import ReferencePriceFactory
import config as cfg
from RequestParser import RequestParser
import LogHelper


class TCPServer:

    def __init__(self):
        self._price_engine = PriceCalculationFactory.get_price_Calculation_engine(
            cfg.price_calculation_engine["type"])
        self._price_source = ReferencePriceFactory.get_reference_price_source(cfg.reference_price)
        self._logger = LogHelper.get_logger("TCPServer")

    async def data_received(self, data, writer):
        try:
            req_parser = RequestParser()
            if not req_parser.parse(data):
                message_bytes = str.encode(req_parser.error)
                writer.write(message_bytes)
            print(req_parser.security_id, req_parser.transaction_type, req_parser.quantity)
            reference_price = await self._price_source.get_reference_price(req_parser.security_id)
            print(reference_price)
            if reference_price < 0:
                message_bytes = str.encode("Error: Price not found for stock")
                writer.write(message_bytes)
            calculated_price = self._price_engine.calculate_price(
                req_parser.security_id, reference_price, req_parser.transaction_type, req_parser.quantity)
            message_bytes = str.encode(str(calculated_price))
            writer.write(message_bytes)
        except Exception as err:
            self._logger.error(f"An error occurred: {err}")


    async def start_server(self, reader, writer):
        while True:
            data = await reader.read(100)  # Max number of bytes to read
            if not data:
                break
            await self.data_received(data, writer)
            await writer.drain()
        writer.close()
