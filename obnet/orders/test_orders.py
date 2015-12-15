import mock
import unittest

from obnet.orders.orders import OrdersAll

class TestOrders(unittest.TestCase):
    @mock.patch('requests.get'):
    def test_OrdersAll(self, patched):
        OrdersAll('foo', 'asdf', '123456')
        self.assertTrue(patched.called)
