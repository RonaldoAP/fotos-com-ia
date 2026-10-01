# Templates — modelos reutilizáveis

Preencha os `[colchetes]` e gere no Nano Banana 2. Cada template já traz as 6 camadas e o
bloco anti-IA embutidos. Há versão **PT** e **EN** (o EN costuma render um pouco melhor).

---

## ⭐ Modo réplica — foto de referência = cópia exata

Quando o dono manda uma foto, o prompt é uma **réplica fiel** dela. Não simplificar, não "melhorar",
não trocar cor/peça/luz/pose por gosto. Antes de escrever, passar pelo checklist e colocar **cada
item** no campo certo dos 5 campos:

| Item | O que descrever com precisão | Campo |
|---|---|---|
| Composição | onde ela está no quadro (esquerda/centro/direita, cortada pela borda?), o que ocupa o resto, espaço vazio acima/abaixo, proporção | POSE |
| Câmera | quem tira (selfie frontal/traseira, espelho, outra pessoa), altura (chão/peito/olho/acima), inclinação (de baixo/de cima), distância, lente (grande-angular, distorção) | POSE |
| Corte | de onde até onde o corpo aparece (topo da cabeça até…), o que é cortado pela borda | POSE |
| Pose | posição do corpo, ombros, cabeça (inclinação, queixo), braços, mãos (o que seguram/onde), pernas | POSE |
| Expressão | olhos (abertos/semicerrados/fechados, pra onde olham), boca, sorriso | DETALHES |
| Cabelo | penteado e como cai (lado, frente, costas, molhado, bagunçado) — cor vem da Vic | DETALHES |
| Luz | fonte, direção, dureza, cor/temperatura, o que fica iluminado e o que fica no escuro, altas-luzes estouradas | AMBIENTE |
| Cor/tratamento | paleta dominante, saturação, contraste, se é escuro/claro, filtro, cor da pele sob aquela luz | AMBIENTE/POSE |
| Textura de imagem | grão, ruído, nitidez, compressão, motion blur, flash, marca no espelho | POSE |
| Cenário | cada objeto visível, com cor, material e posição (primeiro plano / fundo) | AMBIENTE |
| Paleta HEX | rodar `python3 ferramentas/paleta.py <foto>` e colar a linha `HEX: [...]` | AMBIENTE |
| Clima | 2–3 palavras de mood (íntimo, casual, relaxado / cru, real) | POSE |
| Roupa | peça, cor exata, tecido, textura (canelado, cetim…), caimento, detalhes | ROUPA |

**Só 4 exceções** (sempre avisar o dono do que mudou): (1) joia/piercing/tatuagem saem; (2) rosto,
cor de cabelo e corpo vêm da referência da Vic; (3) lingerie/transparência/peça íntima → peça
equivalente mais próxima (mesmo corte, cor, caimento); (4) recorte feito pra destacar corpo → mesma
pose/luz, só o corte muda o mínimo necessário.

---

## ⭐ Estrutura padrão (5 campos) — usar em todos os prompts

Todo prompt da Vic segue esta ordem de campos. Cada campo é uma **frase natural** (não é lista
de tags) — o Nano Banana lê linguagem natural, mas a ordem por campos deixa fácil trocar peça
por peça (só a roupa, só a pose, só o ambiente).

1. **Personagem** — quem é. Sempre a Vic, vinda das **imagens de referência** anexadas. Não
   descreve traços físicos (rosto, cor de cabelo, corpo) — isso a referência puxa.
2. **Ambiente** — onde. Um local descrito, **ou** `[AQUI]` quando for o quarto padrão da Vic
   (aí o ambiente vem da referência do quarto — ver `cenarios/quarto-vic.md`).
3. **Roupa** — o que veste. Descreve só a roupa/calçado (filtro-safe, sem sexualização).
4. **Detalhes da pessoa** — cabelo/penteado, expressão, luz no rosto e o **bloco de realismo**
   (pele saudável, sem acne) + as **exclusões fixas** (sem joia/piercing/tatuagem).
