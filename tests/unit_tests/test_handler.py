"""Behavioural tests for pyweblight's request-handler path helpers.

MyHandler.__init__ chains into SimpleHTTPRequestHandler, which wants a live
socket, so these tests build the instance with object.__new__ and set only
the attributes (path, search_path) the pure helpers read.
"""

import os
import tempfile
import unittest

from pyweblight import webserver_start


def _bare_handler() -> webserver_start.MyHandler:
    handler = object.__new__(webserver_start.MyHandler)
    handler.encoding = "utf8"
    handler.search_path = "."
    return handler


class ToPathTests(unittest.TestCase):
    def test_root_becomes_dot(self):
        handler = _bare_handler()
        handler.path = "/"
        self.assertEqual(handler.to_path(), ".")

    def test_leading_slash_stripped(self):
        handler = _bare_handler()
        handler.path = "/index.html"
        self.assertEqual(handler.to_path(), "index.html")

    def test_nested_path(self):
        handler = _bare_handler()
        handler.path = "/a/b/c.txt"
        self.assertEqual(handler.to_path(), "a/b/c.txt")


class ResolveTests(unittest.TestCase):
    def test_finds_file_in_first_matching_folder(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "found.txt"), "w", encoding="utf-8"):
                pass
            handler = _bare_handler()
            handler.search_path = d
            self.assertEqual(handler.resolve("found.txt"), os.path.join(d, "found.txt"))

    def test_missing_name_returns_none(self):
        with tempfile.TemporaryDirectory() as d:
            handler = _bare_handler()
            handler.search_path = d
            self.assertIsNone(handler.resolve("absent.txt"))

    def test_searches_folders_in_order(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            with open(os.path.join(second, "only.txt"), "w", encoding="utf-8"):
                pass
            handler = _bare_handler()
            handler.search_path = first + ":" + second
            self.assertEqual(handler.resolve("only.txt"), os.path.join(second, "only.txt"))


if __name__ == "__main__":
    unittest.main()
