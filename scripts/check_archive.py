"""Validate the self-contained photography archive after `hugo --destination _site`."""
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1]
photos = json.loads((root / 'data/photos.json').read_text(encoding='utf-8'))
assert len(photos) == 68
assert len({p['name'] for p in photos}) == 68
assert [sum(p['week'] == w for p in photos) for w in (1,2,3)] == [30,19,19]
for photo in photos:
    for key in ('thumb','display','original'):
        path = root / 'static' / photo[key]
        assert path.is_file() and path.stat().st_size > 0, path

class Assets(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls=[]; self.photos=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        for key in ('src','href','data-photo','data-original'):
            if a.get(key): self.urls.append(a[key])
        if 'data-photo' in a: self.photos+=1

for page, count in [('index.html',68),('posts/week1/index.html',30),('posts/week2/index.html',19),('posts/week3/index.html',19)]:
    html=(root/'_site'/page).read_text(encoding='utf-8')
    assert 'bu.dusays.com' not in html and '7bu.top' not in html
    assert 'Bearer ' not in html and '@waline' not in html
    parser=Assets(); parser.feed(html)
    assert parser.photos==count, (page,parser.photos)
    for url in parser.urls:
        u=urlsplit(url)
        if u.scheme or not u.path: continue
        path=unquote(u.path).removeprefix('/bullshitPractice/').lstrip('/')
        target=root/'_site'/path
        assert target.exists(), (page,url)
print('PASS: 68 photos, 204 image assets, 4 pages, local links and no old image hosting.')
