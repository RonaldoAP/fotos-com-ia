# Templates — modelos reutilizáveis

Preencha os `[colchetes]` e gere no Nano Banana 2. Cada template já traz as 6 camadas e o
bloco anti-IA embutidos. Há versão **PT** e **EN** (o EN costuma render um pouco melhor).

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

> PERSONAGEM: a mesma pessoa das imagens de referência anexadas (Vic).
>
> AMBIENTE: [local — ou [AQUI] pro quarto padrão]; [luz do ambiente].
>
> ROUPA: [peça de cima] + [peça de baixo] + [calçado].
>
> DETALHES DA PESSOA: [penteado]; [expressão/olhar]; pele com textura natural e saudável — poros e
> uma sardinha ou outra, leve vermelhidão; sem acne, sem excesso de imperfeição; sem joias, sem
> piercing, sem tatuagem.
>
> POSE: [pose e enquadramento]; foto de celular meio torta, grão suave [+ iPhone 15 Pro Max titânio
> preto, capinha preta, se o celular aparecer]; foto realista, sem retoque, sem cara de IA.

### Molde (EN)

> CHARACTER: the same person as in the attached reference images (Vic).
>
> SETTING: [place — or [HERE] for the standard bedroom]; [ambient light].
>
> OUTFIT: [top] + [bottom] + [footwear].
>
> PERSON DETAILS: [hairstyle]; [expression/gaze]; natural, healthy skin texture — pores and a few
> faint freckles, soft redness; no acne, no over-imperfection; no jewelry, no piercings, no tattoos.
>
> POSE: [pose and framing]; slightly tilted phone photo, soft grain [+ black titanium iPhone 15 Pro
> Max, plain black case, if the phone shows]; realistic photo, no retouching, no AI look.

### Exemplo preenchido (cena normal)

> PERSONAGEM: a mesma pessoa das imagens de referência (Vic).
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

> PERSONAGEM: a mesma pessoa das imagens de referência (Vic).
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
