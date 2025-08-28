#!/usr/bin/env bash
# Wrapper script to launch the Streamlit interface.
# Runs from the repository root, forwarding any extra arguments.
set -e
cd "$(dirname "$0")"

streamlit run tools/ui_app.py "$@"
