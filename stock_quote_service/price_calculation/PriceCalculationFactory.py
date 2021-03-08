import price_calculation.SimplePriceCalculationEngine as spe


class PriceCalculationFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_price_Calculation_engine(calculator_type):
        if calculator_type == "simple":
            return spe.SimplePriceCalculationEngine()
