# 07 — Tutorial: treinar um personagem novo (do zero, igual fizemos com a Vic)

Guia **passo a passo e reutilizável** para criar e "travar" um personagem novo no
**Nano Banana Pro (Gemini Image) via Freepik** — a mesma receita que usamos na Vic. Foi escrito
para outra pessoa (ou outra sessão) executar sozinha. Onde aparece **`[NOME]`**, troque pelo nome
do personagem novo.

> Base teórica: `personagem/00-consistencia.md` e `guia/05-consistencia-banana-pro.md`.
> Este arquivo é o **roteiro de execução**; aqueles dois explicam o "porquê".

---

## 0. O conceito em uma frase

A fidelidade do personagem **não vem do texto** — vem de um **kit de imagens de referência** (rosto
em vários ângulos + corpo) e de uma **foto-âncora (hero shot)** que se reusa sempre. O texto só
**trava regras** (sem joia, pele natural, etc.). Logo, "treinar o personagem" = **produzir e curar
esse kit de imagens**, e depois anexá-lo em toda geração.

**3 regras de ouro (valem pra qualquer personagem):**
1. **Nunca encadear.** Gere sempre a partir da âncora/kit, nunca a partir da última geração — o
   rosto deriva ("face morphing") e o erro acumula.
2. **O treino vira a média.** Se o set de referência tiver ângulos/cabelos/corpos variados demais
   ou fora do look-alvo, o modelo puxa pra essa média. Mantenha o set **homogêneo e no look-alvo**.
3. **Cobertura de ângulos importa.** O que não estiver no kit, o modelo **inventa** (e erra). Por
   isso o kit cobre frontal, 3/4, perfil, cima/baixo, sobre-o-ombro, close e corpo.

---

## 1. Visão geral do fluxo (5 fases)

```
FASE 1  Definir a ficha do personagem (identidade travada em texto)
FASE 2  Conseguir a foto-base (1 imagem de partida do rosto)
FASE 3  Gerar o KIT de ângulos do rosto (turnaround) + kit de corpo
FASE 4  Curar → escolher a HERO SHOT (âncora) e montar o SET de treino
FASE 5  (Opcional) Retreinar como Character na Library + loop de auto-expansão
```

Depois disso o personagem está "treinado": em qualquer cena nova você anexa **âncora + kit** e
escreve o prompt de cena (ver `prompts/templates.md`, formato de 5 campos).

---

## 2. FASE 1 — Ficha do personagem (texto travado)

Antes de gerar imagem, defina a **identidade fixa**. Preencha um bloco curto (a "mini-ficha") com:

- **Idade** aparente e **etnia/tom de pele**.
- **Rosto:** formato, olhos (cor), nariz, boca, marcas fixas (sardas, sinais, covinhas).
- **Cabelo:** cor, comprimento, textura (a cor/base é fixa; **o penteado é dito por cena**).
- **Biotipo:** magro / atlético / curvilíneo / plus etc. + altura aproximada.
- **Exclusões fixas** (o que NUNCA aparece): ex. *sem tatuagens, sem piercings, sem joias.*

> Modelo pronto: copie o formato de `personagem/mini-ficha.md` e `personagem/ficha-canonica.md` da
> Vic e só troque os valores. Essa mini-ficha é colada junto do prompt em toda geração, como reforço.

**Regra que vale pra todo personagem:** o **prompt de cena não descreve traços físicos** (isso a
referência puxa). A única exceção é o **penteado/estado do cabelo** (solto, preso, molhado, ao
vento), que **deve** ser dito por cena.

---

## 3. FASE 2 — Foto-base (a semente)

Você precisa de **1 imagem de partida** do rosto do personagem. Duas formas:

- **(A) Foto real** (recomendado se existir): uma foto nítida, de frente, boa luz. Ancora tudo e dá
  o personagem mais consistente.
- **(B) Só texto:** gere a primeira cara a partir da ficha (FASE 1) no Nano Banana, escolha a
  melhor e trate como foto-base. Menos previsível, mas funciona.

Requisitos da foto-base: rosto nítido, de frente, sem óculos escuros, sem sombra dura cortando o
rosto, cabelo afastado mostrando a linha do cabelo e as orelhas.

---

## 4. FASE 3 — Gerar o KIT de ângulos ⭐ (o coração do tutorial)

Aqui é onde os **ângulos** entram. A ideia é um **turnaround estilo foto de documento (RG)**: fundo
neutro cinza, **luz uniforme e limpa** (é referência de identidade, não foto "de celular" — o
realismo de snapshot entra só nas cenas), proporção **3:4 vertical**, **uma imagem por ângulo**.

### 4.1. Como rodar cada geração
1. Anexe a **foto-base** (FASE 2) como referência em **todas** as gerações.
2. Ajuste a proporção pra **3:4 vertical** na ferramenta.
3. Cole o **BLOCO BASE** (abaixo) **+ uma linha de ângulo**. Gere **um ângulo por vez**, 1–2
   variações cada.
4. Vá salvando as melhores de cada ângulo.

### 4.2. BLOCO BASE do kit (genérico — troque só a ficha)

