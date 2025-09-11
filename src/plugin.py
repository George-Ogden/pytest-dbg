from typing import Any

from _pytest.assertion.util import _compare_eq_any
from debug._format import Formatter, FormatterConfig
from pytest import Config


def pytest_assertrepr_compare(config: Config, op: str, left: Any, right: Any) -> list[str] | None:
    if op == "==":
        formatter_config = FormatterConfig(indent_width=2, terminal_width=0, color=False)
        formatter = Formatter(formatter_config)
        left_repr = formatter.format(left, initial_width=0)
        right_repr = formatter.format(right, initial_width=0)

        if left_repr != right_repr:
            highlighter = config.get_terminal_writer()._highlight
            verbose = config.get_verbosity(Config.VERBOSITY_ASSERTIONS)

            return _compare_eq_any(left_repr, right_repr, highlighter, verbose)
    return None
