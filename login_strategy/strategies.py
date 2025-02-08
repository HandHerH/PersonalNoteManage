class LoginStrategy:
    def __init__(self):
        self.strategies = {}

    def register_strategy(self, strategy_name, login_way):
        self.strategies[strategy_name] = login_way

    def get_strategy(self, strategy_name):
        return self.strategies.get(strategy_name)
