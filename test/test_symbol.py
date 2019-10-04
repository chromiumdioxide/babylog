import unittest

from babylog.symbols import Symbol

class SymbolTest(unittest.TestCase):
    def setUp(self):
        self.symbol_first = Symbol('first')
        self.symbol_second = Symbol('second')
        self.symbol_like_first = Symbol('first')

    def test_equality(self):
        self.assertEqual(self.symbol_first, self.symbol_first)
        self.assertNotEqual(self.symbol_first, self.symbol_second)
        self.assertEqual(self.symbol_first, self.symbol_like_first)

    def test_hashing(self):
        self.assertEqual(hash(self.symbol_first), hash(self.symbol_first))
        self.assertNotEqual(hash(self.symbol_first), hash(self.symbol_second))
        self.assertEqual(hash(self.symbol_first), hash(self.symbol_like_first))

    def test_dictionary_insertion(self):
        test_dictionary = dict()
        unique_value = '4dedd392-99f6-41e5-9f01-39da137a9f1a'

        test_dictionary[self.symbol_first] = self.symbol_first.name
        self.assertEqual(len(test_dictionary), 1)
        self.assertEqual(test_dictionary[self.symbol_first], self.symbol_first.name)
        with self.assertRaises(KeyError): test_dictionary[self.symbol_second]
        self.assertEqual(test_dictionary[self.symbol_like_first], self.symbol_first.name)

        test_dictionary[self.symbol_second] = self.symbol_second.name
        self.assertEqual(len(test_dictionary), 2)
        self.assertEqual(test_dictionary[self.symbol_first], self.symbol_first.name)
        self.assertEqual(test_dictionary[self.symbol_second], self.symbol_second.name)
        self.assertEqual(test_dictionary[self.symbol_like_first], self.symbol_first.name)

        test_dictionary[self.symbol_like_first] = unique_value
        self.assertEqual(len(test_dictionary), 2)
        self.assertEqual(test_dictionary[self.symbol_first], unique_value)
        self.assertEqual(test_dictionary[self.symbol_second], self.symbol_second.name)
        self.assertEqual(test_dictionary[self.symbol_like_first], unique_value)

        


