# Python tooling

Developer tooling, not shipped in the app (no Python runtime is bundled without an ADR): fixture and
sample-project generators, design-board generators (see `design-src/`), data analysis, release helpers.

- Layout: `py/daisy_tools/<area>/` package, `py/tests/`. Run with `uv run` or a venv.
- Style: classes first (ADR 0011), type hints everywhere, ruff for lint and format.
- Checks: `ruff check py`, `ruff format --check py`, `pytest py` (CI job `python` runs when any `py/**/*.py` exists).
