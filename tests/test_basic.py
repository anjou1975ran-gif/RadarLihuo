
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lihou import run as run_lihou
from lihuo import run as run_lihuo


def test_run_exported_from_lihou():
    assert run_lihou("this prompt is long enough") == "[LIHUO] PASS"


def test_typo_alias_lihuo_imports_run():
    assert run_lihuo("short") == "[LIHUO] HOLD"
