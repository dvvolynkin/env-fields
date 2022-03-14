---
# env_fields

[![codecov](https://codecov.io/gh/dvvolynkin/env-fields/branch/main/graph/badge.svg?token=env-fields_token_here)](https://codecov.io/gh/dvvolynkin/env-fields)
[![CI](https://github.com/dvvolynkin/env-fields/actions/workflows/main.yml/badge.svg)](https://github.com/dvvolynkin/env-fields/actions/workflows/main.yml)

Dataclass fields with getting values from environment by default

## Install it from PyPI

```bash
pip install env_fields
```

## Usage

```python
import os
from dataclasses import field, dataclass
from env_fields import (
    env_field_int,
    env_field_str,
    env_field,
)


@dataclass
class SomeClass:
    attribute_1: int = field()
    attribute_2: int = env_field_int('SOME_INT_ENVIRONMENT_VARIABLE')
    attribute_3: str = env_field_str('SOME_STR_ENVIRONMENT_VARIABLE')
    attribute_4: str = env_field_str(
        'SOME_STR_ENVIRONMENT_VARIABLE_THAT_NOT_SET',
        default="hello, world"
    )
    attribute_5: int = env_field("SOME_CUSTOM_TYPE_ENV_VARIABLE", float, init=False)

```
Let's create some dataclass!
```python
>>> os.environ['SOME_INT_ENVIRONMENT_VARIABLE'] = "1234"
>>> os.environ['SOME_STR_ENVIRONMENT_VARIABLE'] = "hello, world 1"
>>> os.environ['SOME_CUSTOM_TYPE_ENV_VARIABLE'] = "2.59"
>>> SomeClass(12)
SomeClass(
    attribute_1=12,
    attribute_2=1234,
    attribute_3='hello, world 1',
    attribute_4='hello, world',
    attribute_5=2.59,
)
```


## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
