"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import querymesh


def test_version_is_set() -> None:
    assert querymesh.__version__
