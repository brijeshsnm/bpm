from .PriceListener import PriceListener


class SimpleCachePriceManager:

    def __init__(self, price_listener):
        self._cache = {}
        self._price_listener = price_listener
        self._price_listener.register(self, self.update_security)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._price_listener.unregister(self)

    def get_security(self, security_id):
        if security_id not in self._cache:
            return None
        else:
            return self._cache[security_id]

    def build_price_cache(self):
        # pull from database
        self._cache = {
            '123': 500,
            '456': 800,
            '1': 600,
        }

    def update_security(self, security_id, price):
        if security_id in self._cache:
            self._cache[security_id] = price