**PT:**
> Retrato de referência estilo foto de documento (RG), proporção 3:4 vertical, da mesma pessoa da
> foto de referência anexada — rosto **idêntico** ao da referência. Fundo neutro liso cinza-claro e
> uniforme. Iluminação suave, difusa e uniforme sobre o rosto, sem sombras duras e sem luz dramática
> de estúdio. Expressão neutra e relaxada, boca fechada, olhos abertos. Cabelo afastado do rosto,
> deixando feições, orelhas e linha do cabelo bem visíveis. Blusa lisa e neutra de gola redonda.
> Pouca ou nenhuma maquiagem. **[EXCLUSÕES FIXAS DO PERSONAGEM — ex.: sem tatuagens, sem piercings,
> sem joias.]** Mantenha exatamente os traços do rosto da referência, sem embelezar, sem afinar o
> rosto, sem padronizar as feições. Textura de pele real com poros e pequenas imperfeições, sem
> suavização nem brilho de IA. Foco nítido e detalhado no rosto. Foto realista, não render 3D, não
> ilustração. **[ÂNGULO]**

**EN:**
> ID/passport-style reference portrait, 3:4 vertical aspect ratio, of the same person as in the
> attached reference photo — face **identical** to the reference. Plain, uniform light-grey neutral
> background. Soft, diffuse, even lighting on the face, no hard shadows and no dramatic studio
> light. Neutral, relaxed expression, mouth closed, eyes open. Hair pulled away from the face,
> keeping features, ears and hairline clearly visible. Plain neutral crew-neck top. Little to no
> makeup. **[FIXED EXCLUSIONS — e.g. no tattoos, no piercings, no jewelry.]** Keep the exact facial
> features from the reference, no beautifying, no slimming, no standardizing of the features. Real
> skin texture with pores and small imperfections, no smoothing or AI glow. Sharp, detailed focus on
> the face. Realistic photo, not a 3D render, not an illustration. **[ANGLE]**

### 4.3. Os ângulos — ROSTO (cobertura completa)

Cole **uma linha por geração** no lugar de `[ÂNGULO]`. Este conjunto cobre o essencial pra o modelo
não "inventar" pose:

| ID | Ângulo / expressão | Linha para colar |
|----|--------------------|------------------|
| A1 | **Frontal (0°)** | Cabeça e ombros de frente, olhando direto para a câmera, rosto totalmente frontal. |
| A2 | **3/4 esquerdo** | Cabeça virada ~45° para a esquerda (três-quartos), olhar acompanhando levemente. |
| A3 | **3/4 direito** | Cabeça virada ~45° para a direita (três-quartos). |
| A4 | **Perfil esquerdo (90°)** | Cabeça de perfil completo para a esquerda, rosto totalmente de lado. |
| A5 | **Perfil direito (90°)** | Cabeça de perfil completo para a direita. |
| A6 | **Câmera de cima** | Câmera um pouco acima; ela ergue o rosto olhando pra cima na direção da câmera. |
| A7 | **Câmera de baixo** | Câmera um pouco abaixo; ela olha pra baixo na direção da câmera, queixo levemente baixo. |
| A8 | **Cabeça inclinada** | Frontal, cabeça pendendo para um lado, olhando para a câmera. |
| A9 | **Rindo** | Frontal, riso espontâneo, sorriso aberto mostrando os dentes, olhos levemente apertados. |
| A10 | **Olhando para o lado** | Frontal, mas com o olhar voltado para fora do quadro (lado/cima). |
| A11 | **Sobre o ombro** | De costas, virando o tronco e olhando por cima do ombro para a câmera. |
| A12 | **Close de rosto** | Enquadramento bem fechado só no rosto (testa ao queixo), frontal, expressão neutra. |
| A13 | **Cabelo solto (âncora de penteado)** | Frontal, mesma luz/fundo, mas com o **cabelo totalmente solto** e com volume, caindo nos ombros. |

> Os 5 primeiros (A1–A5) são o **turnaround mínimo obrigatório**. A6–A12 tiram o modelo do
> "só-frontal". A13 fixa o cabelo solto (útil quando o kit foi feito com cabelo preso).

### 4.4. Os ângulos — CORPO (biotipo)

O corpo se trava melhor com **referência de forma** (ver 4.5). Gere pelo menos estes:

| ID | Ângulo | Linha para colar |
|----|--------|------------------|
| B1 | **Corpo de frente** | Corpo inteiro de frente, da cabeça aos pés, postura reta e neutra, braços relaxados. |
| B2 | **Corpo de costas** | Corpo inteiro de costas, mesma roupa neutra, mostrando as costas e o contorno. |
| B3 | **Corpo 3/4 de costas** | Corpo inteiro virado ~3/4 de costas, em pé, pose reta (mostra quadril). |
| B4 | **Corpo mostrando as pernas** | Corpo inteiro de frente, short curto, pernas e pés totalmente visíveis, câmera afastada na altura do quadril. |

