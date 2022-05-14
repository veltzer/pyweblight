import config.project

package_name = config.project.project_name

console_scripts = [
    "pyweblight=pyweblight.main:main",
]
dev_requires = [
    "pypitools",
]
config_requires = [
    "pyclassifiers",
]
make_requires = [
    "pymakehelper",
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

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
