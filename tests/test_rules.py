import pytest

from flake8_obey_import_goat.rules import collect_rules_for


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('a/foo.py', [('a', '')]),
        ('a/bar.py', [('a', ''), ('b', '')]),
        ('b/baz.py', []),
    ],
)
def test_collect_rules_for_main_cases(filename, expected, all_rules):
    assert collect_rules_for(filename, all_rules) == expected