5. **Pose** — pose, enquadramento e a assinatura de celular (torto, grão, flash no espelho,
   iPhone 15 Pro Max titânio preto se o celular aparecer).

> **Formatação:** cada categoria em **MAIÚSCULA** seguida de `:` e com uma **linha em branco**
> entre elas (como nos exemplos abaixo).

### Molde (PT)

> PERSONAGEM: a mulher da Imagem 1 (Vic). Use a Imagem 1 SOMENTE para a identidade: rosto idêntico ao da Imagem 1 — mesmo formato de rosto, maxilar e queixo, mesmos olhos, nariz, boca e sobrancelhas, mesmas proporções, sardas e pintas, mesma idade aparente e mesmo tom de pele; não embelezar, não afinar, não padronizar e não misturar com nenhum outro rosto. As demais imagens anexadas servem só pro que o texto indicar (cenário/roupa); pose, roupa, luz e cenário vêm do texto abaixo.
>
> AMBIENTE: [local — ou [AQUI] pro quarto padrão]; [luz descrita como legenda: fonte, dureza, cor, segunda
> fonte]; [paleta de cores dominantes]; HEX: ["#...", "#..."] (tirar da foto com `ferramentas/paleta.py`).
>
> ROUPA: [peça de cima] + [peça de baixo] + [calçado].
>
> DETALHES DA PESSOA: [penteado]; [expressão/olhar]; pele com textura natural e saudável — poros e
> uma sardinha ou outra, leve vermelhidão; sem acne, sem excesso de imperfeição; sem joias, sem
> piercing, sem tatuagem.
>
> POSE: [pose e enquadramento]; foto de celular meio torta, grão suave [+ iPhone 15 Pro Max titânio
> preto, capinha preta, se o celular aparecer]; foto casual tirada no momento, com enquadramento meio torto e fora do centro e partes cortadas pelas bordas, expressão natural do momento, alguns fios de cabelo fora do lugar e roupa com leves amassados; crua, real e não produzida, com cara de foto comum postada no Instagram; provavelmente tirada com a câmera de um celular moderno: foco nítido no rosto, leve suavidade da lente nas bordas, fundo um pouco mais suave e com compressão digital, leve processamento digital de celular, cores naturais e balanço de branco automático;
> foto realista, sem retoque, sem cara de IA.

### Molde (EN)

> CHARACTER: the woman from Image 1 (Vic). Use Image 1 ONLY for identity: face identical to Image 1 — same face shape, jaw and chin, same eyes, nose, mouth and brows, same proportions, freckles and moles, same apparent age and same skin tone; do not beautify, slim, standardize or blend with any other face. Any other attached images are only for what the text says (setting/outfit); pose, outfit, light and setting come from the text below.
>
> SETTING: [place — or [HERE] for the standard bedroom]; [light described like a caption: source, hardness,
> color, second source]; [dominant color palette]; HEX: ["#...", "#..."] (from the photo via `ferramentas/paleta.py`).
>
> OUTFIT: [top] + [bottom] + [footwear].
>
> PERSON DETAILS: [hairstyle]; [expression/gaze]; natural, healthy skin texture — pores and a few
> faint freckles, soft redness; no acne, no over-imperfection; no jewelry, no piercings, no tattoos.
>
> POSE: [pose and framing]; slightly tilted phone photo, soft grain [+ black titanium iPhone 15 Pro
> Max, plain black case, if the phone shows]; a casual, in-the-moment photo with slightly tilted, off-center framing and parts cut off by the edges, a natural in-the-moment expression, a few stray hairs and lightly creased clothes; raw, real and not produced, like an ordinary photo posted on Instagram; likely captured on a modern smartphone: sharp focus on the face, slight lens softness at the edges, a slightly softer, digitally compressed background, light phone processing, natural colors and auto white balance; realistic photo, no
> retouching, no AI look.

### Exemplo preenchido (cena normal)

