#!/usr/bin/env python3
"""Compatibility entrypoint; implementation belongs to ai-models."""
from pathlib import Path
import runpy

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).resolve().parents[3]/'ai-models/scripts/model_data.py'),run_name='__main__')
