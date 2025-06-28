"""
All configurations for pyweblight
"""


from pytconf import Config, ParamCreator


class ConfigStart(Config):
    """
    Parameters for the start command
    """
    force = ParamCreator.create_bool(
        help_string="remove target files if they are links?",
        default=True,
    )


class ConfigStop(Config):
    """
    Parameters for the stop command
    """
    force = ParamCreator.create_bool(
        help_string="remove target files if they are links?",
        default=True,
    )
