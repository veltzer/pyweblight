"""
main entry point to the program
"""


import pylogconf.core
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint

from pyweblight.static import APP_NAME, VERSION_STR, DESCRIPTION


@register_endpoint(
    description="Start the web server",
)
def start() -> None:
    pass


@register_endpoint(
    description="Stop the web server",
)
def stop() -> None:
    pass


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
