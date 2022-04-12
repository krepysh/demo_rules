import contextlib
from dataclasses import dataclass
from typing import Callable, Any


@dataclass(frozen=True)
class Product:
    title: str
    price: float
    color: str
    sku: str
    category: int
    product_type: str


class Match:
    conditions: dict[str, Callable[..., bool]] = {
        'more': lambda x, y: x > y,
        'less': lambda x, y: x < y,
        'equal': lambda x, y: x == y,
        'more_or_equal': lambda x, y: x >= y,
        'less_or_equal': lambda x, y: x <= y,
        'contain': lambda x, y: y in x,
        'startswith': lambda x, y: str(x).startswith(y),
        'endswith': lambda x, y: str(x).endswith(y),
    }

    def __init__(self, attribute_name: str, condition: str, value: str | float | int) -> None:
        self.text_condition = condition
        self.condition = self.conditions[condition]
        self.attribute_name = attribute_name
        self.value_for_condition = value

    @staticmethod
    def return_false_in_case_of_exceptions(  # noqa: FNE005
            fn: Callable[..., bool], attribute_value: Any, argument: Any,
    ) -> bool:
        result = False
        with contextlib.suppress(Exception):
            result = fn(attribute_value, argument)
        return result

    def is_match(self, product: Product) -> bool:
        product_value = getattr(product, self.attribute_name)
        return self.return_false_in_case_of_exceptions(
            self.condition, product_value, self.value_for_condition,
        )


class Action:
    def __init__(self, discount_size: int | float):
        self._discount_size = discount_size

    def discounted_price(self, product: Product) -> float:
        return product.price - self._discount_size


class Rule:
    def __init__(self, match: Match, action: Action):
        self.match = match
        self.action = action

    def apply(self, product: Product) -> float:
        if self.match.is_match(product):
            return self.action.discounted_price(product)
        return product.price
