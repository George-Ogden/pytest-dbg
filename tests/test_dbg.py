import pytest
from pytest import Pytester


@pytest.mark.typed
def test_bar_fixture(pytester: Pytester) -> None:
    pytester.makepyfile("""
        import ast
        def test_error():
            assert ast.List([ast.Constant(0)]) == ast.List([ast.Constant(1)])
    """)

    result = pytester.runpytest("-v")

    result.stdout.fnmatch_lines(["*-*value=1,", "*+*value=0,"])

    assert result.ret != 0
