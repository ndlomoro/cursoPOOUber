from account import Account


class Car:
    id = int
    licence = str
    driver = Account("","")
    passegenger = int


    def __init__(self, licence, driver):
        self.license = licence
        self.driver = driver
        