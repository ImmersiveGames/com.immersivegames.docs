from pathlib import Path

from PIL import Image


root = Path("PEGA/assets/documents/gdd")
ok = []
bad = []

for path in sorted(root.glob("*")):
    try:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            ok.append((path.name, image.size, path.stat().st_size))
    except Exception as error:
        bad.append((path.name, path.stat().st_size, str(error)))

print("ok", len(ok))
print(ok[:20])
print("bad", len(bad))
print(bad[:50])
