#!/usr/bin/env python3
"""Extrai a paleta de cores (HEX) de uma foto de referência, no estilo dos prompts do Soul 2.0.

Uso:  python3 ferramentas/paleta.py caminho/da/foto.jpg [n_cores]
Saída: uma linha pronta pra colar no fim do AMBIENTE do prompt:
       HEX: ["#376260", "#3e2f18", ...]
Requer: pip install pillow
"""
import sys
from PIL import Image

def paleta(caminho, n=12):
    img = Image.open(caminho).convert("RGB")
    img.thumbnail((300, 300))                      # rápido e ignora ruído fino
    q = img.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[: n * 3]
    contagem = sorted(q.getcolors(), reverse=True)  # [(qtd, índice), ...] mais frequente primeiro
    cores = []
    for _, i in contagem:
        r, g, b = pal[i * 3 : i * 3 + 3]
        hx = f"#{r:02x}{g:02x}{b:02x}"
        if hx not in cores:
            cores.append(hx)
    return cores

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    cores = paleta(sys.argv[1], n)
    print("HEX: [" + ", ".join(f'"{c}"' for c in cores) + "]")
