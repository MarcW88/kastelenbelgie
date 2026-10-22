#!/usr/bin/env python3
"""Check exact cultural workflow copies and their active castle routing."""
import hashlib,json,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'scripts/verify_site_agents.py')],check=True)
lock=json.loads((ROOT/'.agents/museum-agents.lock.json').read_text())
for name,info in lock['files'].items():
 p=ROOT/name
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=info['sha256']:
  raise SystemExit('FAIL: original file missing or modified: '+name)
registry=(ROOT/'.agents/SKILL_REGISTRY.md').read_text()
required=set(re.findall(r'^- `([a-z][a-z0-9-]+)`',registry,re.M))
required.update(json.loads((ROOT/'.agents/reference/visite-musee/.agents/UPSTREAM_SOURCES.json').read_text())['required_skills'])
for skill in required:
 if not (ROOT/'.agents/skills'/skill/'SKILL.md').is_file():raise SystemExit('FAIL: missing specialist '+skill)
for directory in ['museum-analysis-workflow','museum-content-workflow']:
 d=ROOT/'.agents/skills'/directory
 for p in d.rglob('*.md'):
  for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
   if '://' in target or target.startswith('#'):continue
   if not (p.parent/target.split('#')[0]).is_file():raise SystemExit('FAIL: missing reference '+target)
routing=json.loads((ROOT/'.agents/shared-routing.json').read_text())
assert routing['families']['museum']==['museum-analysis-workflow','museum-content-workflow']
for prefix in ['/','/kasteel/','/kastelen/','/soorten/','/bezoeken/','/routes/','/inspiratie/','/gidsen/']:
 assert routing['routes'][prefix]=='museum', 'Wrong cultural routing: '+prefix
for prefix in ['/bronnen/','/contact/','/over-ons/']:assert routing['routes'][prefix]=='trust'
assert routing['domain_context']=='.agents/castle-context.md'
assert '## Cultural content — Visite Musée migration' in (ROOT/'AGENTS.md').read_text()
assert (ROOT/'.agents/castle-context.md').is_file()
print(f"PASS: {len(lock['files'])} exact original files, required specialists/references present, castle routing active")
