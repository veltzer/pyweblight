import config.project

package_name = config.project.project_name

console_scripts = [
    "pyweblight=pyweblight.main:main",
]

install_requires = [
    "python-daemon",
    "pytconf",
    "pylogconf",
]

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
]

dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
    "pymakehelper",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
