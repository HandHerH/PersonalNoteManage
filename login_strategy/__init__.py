from strategies import LoginStrategy
from email_strategy import EmailStrategy

lst = LoginStrategy()

lst.register_strategy('email', EmailStrategy())
