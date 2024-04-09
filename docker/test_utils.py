import pytest
from fastapi_pagination import paginate


def test_warning():
    """
    This generates `warnings` but pytest.filterwarnings from pyproject.toml
    doesn't catch it, because the asterisk '.*' doesn't match the first '\n'
    in the `_WARNING_MSG`.
    """
    with pytest.raises(RuntimeError, match="Use params or add_pagination"):
        paginate(None)
