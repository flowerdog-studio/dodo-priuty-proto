# Сборка: src/template.html → index.html (u(N) → calc(N*var(--u)), шрифт Dodo вшивается base64)
import re, base64, pathlib
here = pathlib.Path(__file__).parent
s = (here / 'template.html').read_text()
s = re.sub(r'\bu\((-?[\d.]+)\)', r'calc(\1*var(--u))', s)
font = base64.b64encode((here / 'Dodo-Narrow.ttf').read_bytes()).decode()
(here.parent / 'index.html').write_text(s.replace('__FONT__', font))
print('index.html собран')
