from typing import Callable

import pytest

from app.services import RuleBuilder, SerializedRule

rule_builder = RuleBuilder()


@pytest.mark.parametrize(
    'key, key_type, expected',
    [
        ('key_str', str, True),
        ('key_int', int, True),
        ('un_exist_key', str, False),
    ],
)
def test_is_key_exist_in_dict(key: str, key_type: type, expected: bool) -> None:
    dict_to_check = {
        'key_str': 'str',
        'key_int': 1,
        'key_none': None,
    }
    assert rule_builder.is_key_exist_in_dict(key, key_type, dict_to_check) == expected


def test_builded_rule(product_with_price: Callable) -> None:
    raw_rule: SerializedRule = {
        'match': {'attribute_name': 'price', 'condition': 'less', 'attribute_value': 50},
        'action': {'absolute_discount': 10},
    }
    product = product_with_price(40)
    rule = RuleBuilder().build_rule(raw_rule)
    assert rule.apply(product) == 30
