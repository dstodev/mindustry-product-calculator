import typing


class Recipe:
    def __init__(self, product: str, quantity: int, time: float, factory: str, components: typing.List[tuple]):
        self.product = product
        self.quantity = quantity
        self.time = time
        self.factory = factory
        self.components = components

    def rate(self, multiplier: float = 1) -> float:
        output_per_time = (self.quantity / self.time)
        output_per_time *= multiplier
        return output_per_time

    def factories_required(self, rate: float, multiplier: float = 1) -> float:
        return (rate / self.rate(multiplier))

    def component_rates(self, multiplier: float = 1) -> typing.List[tuple]:
        adjusted_components = []

        for component in self.components:
            adjusted_components.append((component[0], (component[1] / (self.time / multiplier))))

        return adjusted_components
