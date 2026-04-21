import unittest
from dictionary_bst import DictionaryBST


class TestDictionaryBST(unittest.TestCase):
    def test_insert_and_search_single_word(self):
        """Test that inserting one word allows it to be found with search()."""
        dictionary = DictionaryBST()
        dictionary.insert("banana", "A yellow tropical fruit.")
        self.assertEqual(dictionary.search("banana"), "A yellow tropical fruit.")

    def test_search_missing_word_returns_none(self):
        """Test that searching for a missing word returns None."""
        dictionary = DictionaryBST()
        dictionary.insert("banana", "A yellow tropical fruit.")
        self.assertIsNone(dictionary.search("apple"))

    def test_print_alphabetical_returns_sorted_entries(self):
        """Test that print_alphabetical() returns entries in sorted word order."""
        dictionary = DictionaryBST()
        dictionary.insert("banana", "A yellow tropical fruit.")
        dictionary.insert("apple", "A fruit that grows on trees.")
        dictionary.insert("cherry", "A small, round, red fruit.")

        expected = [
            ("apple", "A fruit that grows on trees."),
            ("banana", "A yellow tropical fruit."),
            ("cherry", "A small, round, red fruit.")
        ]
        self.assertEqual(dictionary.print_alphabetical(), expected)

    def test_duplicate_word_updates_meaning(self):
        """Test that inserting a duplicate word updates its meaning instead of adding a new entry."""
        dictionary = DictionaryBST()
        dictionary.insert("apple", "A fruit.")
        dictionary.insert("apple", "A red or green fruit.")

        self.assertEqual(dictionary.search("apple"), "A red or green fruit.")
        self.assertEqual(
            dictionary.print_alphabetical(),
            [("apple", "A red or green fruit.")]
        )

    def test_constructor_with_entries(self):
        """Test that the constructor inserts all provided entries correctly."""
        entries = {
            "banana": "A yellow tropical fruit.",
            "apple": "A fruit that grows on trees.",
            "cherry": "A small, round, red fruit."
        }

        dictionary = DictionaryBST(entries)

        self.assertEqual(dictionary.search("banana"), "A yellow tropical fruit.")
        self.assertEqual(dictionary.search("apple"), "A fruit that grows on trees.")
        self.assertEqual(dictionary.search("cherry"), "A small, round, red fruit.")

    def test_constructor_entries_print_alphabetical(self):
        """Test that constructor-loaded entries are returned in alphabetical order."""
        entries = {
            "banana": "A yellow tropical fruit.",
            "apple": "A fruit that grows on trees.",
            "cherry": "A small, round, red fruit."
        }

        dictionary = DictionaryBST(entries)

        expected = [
            ("apple", "A fruit that grows on trees."),
            ("banana", "A yellow tropical fruit."),
            ("cherry", "A small, round, red fruit.")
        ]
        self.assertEqual(dictionary.print_alphabetical(), expected)

    def test_print_alphabetical_empty_tree(self):
        """Test that print_alphabetical() returns an empty list for an empty tree."""
        dictionary = DictionaryBST()
        self.assertEqual(dictionary.print_alphabetical(), [])

    def test_search_empty_tree(self):
        """Test that searching an empty tree returns None."""
        dictionary = DictionaryBST()
        self.assertIsNone(dictionary.search("anything"))

    def test_multiple_insertions_balance_case_still_searchable(self):
        """Test that multiple insertions remain searchable after balancing operations."""
        dictionary = DictionaryBST()
        words = [
            ("dog", "An animal."),
            ("cat", "A pet."),
            ("apple", "A fruit."),
            ("zebra", "A striped animal."),
            ("banana", "A yellow fruit."),
            ("yak", "A hairy animal."),
            ("carrot", "A vegetable.")
        ]

        for word, meaning in words:
            dictionary.insert(word, meaning)

        for word, meaning in words:
            self.assertEqual(dictionary.search(word), meaning)

    def test_alphabetical_order_with_more_words(self):
        """Test alphabetical output with a larger set of inserted words."""
        dictionary = DictionaryBST()
        dictionary.insert("mango", "A tropical fruit.")
        dictionary.insert("apple", "A fruit.")
        dictionary.insert("pear", "A green fruit.")
        dictionary.insert("banana", "A yellow fruit.")
        dictionary.insert("grape", "A small fruit.")

        expected = [
            ("apple", "A fruit."),
            ("banana", "A yellow fruit."),
            ("grape", "A small fruit."),
            ("mango", "A tropical fruit."),
            ("pear", "A green fruit.")
        ]

        self.assertEqual(dictionary.print_alphabetical(), expected)


if __name__ == "__main__":
    unittest.main()