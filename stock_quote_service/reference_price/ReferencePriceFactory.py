import reference_price.WebReferencePriceSource as rp


class ReferencePriceFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_reference_price_source(source_config):
        if source_config['type'] == 'web':
            return rp.WebReferencePriceSource(source_config['url'])
