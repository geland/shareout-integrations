#!/usr/bin/env python3
"""Build a review ZIP containing only public plugin files."""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    'plugin.json', 'mcp.json', '.mcp.json',
    '.codex-plugin/plugin.json', '.claude-plugin/plugin.json',
    'skills/shareout/SKILL.md', 'skills/shareout/agents/openai.yaml',
    'assets/icon.svg', 'README.md', 'LICENSE',
    'docs/distribution.md', 'docs/submission-kit.md', 'docs/host-acceptance.md',
    'configs/codex.toml', 'configs/cursor.json',
    'configs/opencode.json', 'configs/stdio.json', 'configs/vscode.json',
]
version = json.loads((ROOT / 'plugin.json').read_text())['version']
out = ROOT / 'dist' / f'shareout-plugin-{version}.zip'
out.parent.mkdir(exist_ok=True)
with ZipFile(out, 'w', ZIP_DEFLATED) as archive:
    for name in FILES:
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise SystemExit(f'Not a regular package file: {name}')
        archive.write(path, name)
print(out)
