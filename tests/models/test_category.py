import pytest

from product.factories import CategoryFactory

@pytest.fixture
def category_published():
    return CategoryFactory(title = 'pystr')

@pytest.mark.django_db
def test_create_published_post(category_published):
    assert category_published.title == 'pystr'