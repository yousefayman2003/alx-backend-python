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
