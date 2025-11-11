#!/usr/bin/env python3
"""
fix_nb_metadata.py

Usage:
  python fix_nb_metadata.py path/to/notebook.ipynb         # remove metadata.widgets if present
  python fix_nb_metadata.py path/to/notebook.ipynb --keep-widgets
      # keep metadata.widgets but ensure it has a "state" key (set to {} if missing)

This script edits the notebook in-place. Make a backup before running if you want to preserve the original.
"""
import sys
from pathlib import Path
import nbformat

def clean(path: Path, remove: bool = True):
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    if 'widgets' in nb.metadata:
        if remove:
            del nb.metadata['widgets']
            print(f"Removed metadata.widgets from {path}")
        else:
            w = nb.metadata['widgets']
            if not isinstance(w, dict):
                nb.metadata['widgets'] = {'state': {}}
                print(f"Replaced non-dict metadata.widgets with {{'state': {{}}}} in {path}")
            else:
                if 'state' not in w:
                    nb.metadata['widgets']['state'] = {}
                    print(f"Added empty 'state' to metadata.widgets in {path}")
                else:
                    print(f"metadata.widgets already has 'state' in {path}; no change made")
        nbformat.write(nb, path)
        print(f"Wrote cleaned notebook to {path}")
    else:
        print(f"No metadata.widgets present in {path}; nothing to do")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fix_nb_metadata.py notebook.ipynb [--keep-widgets]")
        sys.exit(1)
    p = Path(sys.argv[1])
    if not p.exists():
        print(f"File not found: {p}")
        sys.exit(2)
    keep = '--keep-widgets' in sys.argv
    clean(p, remove=not keep)