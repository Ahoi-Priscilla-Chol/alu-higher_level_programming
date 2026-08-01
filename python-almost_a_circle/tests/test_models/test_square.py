#!/usr/bin/python3
"""Unittest for the Square class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Tests for correct instantiation of the Square class."""

    def setUp(self):
        """Reset the Base private class counter before every test."""
        Base._Base__nb_objects = 0

    def test_basic_instantiation(self):
        """Test size sets both width and height."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_full_instantiation(self):
        """Test size, x, y, id are all correctly set."""
        s = Square(5, 1, 2, 99)
        self.assertEqual(
            (s.size, s.x, s.y, s.id), (5, 1, 2, 99))

    def test_is_instance_of_rectangle(self):
        """Test that Square inherits from Rectangle."""
        s = Square(3)
        self.assertIsInstance(s, Rectangle)

    def test_is_instance_of_base(self):
        """Test that Square inherits from Base."""
        s = Square(3)
        self.assertIsInstance(s, Base)

    def test_id_auto_assigned(self):
        """Test that id auto-increments when not given."""
        s1 = Square(2)
        s2 = Square(2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)


class TestSquareSizeValidation(unittest.TestCase):
    """Tests for the size attribute validation."""

    def test_size_not_int_raises_type_error(self):
        """Test size as a string raises TypeError."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero_raises_value_error(self):
        """Test size of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative_raises_value_error(self):
        """Test negative size raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_set_size_after_init(self):
        """Test size can be updated after instantiation."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_set_size_invalid_after_init(self):
        """Test setting an invalid size later still raises errors."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -3


class TestSquareArea(unittest.TestCase):
    """Tests for the inherited area method."""

    def test_area_basic(self):
        """Test area computation for a square."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_area_after_size_update(self):
        """Test area reflects a size change."""
        s = Square(4)
        s.size = 6
        self.assertEqual(s.area(), 36)


class TestSquareDisplay(unittest.TestCase):
    """Tests for the inherited display method."""

    def test_display_no_offset(self):
        """Test display with x=0 and y=0."""
        s = Square(2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_with_offsets(self):
        """Test display respects x and y offsets."""
        s = Square(2, 1, 1)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), "\n ##\n ##\n")


class TestSquareStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def setUp(self):
        """Reset the Base private class counter before every test."""
        Base._Base__nb_objects = 0

    def test_str_with_id(self):
        """Test string representation with an explicit id."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_str_auto_id(self):
        """Test string representation with an auto-assigned id."""
        s = Square(4)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 4")


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for the update method using *args."""

    def test_update_id_only(self):
        """Test updating only the id via args."""
        s = Square(10, 10, 10, 1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_id_and_size(self):
        """Test updating id and size via args."""
        s = Square(10, 10, 10, 1)
        s.update(89, 2)
        self.assertEqual((s.id, s.size), (89, 2))

    def test_update_all_args(self):
        """Test updating all attributes via args."""
        s = Square(10, 10, 10, 1)
        s.update(89, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 2, 3, 4))

    def test_update_no_args_no_change(self):
        """Test that calling update with no arguments changes nothing."""
        s = Square(10, 10, 10, 1)
        s.update()
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 10, 10, 10))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for the update method using **kwargs."""

    def test_update_kwargs_single(self):
        """Test updating a single attribute via kwargs."""
        s = Square(10, 10, 10, 1)
        s.update(size=2)
        self.assertEqual(s.size, 2)

    def test_update_kwargs_multiple(self):
        """Test updating multiple attributes via kwargs."""
        s = Square(10, 10, 10, 1)
        s.update(x=2, y=3, id=100)
        self.assertEqual((s.x, s.y, s.id), (2, 3, 100))

    def test_update_args_take_priority_over_kwargs(self):
        """Test that when args are given, kwargs are ignored."""
        s = Square(10, 10, 10, 1)
        s.update(50, size=999)
        self.assertEqual((s.id, s.size), (50, 10))


class TestSquareToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_to_dictionary_keys_and_values(self):
        """Test the dictionary has correct keys and values."""
        s = Square(10, 1, 9, 5)
        expected = {"id": 5, "size": 10, "x": 1, "y": 9}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_is_dict_type(self):
        """Test the return type is a dict."""
        s = Square(10)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_to_dictionary_creates_identical_square(self):
        """Test a square built from the dictionary matches original."""
        s1 = Square(10, 1, 9, 5)
        s1_dict = s1.to_dictionary()
        s2 = Square(**s1_dict)
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
