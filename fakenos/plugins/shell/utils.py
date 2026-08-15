"""
This module is intended to be used
a collection of utilities for the shell.
"""

import os
from pathlib import Path
from typing import Dict, List

_files_lasttime_changed_by_directory: Dict[str, Dict[str, float]] = {}


def get_files_under_directory(directory: str) -> List[str]:
    """Method to get files under a directory"""
    files: List[str] = []
    for root, _, filenames in os.walk(directory):
        if "__pycache__" in root:
            continue
        files += [os.path.join(root, filename) for filename in filenames]
    return [
        file
        for file in files
        if os.path.isfile(file) and file.endswith((".py", ".j2", ".yaml", ".yml")) and not file.endswith("__init__.py")
    ]


def get_files_lasttime_changed(files: List[str]) -> Dict[str, float]:
    """Method to get files last time changed"""
    return {file: os.stat(file).st_mtime for file in files}


def get_new_files(old_files: List[str], new_files: List[str]) -> List[str]:
    """Compare old files with new files and return new files"""
    return [file for file in new_files if file not in old_files]


def get_files_recently_modified(
    files: List[str],
    files_lasttime_changed_old: Dict[str, float],
) -> List[str]:
    """Method to get files recently modified"""
    return [file for file in files if os.stat(file).st_mtime != files_lasttime_changed_old.get(file, 0)]


def change_jinja_to_corresponding_py(files: List[str]) -> List[str]:
    """Method to change j2 files to corresponding py files"""
    jinja_files = [file for file in files if file.endswith(".j2")]
    changed_files = {file for file in files if not file.endswith(".j2")}
    for filepath in jinja_files:
        path = Path(filepath)
        if "configurations" in path.parts:
            platform = path.name.removesuffix(".yaml.j2").removesuffix(".yaml")
            changed_files.add(str(path.parent.parent / f"{platform}.py"))
        else:
            platform = path.parent.name
            changed_files.add(str(path.parent.parent.parent / f"{platform}.py"))
    return list(changed_files)


def get_files_changed(directory: str) -> List[str]:
    """Method to get files changed under a directory"""
    files_changed: List[str] = []
    files_under_directory: List[str] = get_files_under_directory(directory)
    previous_timestamps = _files_lasttime_changed_by_directory.setdefault(
        directory,
        get_files_lasttime_changed(files_under_directory),
    )
    files_changed += get_new_files(list(previous_timestamps), files_under_directory)
    files_changed += get_files_recently_modified(files_under_directory, previous_timestamps)
    files_changed = change_jinja_to_corresponding_py(files_changed)
    _files_lasttime_changed_by_directory[directory] = get_files_lasttime_changed(files_under_directory)
    return files_changed
