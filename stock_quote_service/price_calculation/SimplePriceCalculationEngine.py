
class SimplePriceCalculationEngine:

    def __init__(self):
        pass

    def calculate_price(self,  security_id,  reference_price, transaction_type, quantity):
        return quantity * reference_price
