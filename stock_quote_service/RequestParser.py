class RequestParser:

    def __init__(self):
        self.security_id = None
        self.quantity = None
        self.transaction_type = None
        self.error = ''

    def parse(self, data):
        req_data = data.decode("utf-8")
        input_parameters = req_data.split()

        if len(input_parameters) != 3:
            self.error = 'Error: Not enough input'
            return False

        self.security_id, self.transaction_type, self.quantity = input_parameters
        if not self.quantity.isnumeric():
            self.error = 'Error: Quantity must be integer'
            return False
        if self.transaction_type.lower() not in ['buy', 'sell']:
            self.error = 'Error: Transaction type must be buy or sell'
            return False
        self.quantity = float(self.quantity)
        return True
