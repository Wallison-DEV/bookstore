import pytest

from product.factories import ProductFactory

@pytest.fixture
def product_published():
    return ProductFactory(title = 'pystr')

@pytest.mark.django_db
def test_create_published_post(product_published):
    assert product_published.title == 'pystr'