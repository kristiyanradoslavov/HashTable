from unittest import TestCase, main

from HashTable import HashTable


class TestHashTable(TestCase):

    def setUp(self):
        self.table = HashTable()

    def test_initialising(self):
        self.assertEqual(4, self.table.capacity)
        self.assertEqual([None, None, None, None], self.table.keys)
        self.assertEqual([None, None, None, None], self.table.values)

    def test_getitem_wrong_input(self):
        with self.assertRaises(KeyError) as ke:
            result = self.table["something_missing"]

    def test_getitem_correct_input(self):
        self.table["something"] = "new"
        result = self.table["something"]
        expected = "new"

        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
