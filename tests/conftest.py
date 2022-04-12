import pytest

from app import domain


@pytest.fixture
def product_with_price():
    def product_fabric(price: int | float) -> domain.Product:
        return domain.Product('Product', price, 'black', 'sk', 0, 'abstract')
    return product_fabric
