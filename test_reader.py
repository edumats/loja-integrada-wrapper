import unittest
import csv_reader


class TestCSVReader(unittest.TestCase):
    def setUp(self):
        pass

    def test_states(self):
        state = csv_reader.find_state('São Paulo')
        self.assertEqual(state, 'SP')
        not_state = csv_reader.find_state('Sp')
        self.assertIsNone(not_state)

    def test_address_filter(self):
        pass


if __name__ == '__main__':
    unittest.main()
