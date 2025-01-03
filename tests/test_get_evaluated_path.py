import uuid
from datetime import date as Date
from pathlib import PurePath

from pathtmpl import get_evaluated_path, CField, DocumentContext


def test_get_evaluated_path_as_folder():
    """Folder path end with '/' """
    doc = DocumentContext(title="coco", id=uuid.uuid4())
    ev_path = get_evaluated_path(doc, path_template="/home/My Documents/Receipt/")

    assert ev_path == "/home/My Documents/Receipt/"


def test_get_evaluated_path_as_document_without_templating():
    """Notice there is no templating i.e. {{}}  or {% ... %} """
    doc = DocumentContext(title="coco", id=uuid.uuid4())
    ev_path = get_evaluated_path(doc, path_template="/home/My Documents/coco")

    assert ev_path == "/home/My Documents/coco"


def test_get_evaluated_path_title():
    doc = DocumentContext(title="coco", id=uuid.uuid4())
    ev_path = get_evaluated_path(doc, path_template="/home/{{ document.title }}")

    assert ev_path == "/home/coco"


def test_get_evaluated_path_id():
    doc = DocumentContext(title="coco", id=uuid.uuid4())
    ev_path = get_evaluated_path(
        doc,
        path_template="/home/{{ document.title }}-{{ document.id }}",
    )

    assert PurePath(ev_path) == PurePath(f"/home/coco-{doc.id}")


def test_get_evaluated_path_with_all_cf_defined():
    path_tmpl = """
    {% if document.has_all_cf %}
        /home/Groceries/{{ document.cf['Shop'] }}-{{ document.cf['Effective Date'] }}-{{document.cf['Total']}}
    {% else %}
        /home/Groceries/{{ document.id }}
    {% endif %}
    """

    custom_fields = [
        CField(name="Shop", value="lidl"),
        CField(name="Total", value=10.34),
        CField(name="Effective Date", value=Date(2024, 12, 23)),
    ]
    doc = DocumentContext(id=uuid.uuid4(), title="coco", custom_fields=custom_fields)
    ev_path = get_evaluated_path(doc, path_template=path_tmpl)
    assert PurePath(ev_path.strip()) == PurePath(f"/home/Groceries/lidl-2024-12-23-10.34")


def test_get_evaluated_path_with_some_cf_missing():
    path_tmpl = """
    {% if document.has_all_cf %}
        /home/Groceries/{{ document.cf['Shop'] }}-{{ document.cf['Effective Date'] }}-{{document.cf['Total']}}
    {% else %}
        /home/Groceries/{{ document.id }}
    {% endif %}
    """
    custom_fields = [
        CField(name="Shop", value=None),  # !!! missing !!!
        CField(name="Total", value=10.34),
        CField(name="Effective Date", value=Date(2024, 12, 23)),
    ]
    doc = DocumentContext(id=uuid.uuid4(), title="coco", custom_fields=custom_fields)

    ev_path = get_evaluated_path(doc, path_template=path_tmpl)
    assert PurePath(ev_path.strip()) == PurePath(f"/home/Groceries/{doc.id}")


def test_get_evaluated_path_with_datefmt():
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
    assert PurePath(ev_path.strip()) == PurePath("/home/Tax/2024.pdf")
