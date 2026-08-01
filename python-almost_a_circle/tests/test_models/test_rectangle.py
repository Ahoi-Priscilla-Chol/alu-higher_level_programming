#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import json
import os
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for correct instantiation of the Rectangle class."""

    def setUp(self):
        """Reset the Base private class counter before every test."""
        Base._Base__nb_objects = 0

    def test_basic_instantiation(self):
        """Test width/height/x/y are correctly set."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_full_instantiation(self):
        """Test all four positional args plus id."""
        r = Rectangle(10, 2, 1, 2, 99)
        expected = (10, 2, 1, 2, 99)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), expected)

    def test_is_instance_of_base(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_id_auto_assigned(self):
        """Test that id auto-increments when not given."""
        r1 = Rectangle(2, 2)
        r2 = Rectangle(2, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)


class TestRectangleWidthValidation(unittest.TestCase):
    """Tests for the width attribute validation."""

    def test_width_not_int_str(self):
        """Test width as a string raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_not_int_float(self):
        """Test width as a float raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10.5, 2)

    def test_width_not_int_none(self):
        """Test width as None raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_width_zero_raises_value_error(self):
        """Test width of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_negative_raises_value_error(self):
        """Test negative width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-3, 2)

    def test_width_error_message(self):
        """Test the exact error message for invalid width type."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([], 2)


class TestRectangleHeightValidation(unittest.TestCase):
    """Tests for the height attribute validation."""

    def test_height_not_int(self):
        """Test height as a string raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_height_zero_raises_value_error(self):
        """Test height of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_height_negative_raises_value_error(self):
        """Test negative height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, -1)

    def test_height_error_message(self):
        """Test the exact error message for invalid height value."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -1)


class TestRectangleXValidation(unittest.TestCase):
    """Tests for the x attribute validation."""

    def test_x_not_int(self):
        """Test x as a string raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")

    def test_x_negative_raises_value_error(self):
        """Test negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_x_zero_is_valid(self):
        """Test x of 0 is a valid value."""
        r = Rectangle(10, 2, 0)
        self.assertEqual(r.x, 0)


class TestRectangleYValidation(unittest.TestCase):
    """Tests for the y attribute validation."""

    def test_y_not_int(self):
        """Test y as a float raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 2.5)

    def test_y_negative_raises_value_error(self):
        """Test negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -2)

    def test_y_zero_is_valid(self):
        """Test y of 0 is a valid value."""
        r = Rectangle(10, 2, 1, 0)
        self.assertEqual(r.y, 0)


