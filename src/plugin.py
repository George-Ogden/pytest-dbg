import functools
from typing import Any

from _pytest.assertion.util import _compare_eq_any
from debug import pformat
from pytest import Config


def pytest_assertrepr_compare(config: Config, op: str, left: Any, right: Any) -> list[str] | None:
    if op == "==":
        format = functools.partial(
            pformat, width=0, style=None, indent=2, sort_unordered_collections=True
        )
        left_repr = format(left)
        right_repr = format(right)

        if left_repr != right_repr:
            highlighter = config.get_terminal_writer()._highlight
            verbose = config.get_verbosity(Config.VERBOSITY_ASSERTIONS)

            return _compare_eq_any(left_repr, right_repr, highlighter, verbose)
    return None
