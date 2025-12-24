from src.car import Car


def test_car_init_sets_fuel_zero():
    car = Car("BMW", 50)
    assert car.get_current_fuel_level() == 0
