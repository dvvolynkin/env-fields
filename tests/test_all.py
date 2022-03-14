import os
from dataclasses import dataclass
from typing import Any

import pytest

from env_fields import (
    env_field_int,
    env_field_str,
    env_field_float,
    env_field,
    env_var_getter,
    str_env_var_getter,
    int_env_var_getter,
    float_env_var_getter,
)

given = pytest.mark.parametrize


@given(
    "env_field_fn, env_var_value, expected_res_value",
    [
        (env_field_int, "12", 12),
        (env_field_str, "12", "12"),
        (env_field_float, "1.2", 1.2),
    ],
)
def test_ready_field_types(
    monkeypatch, env_field_fn, env_var_value, expected_res_value
):
    monkeypatch.setattr(os, "environ", {"SOME_ENV_VAR_NAME": env_var_value})

    @dataclass
    class SomeDataClass:
        env_var: Any = env_field_fn("SOME_ENV_VAR_NAME")

    assert SomeDataClass().env_var == expected_res_value


@given(
    "env_var_getter, env_var_value, expected_res_value",
    [
        (int_env_var_getter, "12", 12),
        (str_env_var_getter, "12", "12"),
        (float_env_var_getter, "1.2", 1.2),
    ],
)
def test_ready_env_var_getters(
    monkeypatch, env_var_getter, env_var_value, expected_res_value
):
    monkeypatch.setattr(os, "environ", {"SOME_ENV_VAR_NAME": env_var_value})

    assert env_var_getter("SOME_ENV_VAR_NAME")() == expected_res_value


def test_env_field(monkeypatch):
    @dataclass
    class SomeDataClass:
        env_var: Any = env_field("SOME_ENV_VAR_NAME", str, default=12323)

    assert SomeDataClass().env_var == 12323
    monkeypatch.setattr(os, "environ", {"SOME_ENV_VAR_NAME": "hello, world"})
    assert SomeDataClass().env_var == "hello, world"


def test_env_var_getter(monkeypatch):
    getter = env_var_getter("SOME_ENV_VAR_NAME", str, default=12323)

    assert getter() == 12323
    monkeypatch.setattr(os, "environ", {"SOME_ENV_VAR_NAME": "hello, world"})
    assert getter() == "hello, world"
