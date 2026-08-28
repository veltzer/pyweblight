"""
All configurations for pyweblight
"""


from pytconf import Config, ParamCreator


class ConfigForce(Config):
    """
    Shared parameters for the start and stop commands
    """
    force = ParamCreator.create_bool(
        help_string="remove target files if they are links?",
        default=True,
    )
