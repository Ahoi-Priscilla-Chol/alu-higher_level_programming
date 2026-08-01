#!/usr/bin/python3
"""Unittest for the Base class."""
import json
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Reset the Base private class counter before every test."""
        Base._Base__nb_objects = 0

    def test_id_is_public(self):
        """Test that id attribute is set and accessible."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_increments_counter(self):
        """Test id auto-increments when id is None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given_does_not_increment_counter(self):
        """Test that giving an explicit id does not affect the counter."""
        b1 = Base(50)
        b2 = Base()
        self.assertEqual(b1.id, 50)
        self.assertEqual(b2.id, 1)

    def test_id_zero(self):
        """Test that id of 0 is accepted as is (not None)."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test that a negative id is accepted as given."""
        b = Base(-7)
        self.assertEqual(b.id, -7)

    def test_id_string(self):
        """Test that a string id is accepted as given."""
        b = Base("my_id")
        self.assertEqual(b.id, "my_id")

    def test_no_args_raises_type_error(self):
        """Test that Base requires zero or one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_multiple_instances_increment_sequentially(self):
        """Test that multiple default instances get sequential ids."""
        instances = [Base() for _ in range(5)]
        ids = [inst.id for inst in instances]
        self.assertEqual(ids, [1, 2, 3, 4, 5])


class TestBaseToJsonString(unittest.TestCase):
    """Tests for the to_json_string static method."""

    def test_none_returns_empty_brackets(self):
        """Test None returns the string '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list_returns_empty_brackets(self):
        """Test an empty list returns the string '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_return_type_is_str(self):
        """Test the return type is a string."""
        result = Base.to_json_string([{"id": 1}])
        self.assertIsInstance(result, str)

    def test_single_dictionary_content(self):
        """Test the JSON content matches a single dictionary given."""
        d = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        result = Base.to_json_string([d])
        self.assertEqual(json.loads(result), [d])

    def test_multiple_dictionaries_content(self):
        """Test the JSON content matches multiple dictionaries given."""
        d1 = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}
        result = Base.to_json_string([d1, d2])
        self.assertEqual(json.loads(result), [d1, d2])

    def test_callable_without_instance(self):
        """Test the method is callable directly on the class."""
        self.assertEqual(Base.to_json_string([]), "[]")


if __name__ == "__main__":
    unittest.main()