> PERSONAGEM: a mulher da Imagem 1 (Vic). Use a Imagem 1 SOMENTE para a identidade: rosto idêntico ao da Imagem 1 — mesmo formato de rosto, maxilar e queixo, mesmos olhos, nariz, boca e sobrancelhas, mesmas proporções, sardas e pintas, mesma idade aparente e mesmo tom de pele; não embelezar, não afinar, não padronizar e não misturar com nenhum outro rosto. As demais imagens anexadas servem só pro que o texto indicar (cenário/roupa); pose, roupa, luz e cenário vêm do texto abaixo.
>
> AMBIENTE: na areia de Ipanema no fim de tarde, mar e Dois Irmãos ao fundo; sol dourado de lado,
> um cantinho estourado de luz.
>
> ROUPA: biquíni de amarrar simples e colorido, óculos de sol na cabeça.
>
> DETALHES DA PESSOA: cabelo comprido solto ao vento; quase rindo, olhando pra câmera; pele com
> textura natural e saudável — poros e uma sardinha ou outra, leve marca de bronzeado; sem acne;
> sem joias, sem piercing, sem tatuagem.
>
> POSE: em pé, meio de lado, uma mão ajeitando o cabelo; foto de celular aberta, meio torta, grão
> suave no sol; foto realista, sem cara de IA.

### Exemplo preenchido (quarto padrão)

> PERSONAGEM: a mulher da Imagem 1 (Vic). Use a Imagem 1 SOMENTE para a identidade: rosto idêntico ao da Imagem 1 — mesmo formato de rosto, maxilar e queixo, mesmos olhos, nariz, boca e sobrancelhas, mesmas proporções, sardas e pintas, mesma idade aparente e mesmo tom de pele; não embelezar, não afinar, não padronizar e não misturar com nenhum outro rosto. As demais imagens anexadas servem só pro que o texto indicar (cenário/roupa); pose, roupa, luz e cenário vêm do texto abaixo.
>
> AMBIENTE: [AQUI] (referência do quarto da Vic); luz da LED do teto em roxo + abajur quente no
> rosto.
>
> ROUPA: camiseta branca larguinha e short preto de treino.
>
> DETALHES DA PESSOA: cabelo comprido solto caindo pro lado; biquinho de leve, olhar tranquilo;
> pele com textura natural e saudável — poros e uma sardinha ou outra, leve vermelhidão; sem acne;
> sem joias, sem piercing, sem tatuagem.
>
> POSE: deitada de bruços, apoiada nos cotovelos, selfie de braço esticado com o iPhone 15 Pro Max
> titânio preto (capinha preta); enquadramento meio torto, reflexo do flash na tela, grão suave;
> foto realista, sem cara de IA.

> Os templates T1–T… abaixo continuam válidos como variações; a **estrutura de 5 campos** é o
> formato principal daqui pra frente.

---

## T1 — Selfie de câmera frontal

**PT**
> Selfie de câmera frontal, braço estendido, de [pessoa: idade, gênero, traços], em
> [ambiente cotidiano], com [luz disponível]. Expressão espontânea, [meio sorriso /
> séria / rindo], olhando para a câmera. A pele mostra poros visíveis, textura real,
> [oleosidade leve na zona T / sardas / olheiras leves] e sem suavização; alguns fios
> de cabelo soltos. Leve distorção de lente frontal, enquadramento descuidado, grão
> sutil de celular. Foto real de celular, não retoque, não render 3D.

**EN**
> Front-camera selfie, arm's length, of [person: age, gender, features], in [everyday
> setting], under [available light]. Spontaneous expression, looking at the camera. Skin
> shows visible pores, real texture, [slight T-zone oiliness / freckles / faint under-eye
> circles], no smoothing; a few stray hairs. Slight front-lens distortion, careless
> framing, subtle phone grain. Real smartphone photo, no retouching, not a 3D render.

---

## T2 — Candid (alguém tirou de você)

