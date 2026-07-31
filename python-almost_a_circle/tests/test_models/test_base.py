#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_assigned(self):
        """A given id is assigned as-is."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_assigned(self):
        """When id is None, an id is assigned automatically."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_increments_from_previous(self):
        """A new object with no id gets the previous id + 1."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_zero(self):
        """An id of 0 is respected, not treated as None."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """A negative id is accepted as given."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_string(self):
        """A string id is accepted as given."""
        b = Base("my_id")
        self.assertEqual(b.id, "my_id")

    def test_mixed_none_and_given_ids(self):
        """Auto-incrementing ids are independent of explicitly given ids."""
        b1 = Base(100)
        b2 = Base()
        self.assertEqual(b1.id, 100)
        self.assertEqual(b2.id, 1)


if __name__ == '__main__':
    unittest.main()
