from pathlib import Path
import json

root = Path(__file__).parent
questions = json.loads((root / 'questions.json').read_text(encoding='utf-8'))
assert len(questions) >= 10, 'En az 10 soru olmalı'
assert len({q['id'] for q in questions}) == len(questions), 'Soru id değerleri benzersiz olmalı'
assert len({q['city'] for q in questions}) == len(questions), 'Her şehir bir kez yer almalı'
for q in questions:
    assert all(q.get(key) for key in ('city', 'region', 'landmark', 'hint', 'fact', 'illustration'))
    assert q['illustration'].startswith('<svg') and q['illustration'].endswith('</svg>')
template = (root / 'index.template.html').read_text(encoding='utf-8')
assert template.count('__QUESTIONS_PAYLOAD__') == 1
payload = json.dumps(questions, ensure_ascii=False, separators=(',', ':')).replace('</', '<' + chr(92) + '/')
html = template.replace('__QUESTIONS_PAYLOAD__', payload)
(root / 'index.html').write_text(html, encoding='utf-8')
print(f'✅ {len(questions)} şehirle index.html hazır — {len(html)} karakter')