**PT**
> Foto tirada de improviso por um amigo, de [pessoa], [ação espontânea: rindo / falando /
> distraída] em [ambiente], com [luz disponível]. Sem pose, pego de surpresa, enquadramento
> torto cortando [parte do corpo/fundo]. Pele com poros e textura natural, sem retoque;
> cabelo um pouco bagunçado. Leve desfoque de movimento, grão de celular, exposição
> equilibrada. Fotografia real, não ilustração.

**EN**
> Candid photo taken by a friend, of [person], [spontaneous action] in [setting], under
> [available light]. Unposed, caught off guard, tilted framing cropping [part]. Skin with
> pores and natural texture, no retouching; slightly messy hair. Subtle motion blur, phone
> grain, balanced exposure. Real photograph, not an illustration.

---

## T3 — Foto noturna com flash

**PT**
> Foto noturna com flash do celular, de [pessoa], em [ambiente à noite]. Luz dura e direta
> do flash, sombra forte atrás, fundo escuro. Pele com brilho natural do flash mostrando
> poros e textura, leve vermelhidão, sem suavização; olhos com leve reflexo do flash.
> Enquadramento casual, grão e ruído de foto noturna de celular. Foto real, não render.

**EN**
> Night phone-flash photo of [person], in [night setting]. Hard direct flash, strong
> shadow behind, dark background. Skin with natural flash sheen revealing pores and
> texture, slight redness, no smoothing; faint flash catchlight in the eyes. Casual
> framing, grain and noise of a night smartphone photo. Real photo, not a render.

---

## T4 — Retrato com luz de janela (dia nublado)

**PT**
> Foto de celular de [pessoa] perto da janela num dia nublado, [ação: olhando para fora /
> mexendo no celular], em [ambiente]. Luz suave e desigual da janela, um lado do rosto
> mais escuro. Pele detalhada com poros, penugem facial, linhas de expressão e sem
> retoque; acabamento fosco. Enquadramento simples e descentralizado, leve grão. Foto
> real de celular.

**EN**
> Smartphone photo of [person] by the window on an overcast day, [action], in [setting].
> Soft uneven window light, one side of the face darker. Detailed skin with pores, facial
> peach fuzz, expression lines, no retouching; matte finish. Simple off-center framing,
> subtle grain. Real phone photo.

---

## T5 — Corpo inteiro / na rua

**PT**
> Foto de celular de corpo inteiro de [pessoa], parada/andando em [local urbano cotidiano],
> [luz: sol forte / fim de tarde nublado]. Roupa comum e amassada, postura relaxada e
> natural. Pele com textura real; mãos em posição natural [no bolso / segurando sacola]
> com anatomia correta. Enquadramento descuidado, pessoas/fundo banal atrás, grão sutil.
> Fotografia real, não estúdio, não 3D.

**EN**
> Full-body smartphone photo of [person], standing/walking in [everyday urban spot], under
> [light]. Plain wrinkled clothes, relaxed natural posture. Real skin texture; hands in a
> natural position [in pockets / holding a bag] with correct anatomy. Careless framing,
> mundane background, subtle grain. Real photograph, not studio, not 3D.

---

## Modo natural (estilo padrão a partir de agora)

Prompts escritos como uma **descrição solta**, do jeito que você contaria pra um amigo — não como
lista técnica. Deixa a foto com mais cara de snapshot real e menos de "modelo posando". Os
cuidados (pele real, sem joia, identidade da Vic) continuam, só **diluídos no texto**.

**Molde mental:** _"Foto de celular da Vic [fazendo algo] em [lugar], [hora/luz]. Ela está [pose/
expressão casual], usando [roupa]. [O que dá pra ver no fundo]. [Clima da luz]. Pele real com
textura, sem retoque nem cara de IA. Sem tatuagem, piercing ou joia. Foto meio torta, com
grãozinho de celular."_

