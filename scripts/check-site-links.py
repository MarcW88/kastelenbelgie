from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin,urlsplit,unquote
import sys
R=Path('.').resolve(); files=[x for x in R.rglob('index.html') if not any(t in x.parts for t in ('.git','.agents','node_modules','content','.artifacts','.github'))]
class P(HTMLParser):
 def __init__(self): super().__init__();self.ids=[];self.links=[];self.base=None;self.images=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='a' and 'href' in d:self.links.append(d['href'])
  if t=='base':self.base=d.get('href')
  if t in ('img','script') and 'src' in d:self.images.append(d['src'])
pages={}
for f in files:
 p=P();p.feed(f.read_text());pages['/' if f.parent == R else '/' + f.parent.relative_to(R).as_posix() + '/']=p
bad=[]
for route,p in pages.items():
 for ref in p.links+p.images:
  u=urlsplit(urljoin(urljoin('https://kastelenbelgie.be'+route,p.base or route),ref))
  if u.netloc!='kastelenbelgie.be' or u.scheme not in ('http','https'):continue
  target=unquote(u.path)
  if target.endswith('/'):
   if target not in pages:bad.append((route,ref,'route'))
   elif u.fragment and unquote(u.fragment) not in pages[target].ids:bad.append((route,ref,'anchor'))
  elif not (R/target.lstrip('/')).is_file():bad.append((route,ref,'asset'))
print('routes',len(files),'errors',len(bad));print('\n'.join(map(str,bad[:100])));sys.exit(bool(bad))
