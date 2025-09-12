# pytest-dbg

I wrote a version of the `dbg!` macro in Python: https://github.com/George-Ogden/dbg.
It has a pretty printing library built into it.
One of the core users suggested I use it for pytest equality assertions to make debugging failing tests easier.

## Example

Here's a test:

```python
import ast

def test_ast():
    assert ast.List([ast.Constant(0)]) == ast.List([ast.Constant(1)])
```

Without this plugin, you get the following output:

```
pytest ast_test.py -v
=================================== FAILURES ===================================
___________________________________ test_dbg ___________________________________

    def test_ast():
>       assert ast.List([ast.Constant(0)]) == ast.List([ast.Constant(1)])
E       AssertionError: assert <ast.List object at 0x7f0477d447d0> == <ast.List object at 0x7f0477d45350>
E        +  where <ast.List object at 0x7f0477d447d0> = <class 'ast.List'>([<ast.Constant object at 0x7f0477d2fcd0>])
E        +    where <class 'ast.List'> = ast.List
E        +  and   <ast.List object at 0x7f0477d45350> = <class 'ast.List'>([<ast.Constant object at 0x7f0477d45410>])
E        +    where <class 'ast.List'> = ast.List

ast_test.py:4: AssertionError
```

With this plugin, you get a clearer output:

```
pytest ast_test.py -v
=================================== FAILURES ===================================
___________________________________ test_dbg ___________________________________

    def test_ast():
>       assert ast.List([ast.Constant(0)]) == ast.List([ast.Constant(1)])
E       assert   List(
E             elts=[
E               Constant(
E         -       value=1,
E         ?             ^
E         +       value=0,
E         ?             ^
E               ),
E             ],
E           )

ast_test.py:4: AssertionError
```

It looks even better in color!

# Usage/Install

```bash
pip install git+https://github.com/George-Ogden/pytest-dbg
```

Then use `pytest` as normal!

For more advanced usage, see https://docs.pytest.org/en/stable/how-to/plugins.html.
