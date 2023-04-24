#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """the first unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """Test access_nested_map method.
            Nested_map(Dict): dictonary
            path(List, tuple, set): keys to get value in nested dect
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
