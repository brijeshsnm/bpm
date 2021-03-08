from flask import Flask, request
from price_sources.SimpleCachePriceManager import SimpleCachePriceManager
from price_sources.PriceListener import PriceListener

app = Flask(__name__)
price_listener = PriceListener()
price_manager = SimpleCachePriceManager(price_listener)
price_manager.build_price_cache()


@app.route('/get_price', methods=['GET', 'POST'])
def get_price():
    security_id = request.args.get('security_id')
    price = price_manager.get_security(security_id)
    if price is not None:
        return str(price)
    else:
        return str(-1)


# end point to receive price updates
@app.route('/update_price', methods=['GET', 'POST'])
def update_price():
    security_id = request.args.get('security_id')
    price = long(request.args.get('price'))
    price_listener.price_changed(security_id, price)


@app.route('/ping', methods=['GET', 'POST'])
def test():
    return "hello"
