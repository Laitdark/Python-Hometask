import sys
sys.path.append('..')
import unittest
import socket
import chat
import time



class TestServer(unittest.TestCase):
    def setUp(self):
        time.sleep(0.5)
        self.s = chat.get_server_socket('localhost', 7777)

    def tearDown(self):
        self.s.close()

    def test_server_socket_is_socket(self):
        self.assertIsInstance(self.s, socket.socket)

    def test_server_socket_addr(self):
        self.assertEqual(self.s.getsockname(), ('127.0.0.1', 7777))


if __name__ == '__main__':
    unittest.main()