#!/usr/bin/env bash

set -e
set -x

uv run ruff check app scripts --fix
# sort app imports
uv run ruff check app --select I --fix
uv run ruff format app