**Princípios:**
- Comece pelo **momento** ("dessas tiradas de qualquer jeito", "selfie rápida"), não por specs.
- Frases corridas e casuais; nada de bloco "Booster:" etiquetado.
- Mantenha o essencial **embutido**: foto de celular, pele real/sem retoque, "nada de cara de IA",
  sem joia/tatuagem/piercing, enquadramento descuidado, leve grão.
- Cor de cabelo/corpo continua vindo da personagem (não descrever traço).

> Exemplo (Ipanema): _"Foto de celular da Vic na praia de Ipanema num dia de sol, dessas tiradas
> meio de qualquer jeito. Ela está em pé na areia ajeitando o cabelo, de óculos escuros, camiseta
> verde do Brasil e short jeans. Atrás, o Dois Irmãos, o mar e a galera. Sol forte, sombra dura.
> Pele real com sardas e textura, sem filtro nem cara de IA. Sem joia, tatuagem ou piercing. Foto
> meio torta, com grãozinho de celular."_

## Presets de ambiente/luz (reaproveitáveis)

"Receitas" de **ambiente + luz + coloração**, separadas da pose e da roupa. Cole o preset e
troque só `[POSE]` e `[ROUPA]`. Servem pra manter um clima/estética em vários posts.

### Preset — Varanda ao anoitecer / skyline (hora azul)

- **Ambiente:** varanda de apê alto, corrimão de metal, cidade em silhueta com janelas acesas.
- **Luz:** hora azul (logo após o pôr do sol); céu azul profundo em cima, laranja no horizonte;
  ambiente escuro, rosto na luz ambiente + brilho quente da cidade; foto levemente subexposta.
- **Coloração:** moody e meio saturada (filtro de filme/VSCO): azul-petróleo + laranja quente,
  sombras fechadas/"esmagadas", realces quentes; amarelo/laranja da roupa estoura.
- **Câmera:** celular vertical, ângulo meio torto (dutch), grão de pouca luz, cabelo ao vento.

> **Cole e troque [POSE]/[ROUPA] (PT):** Foto de celular da Vic [POSE] numa varanda de apartamento
> alto ao anoitecer (hora azul), com a cidade em silhueta e janelas acesas lá embaixo, corrimão de
> metal do lado. Céu em degradê do azul profundo pro laranja no horizonte, ambiente escuro, foto
> levemente subexposta; clima moody meio saturado tipo filtro de filme (azul-petróleo + laranja
> quente), sombras fechadas. [ROUPA]. Cabelo solto meio ao vento. Pele real com sardas e textura,
> sem retoque nem cara de IA. Sem joia, tatuagem ou piercing. Ângulo meio torto, grão de pouca luz.

> **(EN):** A phone photo of Vic [POSE] on a high apartment balcony at dusk (blue hour), with the
> city in silhouette and lit windows below, a metal railing to the side. Sky gradient from deep blue
> to orange at the horizon, dark setting, slightly underexposed; moody, fairly saturated film-filter
> look (teal + warm orange), crushed shadows. [OUTFIT]. Hair down, a bit windblown. Real skin with
> freckles and texture, no retouching or AI look. No jewelry, tattoos or piercings. Slightly tilted
> angle, low-light grain.

## Como usar mãos com segurança

Sempre que o template mostrar mãos, prefira uma destas: **no bolso**, **segurando um
objeto** (xícara, celular, sacola), **apoiando o rosto**, ou **fora do quadro**. Se
precisarem aparecer abertas, acrescente: "mãos com exatamente cinco dedos, anatomia
correta".

---

## Formato alternativo — JSON estruturado ("mother reference")

Formato mais detalhado, em JSON, que separa `visual_prompt`, `negative_prompt`, câmera, luz e um
`identity_lock` (trava de identidade). Útil em ferramentas que aceitam prompt estruturado. **Molde
genérico já adaptado à Vic** — troque só os campos em `[COLCHETES]` por cena. As regras fixas da
Vic já vêm embutidas (rosto/cabelo/pele **vêm da referência**; sem joia/piercing/tatuagem;
filtro-safe, sem transparência/lingerie).

