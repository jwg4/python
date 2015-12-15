import mock
import re
import unittest

from obnet.orders.orders import OrdersAll

class TestOrders(unittest.TestCase):
    url_regex = 'https://api.icbit.se/api/orders/all\?key=foo&signature=[A-Z0-9]+&nonce=[0-9]+'

    @mock.patch('requests.get')
    def test_OrdersAll(self, patched):
        OrdersAll('foo', 'asdf', '123456')
        self.assertTrue(patched.called)
        args = patched.call_args[0]
        self.assertTrue(re.match(self.url_regex, args[0]), args[0])
