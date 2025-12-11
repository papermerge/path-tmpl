from jinja2.sandbox import SandboxedEnvironment
from jinja2 import Template

from pathtmpl import models


template_env = SandboxedEnvironment()


def get_evaluated_path(
    context: models.Context,
    path_template: str,
) -> str:
    template = template_env.from_string(
        path_template,
        template_class=Template,
    )
    return template.render(context)
