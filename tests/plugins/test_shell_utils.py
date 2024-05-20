"""
Test module fpr the tests of the shell utils
"""

import os
import random
import time
from unittest import TestCase
from unittest.mock import patch

from fakenos.plugins.shell.utils import (
    get_files_lasttime_changed,
    get_files_under_directory,
    get_files_changed,
    change_jinja_to_corresponding_py,
    get_files_recently_modified,
    get_new_files,
)

RANDOM_FILE: str = random.choice(
    [file for file in get_files_under_directory("fakenos/plugins/nos") if file.endswith((".py", ".yaml"))]
)


class MockStatResult:
    """Mocking class for os.stat"""

    def __init__(self, original_stat_result, file):
        """Mocking class for os.stat"""
        self._original_stat_result = original_stat_result
        self._file = file

    @property
    def st_mtime(self):
        """Mocking st_mtime"""
        if self._file == RANDOM_FILE:
            return time.time()
        return self._original_stat_result.st_mtime

    def __getattr__(self, name):
        return getattr(self._original_stat_result, name)


def mock_os_stat(file):
    """Mocking os.stat"""
    original_stat_result = original_os_stat(file)
    return MockStatResult(original_stat_result, file)


original_os_stat = os.stat


class ShellUtilsTest(TestCase):
    """
    Test class for the shell utils
    """

    def tearDown(self):
        """
        Set up for the tests.
        We want to avoid side-effect as get_files_changed
        it is stateful.
        """
        if hasattr(get_files_changed, "files_lasttime_changed_old"):
            del get_files_changed.files_lasttime_changed_old

    def test_get_files_under_directory(self):
        """
        Test method for the get_files_under_directory
        """
        files = get_files_under_directory("fakenos/plugins/nos")
        self.assertTrue(files)
        self.assertTrue(all(not file.endswith("__init__.py") for file in files))
        self.assertTrue(all(file for file in files if file.endswith((".py", ".jinja", ".yaml"))))

    def test_get_files_lasttime_changed(self):
        """
        Test to check if we get the last time
        that the files has been changed correctly.
        """
        files = get_files_under_directory("fakenos/plugins/nos")
        files_lasttime_changed = get_files_lasttime_changed(files)
        self.assertTrue(files_lasttime_changed)
        self.assertTrue(all(file in files_lasttime_changed for file in files))
        self.assertTrue(all(files_lasttime_changed[file] for file in files))
        self.assertTrue(all(files_lasttime_changed[file] > 0 for file in files))

    def test_get_new_files(self):
        """
        Test to check if we get the new files
        """
        old_files = ["file1", "file2"]
        new_files = ["file2", "file3"]
        self.assertEqual(get_new_files(old_files, new_files), ["file3"])

    def test_change_jinja_to_corresponding_py(self):
        """
        Test to check if we change jinja files to corresponding py files
        """
        files = get_files_under_directory("fakenos/plugins/nos")
        files = [file for file in files if "cisco_ios" in file]
        files = [file for file in files if file.endswith(".jinja")]
        files = change_jinja_to_corresponding_py(files)
        self.assertTrue(files)
        self.assertTrue(all(not file.endswith(".jinja") for file in files))
        self.assertTrue(all(file for file in files if file.endswith(".py")))
        self.assertTrue(all("cisco_ios" in file for file in files))

    def test_change_jinja_to_corresponding_py_null(self):
        """
        Test to check if we don't change any jinja files to corresponding py files
        """
        files = get_files_under_directory("fakenos/plugins/nos")
        files = [file for file in files if "cisco_ios" in file]
        files = [file for file in files if file.endswith(".py")]
        files = change_jinja_to_corresponding_py(files)
        self.assertTrue(files)
        self.assertTrue(all(not file.endswith(".jinja") for file in files))
        self.assertTrue(all(file for file in files if file.endswith(".py")))
        self.assertTrue(all("cisco_ios" in file for file in files))

    def test_get_files_recently_modified(self):
        """
        Test to check if we get the files that have been recently modified
        """
        files = get_files_under_directory("fakenos/plugins/nos")
        files_lasttime_changed = get_files_lasttime_changed(files)
        with patch("os.stat", side_effect=mock_os_stat):
            files = get_files_recently_modified(files, files_lasttime_changed)
        self.assertTrue(files)
        self.assertTrue(all(file in files for file in files))
        self.assertTrue(all(files_lasttime_changed[file] != 0 for file in files))

    def test_get_files_changed(self):
        """
        Test to check if we get the files that have been changed
        """
        files = get_files_changed("fakenos/plugins/nos")
        self.assertFalse(files)
        with patch("os.stat", side_effect=mock_os_stat):
            files = get_files_changed("fakenos/plugins/nos")
        self.assertTrue(files)
        self.assertIn(RANDOM_FILE, files)
        files = get_files_changed("fakenos/plugins/nos")

    def test_get_files_changed_null(self):
        """
        Test to check if we don't get the files that have been changed
        """
        files = get_files_changed("fakenos/plugins/nos")
        self.assertFalse(files)
        files = get_files_changed("fakenos/plugins/nos")
        self.assertFalse(files)