> ⚠️ **Traços que NÃO se descrevem aqui** (vêm das imagens de referência, não do texto): cor/formato
> do cabelo, cor de pele, formato de rosto/olhos/nariz/boca, sobrancelha, corpo. O texto só trava
> "manter idêntico à referência". A **única** coisa de aparência dita por cena é o **penteado**
> (`[PENTEADO]`: solto, coque, rabo, molhado, ao vento…).
>
> Nano Banana **ignora negative prompt** — por isso as exclusões também estão **afirmadas** no
> `visual_prompt`. O bloco `negative_prompt` serve só pra ferramentas que o respeitam.

```json
{
  "reference_type": "mother_reference_image",
  "visual_prompt": "A vertical smartphone [selfie/photo] of the same young adult woman as in the attached reference images (Vic), framed [ENQUADRAMENTO: ex. from the upper torso to the top of the head], photographed [ÂNGULO/PERSPECTIVA: ex. at close range, slightly high front-facing angle]. She has [EXPRESSÃO/OLHAR: ex. a calm expression looking at the camera]. Preserve the exact facial structure, natural asymmetry, skin tone, cheek volume, nose shape, lip shape and teeth alignment from the reference images, without beautification or retouching — do not restyle or slim the face. Her hair is worn [PENTEADO: ex. down / in a bun / windblown] (hair color, length and texture come from the reference images). She wears [ROUPA — filtro-safe, sem transparência/lingerie/peça íntima]. [MÃO/GESTO opcional: ex. one hand resting on the face; hand with exactly five fingers, correct anatomy]. No jewelry, no piercings, no tattoos. The background shows [AMBIENTE/CENÁRIO + [AQUI] se for o quarto padrão]. Lighting: [LUZ: fonte, direção, temperatura]. Casual smartphone qualities: close/informal framing, mild grain, warm-neutral color cast, slightly tilted; likely captured on a modern smartphone: sharp focus on the face, slight lens softness at the edges, a slightly softer, digitally compressed background, light phone processing, natural colors and auto white balance; realistic photo, not a 3D render, no AI look.",
  "negative_prompt": "changed identity, altered facial bone structure, different age or skin tone, hair recolored or restyled away from the reference; jewelry, earrings, septum or nose ring, rings, bracelets, necklaces; piercings; tattoos; sheer/see-through fabric, lingerie, visible undergarments, body-focused or sexualized framing; glamour or studio lighting, beauty retouching, porcelain skin, excessive symmetry, altered body proportions, artificial sharpness, CGI/3D/render texture, cartoon, brand logos, fantasy elements, extra fingers, deformed hands.",
  "camera_and_optics": {
    "format": "vertical smartphone [selfie/photo]",
    "framing": "[ENQUADRAMENTO]",
    "angle": "[ÂNGULO]",
    "perspective": "[PERSPECTIVA — ex. close-range selfie]",
    "focus": "face and upper torso in clear focus; background slightly softer"
  },
  "lighting": {
    "source": "[FONTE DE LUZ]",
    "shadow_behavior": "soft natural shadows under hair, chin, nose and neckline",
    "color_temperature": "[TEMPERATURA — ex. warm-neutral indoor daylight]",
    "highlight_behavior": "[COMPORTAMENTO DAS ALTAS-LUZES]"
  },
  "identity_lock": {
    "preserve": [
      "exact facial structure from the reference",
      "natural facial asymmetry",
      "skin tone and visible skin texture",
      "hair color, length and texture from the reference",
      "[PENTEADO da cena]",
      "[EXPRESSÃO/GESTO da cena]",
      "casual smartphone composition"
    ]
  }
}
```

**O que foi removido do exemplo original (porque não é da Vic):** cabelo escuro fixo, piercing de
septo, brinco de argola, pulseira com berloques, sobrancelha "escura marcante", e a blusa preta
**transparente/mesh sobre peça estruturada** (transparência → não é filtro-safe). No lugar,
placeholders neutros + as travas da Vic.
