from datetime import datetime, date

from jinja2.sandbox import SandboxedEnvironment
from jinja2 import Template


from pathtmpl import models


def datefmt(value: datetime | date, format: str) -> str:
    return value.strftime(format=format)


template_env = SandboxedEnvironment()
template_env.filters["datefmt"] = datefmt


def get_evaluated_path(
    doc: models.DocumentContext,
    path_template: str,
) -> str:
    context = {"document": doc}
    template = template_env.from_string(
        path_template,
        template_class=Template,
    )
    return template.render(context)
