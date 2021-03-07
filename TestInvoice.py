import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


def test_addProduct(invoice, products):
    invoice.item = invoice.addProduct(products['Pen']['qnt'],
                                      products['Pen']['unit_price'],
                                      products['Pen']['discount'])
    assert invoice.item['qnt'] == products['Pen']['qnt']
    assert invoice.item['unit_price'] == products['Pen']['unit_price']
    assert invoice.item['discount'] == products['Pen']['discount']


def test_changeProductQnt(invoice, products):
    test_addProduct(invoice, products)
    invoice.changeProductQnt('15')

    assert invoice.item['qnt'] == '15'
