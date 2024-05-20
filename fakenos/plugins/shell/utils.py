"""
This module is intended to be used
a collection of utilities for the shell.
"""

import os
from typing import Dict, List


def get_files_under_directory(directory):
    """Method to get files under a directory"""
    files: List = []
    for root, _, filenames in os.walk(directory):
        if "__pycache__" in root:
            continue
        files += [os.path.join(root, filename) for filename in filenames]
    files = [file for file in files if os.path.isfile(file)]
    files = [file for file in files if file.endswith((".py", ".j2", ".yaml"))]
    files = [file for file in files if not file.endswith("__init__.py")]
    return files


def get_files_lasttime_changed(files):
    """Method to get files last time changed"""
    return {file: os.stat(file).st_mtime for file in files}


def get_new_files(old_files: List[str], new_files: List[str]):
    """Compare old files with new files and return new files"""
    return [file for file in new_files if file not in old_files]


def get_files_recently_modified(files: List[str], files_lasttime_changed_old: Dict[str, float]):
    """Method to get files recently modified"""
    return [file for file in files if os.stat(file).st_mtime != files_lasttime_changed_old.get(file, 0)]


def change_jinja_to_corresponding_py(files: List[str]):
    """Method to change j2 files to corresponding py files"""
    jinja_files = [file for file in files if file.endswith(".j2")]
    files = [file for file in files if not file.endswith(".j2")]
    for filepath in jinja_files:
        split: List[str] = filepath.rsplit("/", 3)
        corresponding_py_module = f"{split[0]}/{split[2]}.py"
        files.append(corresponding_py_module)
    return files


def get_files_changed(directory: str):
    """Method to get files changed under a directory"""
    files_changed: List[str] = []
    files_under_directory: List[str] = get_files_under_directory(directory)
    if not hasattr(get_files_changed, "files_lasttime_changed_old"):
        get_files_changed.files_lasttime_changed_old = get_files_lasttime_changed(files_under_directory)
    files_changed += get_new_files(get_files_changed.files_lasttime_changed_old.keys(), files_under_directory)
    files_changed += get_files_recently_modified(files_under_directory, get_files_changed.files_lasttime_changed_old)
    files_changed = change_jinja_to_corresponding_py(files_changed)
    get_files_changed.files_lasttime_changed_old = get_files_lasttime_changed(files_under_directory)
    return files_changed
