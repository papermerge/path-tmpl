# Path Template

## Install

```shell
poetry add pathtmpl
```


## Usage

```python
import uuid
from pathlib import PurePath
from datetime import date as Date
from pathtmpl import Context, get_evaluated_path


path_tmpl = """
  /Tax/{{ year }}/{{ file_name }}
"""
doc = Context(
    id=uuid.uuid4(),
    title="My Tax Declaration",
    file_name="elster_doc.pdf",
    year=2025,
    month=12,
    day=11,
)

ev_path = get_evaluated_path(doc, path_template=path_tmpl)
assert ev_path == PurePath("/Tax/2025/elster_doc.pdf")
```

## Tests

```shell
poetry run pytest
```
