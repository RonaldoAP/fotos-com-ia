# 05 — Consistência de rosto e corpo no Nano Banana Pro

No Nano Banana Pro (Gemini 3 Pro Image), a consistência vem **muito mais das imagens de
referência do que do texto**. O texto controla cena, pose e luz; as **imagens** controlam
quem é a pessoa. Estratégia = referências boas + reuso disciplinado.

## Regra de ouro

> A identidade vem das **imagens que você anexa**, não da descrição. Consistência =
> referências coerentes + reuso da âncora, não prompt perfeito.

## 1. Kit de referência da personagem

O Pro aceita **várias imagens de referência ao mesmo tempo** (até ~14). Não suba só 1 foto —
monte um conjunto coerente da mesma pessoa:

**Rosto (prioridade máxima):**
- frente, bem iluminada, expressão neutra
- 3/4 (meio perfil)
- perfil
- uma com outra expressão (sorrindo)
- luz uniforme, sem sombra pesada, sem variação grande de maquiagem

**Corpo (mais difícil que o rosto):**
- corpo inteiro de frente
- de lado / 3/4
- roupa justa/neutra para o modelo ler a silhueta e as proporções

## 2. Foto-âncora (hero shot)

Quando sair uma geração perfeita, ela vira a **âncora mestre**:
- reuse **sempre a mesma** âncora como referência principal
- **nunca encadeie** (gerar a partir da geração anterior repetidamente) — o erro acumula e o
  rosto deriva (face morphing). Volte sempre à âncora original.

## 3. Separe identidade de cena (multi-referência)

> "Mantenha a mesma pessoa/rosto/corpo das imagens de referência. Coloque-a nesta cena/pose."

Kit da personagem (identidade) + prompt do cenário (biblioteca) = foto nova, mesma pessoa.

## 4. Trave também no texto (cinto + suspensório)

Junto das imagens, cole a **mini-ficha** (`personagem/mini-ficha.md`): idade, cabelo, biotipo,
tom de pele e exclusões (sem tatuagem/piercing/joia). Não substitui as imagens, mas reduz a
deriva. Mantenha-a **ampla** — texto detalhado de rosto briga com a referência visual.

## 5. Mude uma coisa de cada vez

Ao gerar um cenário novo, **só mude a cena**. Não troque rosto + cabelo + pose + local no mesmo
prompt. Identidade fixa, cenário variável.

## 6. Corrija por edição, não por re-geração

Se o rosto saiu 90% certo, use a **edição/inpaint**: "ajuste o rosto para ficar igual à
referência, mantendo o resto da imagem". Conserta a deriva sem perder a cena boa.

## 7. Loop de curadoria

Gere 3–4 variações, escolha a mais fiel, **promova a âncora** e descarte o resto. Com o tempo
você acumula um banco de âncoras aprovadas por cenário.

---

## Fluxo resumido

1. **Kit de referência** (rosto multi-ângulo + corpo) → fixo.
2. **Hero shot** aprovada → âncora mestre.
3. Nova foto = kit/âncora (identidade) + prompt de cenário (biblioteca) + mini-ficha (texto).
4. Sempre voltar à âncora, nunca encadear.
5. Ajuste fino por edição, não re-geração.
