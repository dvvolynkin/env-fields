import os
from dataclasses import field
from functools import partial

_EmptyType = type("_EmptyType", (object,), {})
NO_DEFAULT_VALUE = _EmptyType()


class EnvVarParsingError(Exception):
    ...


def get_env_value(cast, name, default=NO_DEFAULT_VALUE):
    value = os.getenv(name)
    if value is None:
        if default == NO_DEFAULT_VALUE:
            raise EnvVarParsingError(
                (
                    f"Environment variable {name} not set."
                    " Default value for this case not set too."
                )
            )

        return default

    return cast(value)


def env_field(name, cast, default=NO_DEFAULT_VALUE, **kwargs):
    return field(
        default_factory=partial(
            get_env_value,
            name=name,
            cast=cast,
            default=default,
        ),
        **kwargs,
    )


def _specific_env_field(cast):
    return partial(env_field, cast=cast)


env_field_str = _specific_env_field(str)
env_field_int = _specific_env_field(int)
env_field_float = _specific_env_field(float)
