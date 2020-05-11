"""
main entry point to the program
"""


import pylogconf.core
from pytconf.config import register_main, get_pytconf

from pyweblight.endpoints.group_default import register_group_default


def register_all_groups():
    """
    registers all groups of operations with pytconf
    """
    register_group_default()


@register_main()
def main():
    """
    pyweblight is a lightweight web server in python
    """
    pylogconf.core.setup()
    register_all_groups()
    get_pytconf().config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
