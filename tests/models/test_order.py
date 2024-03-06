import pytest

from order.factories import OrderFactory

@pytest.fixture
def order_published():
    return OrderFactory()

@pytest.mark.django_db
def test_create_published_post(order_published):
    assert order_published.user == order_published.user