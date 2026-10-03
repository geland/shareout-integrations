#!/usr/bin/env python3
"""Validate distribution contracts against the publishers' schemas."""
import json
from pathlib import Path
import urllib.request
import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
for name in ['plugin.json', 'mcp.json', 'server.json']:
    value = json.loads((ROOT / name).read_text())
    with urllib.request.urlopen(value['$schema'], timeout=30) as response:
        schema = json.load(response)
    jsonschema.validate(value, schema)
    print(f'{name}: official schema passed')

plugin = json.loads((ROOT / 'plugin.json').read_text())
for name in ['.claude-plugin/plugin.json', '.codex-plugin/plugin.json']:
    manifest = json.loads((ROOT / name).read_text())
    for key in ['name', 'version', 'description', 'author', 'homepage', 'repository', 'license']:
        assert manifest[key] == plugin[key], f'{name}: divergent {key}'

openai = plugin['extensions']['com.openai']
assert 0 < len(openai['interface']['shortDescription']) <= 30, 'OpenAI listing subtitle must be 1-30 characters'
codex = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
assert codex['interface'] == openai['interface'], 'Divergent OpenAI listing metadata'
assert codex['extensions']['com.openai']['review'] == openai['review'], 'Divergent review cases'
cases = openai['review']['test_cases']
assert len(cases['positive']) == 5 and len(cases['negative']) == 3
for case in cases['positive']:
    assert all(case.get(key) for key in ['description', 'prompt', 'tools_triggered', 'expected_behavior'])
for case in cases['negative']:
    assert all(case.get(key) for key in ['description', 'prompt', 'expected_behavior'])

skill = (ROOT / 'skills/shareout/SKILL.md').read_text()
frontmatter = yaml.safe_load(skill.split('---', 2)[1])
assert frontmatter['name'] == 'shareout' and frontmatter['description']
assert len(skill.encode()) < 5000, 'Keep the entrypoint small; link to maintained docs'
for path in ROOT.rglob('*.json'):
    if '.git' not in path.parts and 'dist' not in path.parts:
        json.loads(path.read_text())
print('Manifest parity, skill metadata/size and JSON checks passed')
