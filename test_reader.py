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

    def test_filter_address(self):
        input = """Itupeva street\n80\nVila Mariana\nnear a post office"""
        output = {
            'street': 'Itupeva street',
            'street_num': '80',
            'district': 'Vila Mariana',
            'complement': 'near a post office'
        }
        empty_address = csv_reader.filter_adddress('')
        self.assertIsNone(empty_address)
        valid_address = csv_reader.filter_adddress(input)
        self.assertIsInstance(valid_address, dict)
        self.assertEqual(valid_address, output)
        input_empty_fields = (
            'Itupeva street\n'
            '\n'
            'Vila Mariana\n'
            'near a post office\n'
            'first floor'
        )
        output_empty_fields = {
            'street': 'Itupeva street',
            'street_num': '',
            'district': 'Vila Mariana',
            'complement': 'near a post office - first floor'
        }
        empty_fields_address = csv_reader.filter_adddress(input_empty_fields)
        self.assertEqual(empty_fields_address, output_empty_fields)


if __name__ == '__main__':
    unittest.main()
