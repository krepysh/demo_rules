import pytest

from services import RuleBuilder


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
