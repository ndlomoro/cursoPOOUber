from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")

    car = car("AMS234", Account ("Andres Herrera", "ANDA876"))
    # car = Car()
    # car.license = "AMS234"
    # car.driver = "Andres Herrera"
    print(vars(car))
    print(vars(car.driver))


    # car2 = Car()
    # car2.license = "QWE567"
    # car2.driver = "Matha"
    # print(vars(car2))

    