import domain
import pytest


product: domain.Product = domain.Product(
    title='Smart watch', price=20, color='black', sku='SWATCH0002', category=134, product_type='',
)


def test_match() -> None:
    matcher: domain.Match = domain.Match(attribute_name='price', condition='less', value=10)
    assert not matcher.is_match(product)


@pytest.mark.parametrize(
    'match_slug, match_result',
    [
        ('less', False),
        ('more', False),
        ('equal', True),
        ('less_or_equal', True),
        ('more_or_equal', True),
    ],
)
def test_all_valid_numeric_match_types(match_slug: str, match_result: bool) -> None:
    matcher: domain.Match = domain.Match(attribute_name='price', condition=match_slug, value=20)
    assert matcher.is_match(product) == match_result


@pytest.mark.parametrize(
    'match_slug, match_result',
    [
        ('startswith', True),
        ('endswith', False),
        ('contain', True),
    ],
)
def test_all_valid_string_match_types(match_slug: str, match_result: bool) -> None:
    match = domain.Match(attribute_name='title', condition=match_slug, value='Smart')
    assert match.is_match(product) == match_result


def test_invalid_match_type() -> None:
    with pytest.raises(KeyError):
        domain.Match(attribute_name='title', condition='invalid_slug', value='smart')


def test_action() -> None:
    action = domain.Action(discount_size=10)
    assert action.discounted_price(product) == 10


def test_rule() -> None:
    match = domain.Match(attribute_name='title', condition='startswith', value='Smart')
    action = domain.Action(discount_size=10)
    rule = domain.Rule(match=match, action=action)
    assert rule.apply(product) == 10