No bloco de corpo, **descreva o biotipo do personagem** (ex.: "atlético-curvilíneo em ampulheta:
cintura fina, quadril largo, glúteos torneados, pernas definidas, barriga sequinha") e vista roupa
neutra justa (top + short/legging) pra mostrar a silhueta.

### 4.5. ⚠️ Dual-reference — corpos que fogem do "médio"

Texto sozinho tende a gerar **corpo médio**. Para biotipos marcantes (curvilíneo, plus, muito
atlético), anexe **2 imagens** na geração de corpo:
1. a **âncora de rosto** do personagem, **e**
2. uma **foto-guia de corpo** com a forma-alvo.

E amarre no texto: *"rosto idêntico à referência de ROSTO; corpo no formato da referência de
CORPO anexada"*. Alternativa: deixar o corpo pra **steerar só na cena** (mini-ficha + referência de
corpo na hora), sem "assar" no treino.

---

## 5. FASE 4 — Curadoria: hero shot + set de treino

1. **Hero shot (âncora):** escolha a **melhor frontal**, a mais fiel e nítida. Ela vira a
   **âncora** — anexada em toda geração dali pra frente. Guarde e **use sempre a MESMA**.
2. **Set de treino:** junte as melhores de cada ângulo. Descarte qualquer imagem onde o rosto
   "escorregou" — **imagem ruim no treino contamina** (regra 2 do §0).
3. Mantenha o set **homogêneo no look-alvo** (mesmo cabelo/base, biotipo certo). Se metade do set
   estiver fora do look, o personagem puxa pra ele.

### 5.1. ⭐ Limite de slots (ex.: Freepik = 9 fotos de treino)

Quando a ferramenta limita o nº de fotos, **priorize variedade de ROSTO** (é o que trava o
personagem) e deixe o corpo pra steerar na geração. Seleção sugerida de **9**:

```
1. Frontal neutro     4. Rindo              7. Sobre o ombro (giro)
2. 3/4 (um lado)      5. Cabeça inclinada   8. Corpo 3/4 de costas
3. Perfil (um lado)   6. Olhando pra baixo  9. Corpo de frente
```

> **7 rostos variados + 2 corpos.** O biotipo se reforça na geração anexando a referência de corpo
> (dual-ref, §4.5). Ângulos que sobraram entram depois no loop de auto-expansão (§6).

---

## 6. FASE 5 — Retreino e loop de auto-expansão (opcional, recomendado)

Depois que sair a primeira leva boa, o personagem melhora em ciclos:

1. **Cadastrar como Character na Library do Freepik** (reusa fácil; cadastre também locations/styles
   se tiver cenário fixo).
2. **Auto-expansão:** toda vez que faltar um ângulo (o modelo errou numa pose), gere **essa pose**
   com o BLOCO BASE (§4.2) a partir da âncora, cure a melhor e **some ao set**. Retreine.
3. Repita. O kit vira "auto-expansível": cada boa geração nova pode virar referência da próxima.

> **Nunca** retreine a partir de gerações encadeadas ruins. Sempre volte à âncora aprovada.

---

## 7. Checklist rápido (cola pra outra sessão)

```
[ ] Ficha/mini-ficha preenchida (idade, rosto, cabelo, biotipo, EXCLUSÕES fixas)
[ ] Foto-base do rosto em mãos (real ou gerada)
[ ] Proporção 3:4 vertical na ferramenta
[ ] Kit de rosto A1–A13 gerado (mínimo A1–A5), 1 ângulo por geração, foto-base anexada
[ ] Kit de corpo B1–B4 gerado (dual-reference se biotipo marcante)
[ ] Curadoria: descartadas as imagens com rosto "escorregado"
[ ] HERO SHOT escolhida (a frontal mais fiel) = âncora fixa
[ ] Set de treino montado; se houver limite, usar os 9 slots (7 rostos + 2 corpos)
[ ] (Opc.) Cadastrado como Character na Library + loop de auto-expansão
[ ] Regras: nunca encadear · treino homogêneo no look-alvo · cobrir ângulos
```

---

## 8. Erros comuns (e a causa)

| Sintoma | Causa provável | Correção |
|---|---|---|
| Rosto muda entre fotos | Encadeamento (gerou a partir da última geração) | Volte à âncora; nunca encadeie. |
| Personagem "puxa" pra outra cara | Set de treino heterogêneo / fora do look | Refaça o set homogêneo no look-alvo. |
| Erra poses fora do frontal | Kit sem cobertura de ângulos | Gere A6–A12 e retreine (loop §6). |
| Corpo vira "médio" | Só texto, sem guia de forma | Dual-reference (§4.5). |
| Cabelo errado por cena | Penteado não foi dito no prompt de cena | Diga o penteado em cada cena (exceção da regra). |
| Pele com acne/irritação | Excesso de "imperfeição" empilhada | Use o "bloco de pele seguro" (ver `guia/06`). |

---

*Referências no repo:* `personagem/kit-referencia-prompts.md` (turnaround R1–R9),
`personagem/set-expansao-angulos.md` (expansão X1–X10), `personagem/set-retreino-vic.md`
(retreino + dual-ref), `personagem/00-consistencia.md` e `guia/05-consistencia-banana-pro.md`
(teoria). Este tutorial é a versão **genérica e sequencial** desses documentos.
