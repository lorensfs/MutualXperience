#!/usr/bin/env bash

set -e
set -x

uv sync
uv run pre-commit install
source .venv/bin/activate
