from main import *

def test_calculate_total_price():
    products = [
        {"name": "Pen", "price": 1.0, "stock": 10},
        {"name": "Notebook", "price": 2.5, "stock": 5},
        {"name": "Bag", "price": 10.0, "stock": 2}
    ]
    assert calculate_total_price(products) == 13.5


def test_apply_discount_percent():
    result = apply_discount(100, 20)
    assert result == 80


def test_apply_discount_decimal():
    result = apply_discount(50, 0.1)
    assert result == 45


def test_update_stock_reduces_correct_product():
    products = [
        {"name": "Pencil", "price": 1.0, "stock": 10},
        {"name": "Eraser", "price": 0.5, "stock": 20}
    ]

    update_stock(products, "Pencil", 3)

    assert products[0]["stock"] == 7
    assert products[1]["stock"] == 20


def test_get_average_price():
    products = [
        {"name": "A", "price": 2, "stock": 1},
        {"name": "B", "price": 4, "stock": 1}
    ]

    assert get_average_price(products) == 3


def test_update_stock_invalid_product():
    products = [
        {"name": "Marker", "price": 1.5, "stock": 10}
    ]

    update_stock(products, "Pen", 5)

    assert products[0]["stock"] == 10


def test_no_negative_stock():
    products = [
        {"name": "Book", "price": 5, "stock": 3}
    ]

    update_stock(products, "Book", 10)

    assert products[0]["stock"] >= 0
