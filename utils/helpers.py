from typing import NamedTuple


class SelectorParser(NamedTuple):
    selector_type: str
    locator: str