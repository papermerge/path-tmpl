# Path Template

## Install

```shell
  uv add pathtmpl
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
context = Context(
    id=uuid.uuid4(),
    title="My Tax Declaration",
    file_name="elster_doc.pdf",
    category="Taxes",
    year=2025,
    month=12,
    day=11,
)

ev_path = get_evaluated_path(context, path_template=path_tmpl)
assert ev_path == PurePath("/Tax/2025/elster_doc.pdf")
```

Another example:
```python
import uuid
from pathlib import PurePath
from pathtmpl import Context, get_evaluated_path


context = Context(
        file_name="receipt.pdf",
        title="Receipt from ALDI",
        id=uuid.uuid4(),
        year=2025,
        day=11,
        month=12,
        category="Grocery Receipts"
)
ev_path = get_evaluated_path(
    context,
    path_template="/{{ category }}/{{ year }}/{{ file_name }}",
)

expected_path = PurePath(
    "/Grocery Receipts/2025/receipt.pdf"
)
assert PurePath(ev_path) == expected_path
```

In its simplest form:

```python
import uuid
from pathlib import PurePath
from pathtmpl import Context, get_evaluated_path


context = Context(
    title="coco",
    id=uuid.uuid4(),
    year=2025,
    day=11,
    month=12,
    file_name="invoice.pdf",
    category="Invoice"
)
ev_path = get_evaluated_path(context, path_template="/My Documents/Receipt/")

assert ev_path == "/My Documents/Receipt/"
```

## Run Tests

```shell
uv sync --group dev
uv run pytest
```