class TestRectangleAttributeSetters(unittest.TestCase):
    """Tests updating attributes after instantiation."""

    def test_set_width_after_init(self):
        """Test width can be updated after instantiation."""
        r = Rectangle(1, 1)
        r.width = 15
        self.assertEqual(r.width, 15)

    def test_set_width_invalid_after_init(self):
        """Test setting an invalid width later still raises errors."""
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = -5

    def test_set_height_after_init(self):
        """Test height can be updated after instantiation."""
        r = Rectangle(1, 1)
        r.height = 20
        self.assertEqual(r.height, 20)

    def test_set_x_after_init(self):
        """Test x can be updated after instantiation."""
        r = Rectangle(1, 1)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_set_y_after_init(self):
        """Test y can be updated after instantiation."""
        r = Rectangle(1, 1)
        r.y = 5
        self.assertEqual(r.y, 5)


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method."""

    def test_area_basic(self):
        """Test area computation for a simple rectangle."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_square_case(self):
        """Test area computation when width equals height."""
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_area_after_update(self):
        """Test area reflects changes made after instantiation."""
        r = Rectangle(3, 2)
        r.width = 10
        self.assertEqual(r.area(), 20)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method."""

    def test_display_no_offset(self):
        """Test display with x=0 and y=0."""
        r = Rectangle(2, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_with_x_offset(self):
        """Test display respects the x offset (leading spaces)."""
        r = Rectangle(2, 1, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "  ##\n")

    def test_display_with_y_offset(self):
        """Test display respects the y offset (blank lines above)."""
        r = Rectangle(2, 1, 0, 3)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n\n\n##\n")

    def test_display_with_x_and_y_offset(self):
        """Test display respects both x and y offsets together."""
        r = Rectangle(3, 2, 1, 1)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n ###\n ###\n")


class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def setUp(self):
        """Reset the Base private class counter before every test."""
        Base._Base__nb_objects = 0

    def test_str_with_id(self):
        """Test string representation with an explicit id."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_auto_id(self):
        """Test string representation with an auto-assigned id."""
        r = Rectangle(4, 6)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 4/6")

    def test_str_via_print(self):
        """Test print() correctly triggers __str__."""
        r = Rectangle(1, 1, 0, 0, 5)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(r)
            self.assertEqual(
                fake_out.getvalue(), "[Rectangle] (5) 0/0 - 1/1\n")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for the update method using *args."""

    def test_update_id_only(self):
        """Test updating only the id via args."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_and_width(self):
        """Test updating id and width via args."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2)
        self.assertEqual((r.id, r.width), (89, 2))

    def test_update_all_args(self):
        """Test updating all attributes via args."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test_update_no_args_no_change(self):
        """Test that calling update with no arguments changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (1, 10, 10, 10, 10))

    def test_update_args_invalid_value_raises(self):
        """Test that invalid values passed via args still raise errors."""
        r = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            r.update(1, -5)


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for the update method using **kwargs."""

    def test_update_kwargs_single(self):
        """Test updating a single attribute via kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=2)
        self.assertEqual(r.width, 2)

    def test_update_kwargs_multiple(self):
        """Test updating multiple attributes via kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(x=2, y=3, id=100)
        self.assertEqual((r.x, r.y, r.id), (2, 3, 100))

    def test_update_kwargs_unordered(self):
        """Test kwargs update works regardless of order given."""
        r = Rectangle(1, 1)
        r.update(height=7, width=3)
        self.assertEqual((r.width, r.height), (3, 7))

    def test_update_args_take_priority_over_kwargs(self):
        """Test that when args are given, kwargs are ignored."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(50, width=999)
        self.assertEqual((r.id, r.width), (50, 10))


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_to_dictionary_keys_and_values(self):
        """Test the dictionary has correct keys and values."""
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_is_dict_type(self):
        """Test the return type is a dict."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_creates_identical_rectangle(self):
        """Test a rectangle built from the dictionary matches original."""
        r1 = Rectangle(10, 2, 1, 9, 5)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(**r1_dict)
        self.assertEqual(str(r1), str(r2))

    def test_to_dictionary_independent_of_instance(self):
        """Test mutating the returned dict does not affect the instance."""
        r = Rectangle(10, 2)
        d = r.to_dictionary()
        d["width"] = 999
        self.assertEqual(r.width, 10)


class TestRectangleCreate(unittest.TestCase):
    """Tests for the create classmethod."""

    def test_create_returns_rectangle_instance(self):
        """Test create returns an instance of Rectangle."""
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertIsInstance(r, Rectangle)

    def test_create_sets_all_attributes(self):
        """Test create applies every given attribute."""
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_create_partial_dictionary(self):
        """Test create works with only some attributes given."""
        r = Rectangle.create(id=89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)

    def test_create_no_dictionary(self):
        """Test create with no attributes returns a dummy rectangle."""
        r = Rectangle.create()
        self.assertEqual((r.width, r.height), (1, 1))


class TestRectangleSaveToFile(unittest.TestCase):
    """Tests for the save_to_file classmethod."""

    def setUp(self):
        """Reset the Base counter and remove any stray output file."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        """Remove the output file created by these tests, if any."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_none_writes_empty_list(self):
        """Test save_to_file(None) writes an empty JSON list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list_writes_empty_list(self):
        """Test save_to_file([]) writes an empty JSON list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_creates_file(self):
        """Test save_to_file creates a file on disk."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_content_matches(self):
        """Test the JSON content matches the rectangles given."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 0, 0, 6)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            list_dicts = json.loads(f.read())
        self.assertEqual(
            list_dicts, [r1.to_dictionary(), r2.to_dictionary()])


class TestRectangleLoadFromFile(unittest.TestCase):
    """Tests for the load_from_file classmethod."""

    def setUp(self):
        """Reset the Base counter and remove any stray output file."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        """Remove the output file created by these tests, if any."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_load_from_file_no_file_returns_empty_list(self):
        """Test load_from_file returns [] when no file exists."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_round_trip(self):
        """Test save then load returns equivalent rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 0, 0, 6)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(
            [r.to_dictionary() for r in loaded],
            [r1.to_dictionary(), r2.to_dictionary()])

    def test_load_from_file_returns_rectangle_instances(self):
        """Test loaded objects are instances of Rectangle."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        loaded = Rectangle.load_from_file()
        for obj in loaded:
            self.assertIsInstance(obj, Rectangle)


if __name__ == "__main__":
    unittest.main()
