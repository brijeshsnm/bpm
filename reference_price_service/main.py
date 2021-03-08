from waitress import serve
import price_service
import config as cfg
from price_sources.SimpleCachePriceManager import SimpleCachePriceManager
from price_sources.PriceListener import PriceListener

if __name__ == '__main__':
    serve(price_service.app, host=cfg.host['server'], port=cfg.host['port'])


