from typing import List


console_scripts: List[str] = [
    "pyweblight=pyweblight.main:main",
]
config_requires: List[str] = [
    "pyclassifiers",
]
dev_requires: List[str] = [
    "pypitools",
]
install_requires: List[str] = [
    "python-daemon",
    "pytconf",
    "pylogconf",
]
make_requires: List[str] = [
    "pyclassifiers",
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
from typing import List


