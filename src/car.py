class CarError(Exception):
    """Base exception for car-related errors."""


class OverfillError(CarError):
    """Raised when trying to refuel more than the tank can hold."""

    default_message = "Вы пытаетесь залить слишком много бензина!"

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or self.default_message)


class InsufficientFuelError(CarError):
    """Raised when there is not enough fuel to complete the trip."""

    default_message = "Не доедем жеж..."

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or self.default_message)


class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0.0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise OverfillError()
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        # Считаем, что расход 8 литров на 100 км
        fuel_burned: float = 8 * (distance_km / 100)

        # Если топлива не хватает — поездка невозможна
        if self._fuel_in_tank < fuel_burned:
            raise InsufficientFuelError()

        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
