import uuid

from pathlib import PurePath

from pathtmpl import get_evaluated_path, Context


def test_get_evaluated_path_as_folder():
    """Folder path end with '/' """
    doc = Context(
        title="coco",
        id=uuid.uuid4(),
        year=2025,
        day=11,
        month=12,
        file_name="invoice.pdf",
        category="Invoice"
    )
    ev_path = get_evaluated_path(doc, path_template="/My Documents/Receipt/")

    assert ev_path == "/My Documents/Receipt/"


def test_get_evaluated_path_as_document_without_templating():
    """Notice there is no templating i.e. {{}}  or {% ... %} """
    doc = Context(
        title="coco",
        id=uuid.uuid4(),
        year=2025,
        day=11,
        month=12,
        file_name="invoice.pdf",
        category="Invoices"
    )
    ev_path = get_evaluated_path(doc, path_template="/My Documents/coco")

    assert ev_path == "/My Documents/coco"


def test_get_evaluated_path_title():
    doc = Context(
        title="coco",
        id=uuid.uuid4(),
        year=2025,
        day=11,
        month=12,
        file_name = "invoice.pdf",
        category="Invoices"
    )
    ev_path = get_evaluated_path(doc, path_template="/Invoices/{{ title }}")

    assert ev_path == "/Invoices/coco"


def test_get_evaluated_path_id():
    doc = Context(
        title="coco",
        id=uuid.uuid4(),
        year=2025,
        day=11,
        month=12,
        file_name="invoice.pdf",
        category="Invoices"
    )
    ev_path = get_evaluated_path(
        doc,
        path_template="/Invoices/{{ title }}-{{ id }}",
    )

    assert PurePath(ev_path) == PurePath(f"/Invoices/coco-{doc.id}")


def test_get_evaluated_path_with_year():
    context = Context(
        file_name="invoice.pdf",
        title="Invoice from Tom",
        id=uuid.uuid4(),
        year=2025,
        day=11,
        month=12,
        category="Invoices"
    )
    ev_path = get_evaluated_path(
        context,
        path_template="/Invoices/{{ year }}/{{ title }}/{{ file_name }}_{{ id }}",
    )

    expected_path = PurePath(
        f"/Invoices/2025/Invoice from Tom/invoice.pdf_{context.id}"
    )
    assert PurePath(ev_path) == expected_path


def test_get_evaluated_path_with_category():
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
