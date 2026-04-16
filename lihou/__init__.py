"""Public package exports for lihou."""

from .core import run

__all__ = ["run"]

"""Backward-compatible package alias.

This allows imports such as `from lihuo import run` while the canonical
implementation currently lives in the `lihou` package directory.
"""

from lihou import run

__all__ = ["run"]
