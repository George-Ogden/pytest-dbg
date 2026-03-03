import pytest
from pytest import Pytester


@pytest.mark.typed
def test_fixture_with_ast(pytester: Pytester) -> None:
    pytester.makepyfile("""
        import ast
        def test_error():
            assert ast.List([ast.Constant(0)]) == ast.List([ast.Constant(1)])
    """)

    result = pytester.runpytest("-v")

    result.stdout.fnmatch_lines(["*-*value=1,", "*+*value=0,"])

    assert result.ret != 0


@pytest.mark.typed
def test_fixture_with_string(pytester: Pytester) -> None:
    pytester.makepyfile("""
        def test_error():
            assert "a\\nb\\nc\\nd\\ne\\n" == "b\\nc\\nd\\ne\\nf\\n"
    """)

    result = pytester.runpytest("-v")

    result.stdout.fnmatch_lines(["*+*a", "*b", "*c", "*d", "*e", "*-*f"])

    assert result.ret != 0
