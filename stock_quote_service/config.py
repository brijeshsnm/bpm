host = {"server": "127.0.0.1", "port": 5000}

price_calculation_engine = {"type": "simple"}

reference_price = {"type": "web", "url": "http://localhost:5500/get_price?security_id={security_id}"}

log = {"file_path": "stock_quote_service.log"}