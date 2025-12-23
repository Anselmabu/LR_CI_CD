class FuelOverflowError(Exception):
    """Ошибка переполнения бака."""

    def __init__(self) -> None:
        super().__init__("Попытка залить больше топлива, чем вмещает бак.")


class NotEnoughFuelError(Exception):
    """Ошибка недостатка топлива."""

    def __init__(self) -> None:
        super().__init__("Недостаточно топлива для поездки.")


class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0.0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise FuelOverflowError
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        fuel_burned: float = 8 * (distance_km / 100)

        if self._fuel_in_tank < fuel_burned:
            raise NotEnoughFuelError

        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()

