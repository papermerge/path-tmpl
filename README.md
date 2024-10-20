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
from pathtmpl import DocumentContext, CField, get_evaluated_path


path_tmpl = """
{% if document.cf['Effective Date'] %}
    /home/Tax/{{ document.cf['Effective Date'] | datefmt("%Y") }}.pdf
{% else %}
    /home/Tax/{{ document.id }}.pdf
{% endif %}
"""
custom_fields = [
    CField(name="Total", value=245.02),
    CField(name="Effective Date", value=Date(2024, 12, 23)),
]
doc = DocumentContext(
    id=uuid.uuid4(),
    title="coco",
    custom_fields=custom_fields,
)

ev_path = get_evaluated_path(doc, path_template=path_tmpl)
assert ev_path == PurePath("/home/Tax/2024.pdf")
```

## Tests


```shell
poetry run pytest
```
