from typing import List

import os
import subprocess

import sys


def array_indented(level: int, array: List[str], quote_char: str = '\'', comma_after: bool = False) -> str:
    """
    return an array indented according to indent level
    :param level:
    :param array:
    :param quote_char:
    :param comma_after:
    :return:
    """
    out = "[\n"
    for x in array:
        out += (((level + 1) * 4) * " ") + '{}{}{}'.format(quote_char, x, quote_char) + ",\n"
    out += ((level * 4) * " ") + "]"
    if comma_after:
        out += ","
    return out


def find_packages(path: str) -> List[str]:
    """
    A better version of find_packages than what setuptools offers
    :param path:
    :return:
    """
    for root, _dir, files in os.walk(path):
        if '__init__.py' in files:
            yield root.replace("/", ".")


def in_2():
    return sys.version_info[0] == 2


def in_3():
    return sys.version_info[0] == 3


def help_check_output(*args, **kwargs):
    if in_2():
        return subprocess.check_output(*args, **kwargs).decode()
    if in_3():
        return subprocess.check_output(*args, **kwargs)
