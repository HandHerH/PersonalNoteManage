from login_strategy.strategies import LoginStrategy
from login_strategy.email_strategy import EmailStrategy

lst = LoginStrategy()

lst.register_strategy('email', EmailStrategy())
