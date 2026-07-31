#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init_width_height(self):
        """width and height are set correctly."""
        r = Rectangle(3, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 2)

    def test_init_defaults_x_y(self):
        """x and y default to 0."""
        r = Rectangle(3, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_init_all_args(self):
        """All arguments are set correctly, including id."""
        r = Rectangle(3, 2, 1, 5, 9)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (3, 2, 1, 5, 9))

    def test_width_not_int_raises_type_error(self):
        """Non-integer width raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("3", 2)

    def test_width_zero_raises_value_error(self):
        """Zero width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative_raises_value_error(self):
        """Negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_height_not_int_raises_type_error(self):
        """Non-integer height raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "2")

    def test_height_zero_raises_value_error(self):
        """Zero height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)

    def test_height_negative_raises_value_error(self):
        """Negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)

    def test_x_not_int_raises_type_error(self):
        """Non-integer x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, "1")

    def test_x_negative_raises_value_error(self):
        """Negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -1)

    def test_y_not_int_raises_type_error(self):
        """Non-integer y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 1, "5")

    def test_y_negative_raises_value_error(self):
        """Negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 1, -5)

    def test_area(self):
        """area() returns width times height."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        """__str__ returns the expected representation."""
        r = Rectangle(3, 2, 1, 5, 9)
        self.assertEqual(str(r), "[Rectangle] (9) 1/5 - 3/2")

    def test_display_basic(self):
        """display() prints a rectangle of '#' with no offset."""
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            r.display()
            self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        """display() applies x and y offsets."""
        r = Rectangle(2, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as output:
            r.display()
            self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_update_args_all(self):
        """update() with all positional args in order."""
        r = Rectangle(3, 2, 1, 5, 9)
        r.update(10, 4, 6, 2, 3)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (10, 4, 6, 2, 3))

    def test_update_args_partial(self):
        """update() with only some positional args."""
        r = Rectangle(3, 2, 1, 5, 9)
        r.update(10, 4)
        self.assertEqual((r.id, r.width), (10, 4))

    def test_update_kwargs(self):
        """update() with keyword arguments."""
        r = Rectangle(3, 2, 1, 5, 9)
        r.update(width=4, height=6)
        self.assertEqual((r.width, r.height), (4, 6))

    def test_to_dictionary(self):
        """to_dictionary() returns the correct dictionary."""
        r = Rectangle(3, 2, 1, 5, 9)
        expected = {"id": 9, "width": 3, "height": 2, "x": 1, "y": 5}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
