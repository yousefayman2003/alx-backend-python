#!/usr/bin/python3
"""Module contains units test for utils module"""
import unittest
from unittest.mock import Mock, patch

from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict


class TestAccessNestedMap(unittest.TestCase):
    """Unit test to test access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]
            ) -> None:
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            exception: Exception
            ) -> None:
        """Tests When access_nested_map raises an expection correctly"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit test to test get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, expected_payload: Dict) -> None:
        """Test get_json function"""
        attrs = {"json.return_value": expected_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as p:
            self.assertEqual(get_json(test_url), expected_payload)
            p.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unit test to test memoize function"""

    def test_memoize(self) -> None:
        """Test memoize function"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            memo_fn.assert_called_once()


if __name__ == "__main__":
    unittest.main()
