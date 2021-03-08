
class PriceListener:
    def __init__(self):
        self.subscribers = {}

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update_price')
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def price_changed(self, security_id, price):
        for subscriber, callback in self.subscribers.items():
            callback(security_id, price)