#!/usr/bin/python3
"""Unittest for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_is_rectangle_subclass(self):
        """Square inherits from Rectangle."""
        s = Square(3)
        self.assertIsInstance(s, Rectangle)

    def test_init_size(self):
        """size sets both width and height."""
        s = Square(5)
        self.assertEqual((s.width, s.height, s.size), (5, 5, 5))

    def test_init_defaults(self):
        """x and y default to 0."""
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_init_all_args(self):
        """All arguments are set correctly, including id."""
        s = Square(5, 1, 2, 9)
        self.assertEqual((s.size, s.x, s.y, s.id), (5, 1, 2, 9))

    def test_size_not_int_raises_type_error(self):
        """Non-integer size raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_zero_raises_value_error(self):
        """Zero size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_setter(self):
        """The size setter updates both width and height."""
        s = Square(5)
        s.size = 8
        self.assertEqual((s.width, s.height, s.size), (8, 8, 8))

    def test_area(self):
        """area() returns size squared."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        """__str__ returns the expected representation."""
        s = Square(5, 1, 2, 9)
        self.assertEqual(str(s), "[Square] (9) 1/2 - 5")

    def test_update_args_all(self):
        """update() with all positional args in order."""
        s = Square(5, 1, 2, 9)
        s.update(10, 6, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (10, 6, 3, 4))

    def test_update_args_partial(self):
        """update() with only some positional args."""
        s = Square(5, 1, 2, 9)
        s.update(10, 6)
        self.assertEqual((s.id, s.size), (10, 6))

    def test_update_kwargs(self):
        """update() with keyword arguments."""
        s = Square(5, 1, 2, 9)
        s.update(size=7, x=3)
        self.assertEqual((s.size, s.x), (7, 3))

    def test_to_dictionary(self):
        """to_dictionary() returns the correct dictionary."""
        s = Square(5, 1, 2, 9)
        expected = {"id": 9, "size": 5, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
