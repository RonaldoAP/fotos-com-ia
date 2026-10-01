# 08 — Roteiro completo: montar uma personagem nova (da entrevista aos prompts finais)

Passo a passo **de ponta a ponta** pra criar uma influenciadora virtual nova do jeito que fizemos com a
Vic — da conversa inicial com o dono até os prompts finais e o ciclo de refinamento. Onde aparecer
**`[NOME]`**, troque pelo nome da personagem.

> Este é o roteiro **geral**. Detalhes de cada etapa: kit de ângulos → `guia/07`; realismo e presets
> de câmera → `guia/06`; consistência e trava de rosto (Seedream) → `guia/05`; formato de prompt e modo
> réplica → `prompts/templates.md`.

---

## Visão geral — 8 fases

```
FASE 1  Entrevista inicial (quem ela é)                  → questionário preenchido
FASE 2  Ficha canônica + mini-ficha + regras fixas        → personagem/ficha-[nome].md
FASE 3  Rosto-base (a "semente")                          → 1 foto de rosto aprovada
FASE 4  Kit de referência (ângulos de rosto + corpo)      → 13–17 imagens curadas
FASE 5  Hero shot + treino (Library/Character)           → âncora fixa + set de treino
FASE 6  Cenários fixos (quarto, casa, pet…)               → referências de ambiente
FASE 7  Prompts de cena (5 campos + 4 blocos fixos)       → biblioteca C1…, EXT1…
FASE 8  Refinamento contínuo (comparar → diagnosticar → ajustar) → prompts cada vez mais fiéis
```

---

## FASE 1 — Entrevista inicial

Antes de gerar qualquer imagem, conversar com o dono e preencher **todas** as respostas. É daqui que
saem a ficha, o estilo do feed e as regras. Perguntar uma seção por vez.

### 1.1 Identidade
- Nome da personagem e apelido.
- Idade aparente (faixa, ex.: 26–30).
- Nacionalidade / cidade onde "mora" e onde costuma aparecer (praia, cidade, interior…).
- Nicho do perfil: lifestyle, viagem, fitness, moda, beleza, gamer…
- Personalidade em 3 palavras (ex.: meiga, divertida, confiante) — define as **expressões**.

### 1.2 Aparência (o que vai virar referência visual)
- Tom de pele e subtom (claro rosado, moreno dourado…).
- Formato do rosto, cor dos olhos, sobrancelhas, nariz, boca — ou "igual a esta foto" (foto real ou
  gerada, ver Fase 3).
- Marcas fixas: sardas, pintas, covinhas, cicatriz.
- Cabelo: **cor e comprimento fixos** (ex.: loiro com ombré, comprido) + textura (liso, ondulado).
  O **penteado** muda por cena.
- Biotipo: magro / atlético / curvilíneo / plus + altura aproximada.

### 1.3 Regras fixas (exclusões)
- Tem tatuagem? Piercing? Usa joia? (A Vic: **nada disso, nunca.**)
- Óculos/fones/relógio: podem aparecer?
- Maquiagem padrão: natural, marcada, depende da cena?
- Unhas: curtas/longas, cor padrão?

### 1.4 Estilo e mundo
- Estilo de roupa (básico, praiano, fitness, elegante, streetwear…), cores favoritas.
- Cenários recorrentes: quarto dela, academia, praia, carro, restaurantes.
- Objetos-assinatura: celular (modelo e capinha — a Vic usa **iPhone 15 Pro Max titânio preto, capinha
  preta**), bolsa, garrafinha, pet.
- Tipo de foto que mais posta: mirror selfie, selfie frontal, foto que "alguém tirou", paisagem.

### 1.5 Limites de conteúdo
- O que **não** entra (a Vic: sem sexualização, sem lingerie/transparência, sem enquadramento de
  corpo/decote/bumbum, biquíni só como cena de praia/piscina, sem copiar rosto de pessoa real).
- O que fazer quando chega um print fora do limite (padrão: manter cena/luz/pose e trocar só o
  necessário, avisando o dono).

### 1.6 Ferramentas
- Onde vai gerar: Nano Banana Pro (Freepik/Magnific), Seedream 5 Pro, outro?
- A ferramenta aceita quantas imagens de referência? Tem Library/Character? Aceita negative prompt?

> **Entregável da Fase 1:** o questionário respondido, colado no topo de `personagem/ficha-[nome].md`.

---

## FASE 2 — Ficha canônica, mini-ficha e regras fixas

Transformar a entrevista em três blocos de texto (modelo: `personagem/ficha-canonica.md` e
`personagem/mini-ficha.md` da Vic).

1. **Ficha canônica** (completa, pra humanos): tudo da entrevista, organizado.
2. **Mini-ficha** (curta, pra colar junto do prompt quando precisar reforçar): idade, cabelo
   (cor/comprimento), biotipo, marcas fixas, exclusões.
3. **Regras fixas** que entram em **todo** prompt:
   - Exclusões: `sem joias, sem piercing, sem tatuagem` (ou as da personagem).
   - Objeto-assinatura (ex.: o celular padrão sempre que aparecer em quadro).

### ⚠️ O que o prompt de cena NUNCA descreve
Formato de rosto, olhos, nariz, **boca carnuda**, **sobrancelha grossa**, **pele bronzeada**, corpo.
Isso vem **da imagem de referência**. Descrever no texto puxa o rosto pra outra pessoa (lição aprendida
na Vic). No texto entram só: **cor/comprimento do cabelo, penteado da cena, maquiagem por cor**
(batom vermelho, blush rosado) e as exclusões.

---

## FASE 3 — Rosto-base (a semente)

Uma única imagem do rosto, nítida e de frente, que vira a origem de tudo.

- **(A) Foto real** (se existir e o dono tiver direito de uso): mais consistente.
- **(B) Gerada por texto:** gerar 8–12 rostos a partir da ficha e escolher 1.

**Prompt de rosto-base (quando não há foto) — PT:**
> Retrato fotorrealista de documento, 3:4 vertical, de uma mulher de [IDADE] anos, [TOM DE PELE],
> [COR DOS OLHOS], [MARCAS FIXAS: ex. sardas leves no nariz], cabelo [COR E COMPRIMENTO] afastado do
> rosto; expressão neutra, boca fechada, olhando pra câmera; fundo cinza-claro liso, luz suave e
> uniforme; pouca maquiagem; [EXCLUSÕES]; textura de pele real com poros, sem suavização; foto
> realista, não render 3D, não ilustração.

Critérios de escolha: rosto memorável mas comum (não "perfeito de IA"), simétrico só o natural,
combina com a personalidade, **não se parece com nenhuma pessoa famosa**.

---

## FASE 4 — Kit de referência (ângulos)

Com a foto-base anexada, gerar **um ângulo por vez**, 3:4 vertical, fundo cinza, luz uniforme.
Lista completa, blocos base e linhas de ângulo em **`guia/07`** (§4). Resumo:

- **Rosto (A1–A13):** frontal, 3/4 esq/dir, perfil esq/dir, câmera de cima/baixo, cabeça inclinada,
  rindo, olhando pro lado, sobre o ombro, close, cabelo solto.
  → **A1–A5 são obrigatórios.**
- **Corpo (B1–B4):** frente, costas, 3/4 de costas, mostrando pernas (roupa neutra justa).
- Biotipo marcante (curvilíneo, plus, muito atlético) → **dual-reference**: anexar o rosto + uma
  foto-guia de corpo.

Curadoria: descartar toda imagem em que o rosto "escorregou". Uma imagem ruim contamina o kit inteiro.

---

## FASE 5 — Hero shot e treino

1. **Hero shot (âncora):** a melhor frontal nítida do kit. É ela que vai como **Imagem 1** em toda
   geração, pra sempre. Guardar e nunca trocar sem motivo.
2. **Set de treino:** as melhores do kit, homogêneas (mesmo cabelo, mesmo biotipo).
   Limite de 9 fotos (Freepik): **7 rostos variados + 2 corpos** (ver `guia/07` §5.1).
3. **Cadastrar como Character** na Library da ferramenta, se houver.
4. **Regras de ouro:** nunca encadear (gerar a partir de uma geração anterior); treino homogêneo;
   cobrir ângulos (o que falta, o modelo inventa).

---

## FASE 6 — Cenários fixos

Para ambientes que se repetem (quarto dela, a casa, o carro, a academia de sempre):

1. Gerar um **kit do ambiente** em 4–6 ângulos (modelo: `cenarios/quarto-vic.md`, kit Q1–Q6), ou usar
   fotos reais do lugar.
2. Nos prompts, o ambiente **não é descrito**: usa-se `AMBIENTE: [AQUI — Imagem 2]` e anexa-se a foto.
3. Mesma lógica pra **roupa por referência** (`ROUPA: conforme a Imagem 3`) e pra **pet recorrente**.

---

## FASE 7 — Prompts de cena (o molde final)

Todo prompt tem **5 campos** (rótulo em MAIÚSCULA, linha em branco entre eles), versão **PT e EN**, e
**4 blocos fixos**:

| Bloco | Onde entra | Pra quê |
|---|---|---|
| **1. Trava de rosto** | PERSONAGEM | Ancora a identidade na Imagem 1 (essencial no Seedream) |
| **2. Pele segura** | DETALHES DA PESSOA | Textura real sem virar acne |
| **3. Imperfeição discreta** | fim da POSE | Foto comum, não posada — mas sem exagero |
| **4. Câmera** | fim da POSE | Cara de celular: suave, sem nitidez exagerada, sem bokeh |

### Molde completo (PT) — copiar e preencher os `[ ]`

```
PERSONAGEM: a mulher da Imagem 1 ([NOME]). Use a Imagem 1 SOMENTE para a identidade: rosto idêntico ao da Imagem 1 — mesmo formato de rosto, maxilar e queixo, mesmos olhos, nariz, boca e sobrancelhas, mesmas proporções, sardas e pintas, mesma idade aparente e mesmo tom de pele; não embelezar, não afinar, não padronizar e não misturar com nenhum outro rosto. As demais imagens anexadas servem só pro que o texto indicar (cenário/roupa); pose, roupa, luz e cenário vêm do texto abaixo.

AMBIENTE: [lugar, hora do dia; o que aparece atrás e dos lados, com cor e material; luz descrita como numa legenda — de onde vem, se é dura ou suave, a cor, e se tem duas fontes (ex.: neon quente num lado do rosto, fluorescente fria no outro); paleta de cores dominantes; HEX: ["#...", "#..."] tirados da foto com ferramentas/paleta.py]  — ou [AQUI — Imagem 2]

ROUPA: [peça de cima] + [peça de baixo] + [calçado/acessório funcional], com cor, tecido e caimento.

DETALHES DA PESSOA: cabelo [COR DA PERSONAGEM], [penteado da cena]; [expressão e pra onde olha]; [maquiagem só por cor]; pele com textura natural e saudável — poros e uma sardinha ou outra, leve vermelhidão; sem acne, sem excesso de imperfeição; [EXCLUSÕES FIXAS].

POSE: [posição do corpo, braços, mãos e o que seguram]; [quem tira a foto, altura e ângulo da câmera]; [onde ela fica no quadro e onde o quadro corta]; [+ celular padrão se aparecer]; [clima da foto: ex. íntimo, casual e relaxado]; foto casual tirada no momento, com enquadramento meio torto e fora do centro e partes cortadas pelas bordas, expressão natural do momento, alguns fios de cabelo fora do lugar e roupa com leves amassados; crua, real e não produzida, com cara de foto comum postada no Instagram; provavelmente tirada com a câmera de um celular moderno: foco nítido no rosto, leve suavidade da lente nas bordas, fundo um pouco mais suave e com compressão digital, leve processamento digital de celular, cores naturais e balanço de branco automático; foto realista, sem retoque, sem cara de IA.
```

### Molde completo (EN)

```
CHARACTER: the woman from Image 1 ([NAME]). Use Image 1 ONLY for identity: face identical to Image 1 — same face shape, jaw and chin, same eyes, nose, mouth and brows, same proportions, freckles and moles, same apparent age and same skin tone; do not beautify, slim, standardize or blend with any other face. Any other attached images are only for what the text says (setting/outfit); pose, outfit, light and setting come from the text below.

SETTING: [place, time of day; what is behind and at the sides, with color and material; light described like a caption — where it comes from, hard or soft, its color, and any second source (e.g. warm neon on one side of the face, cool fluorescent on the other); dominant color palette; HEX: ["#...", "#..."] taken from the photo with ferramentas/paleta.py]  — or [HERE — Image 2]

OUTFIT: [top] + [bottom] + [footwear/functional accessory], with color, fabric and fit.

PERSON DETAILS: [CHARACTER'S HAIR COLOR] hair, [hairstyle for the scene]; [expression and where she looks]; [makeup by color only]; natural, healthy skin texture — pores and a few faint freckles, soft redness; no acne, no over-imperfection; [FIXED EXCLUSIONS].

POSE: [body position, arms, hands and what they hold]; [who takes the photo, camera height and angle]; [where she sits in the frame and where the frame cuts]; [+ standard phone if it shows]; [photo mood: e.g. intimate, casual and relaxed]; a casual, in-the-moment photo with slightly tilted, off-center framing and parts cut off by the edges, a natural in-the-moment expression, a few stray hairs and lightly creased clothes; raw, real and not produced, like an ordinary photo posted on Instagram; likely captured on a modern smartphone: sharp focus on the face, slight lens softness at the edges, a slightly softer, digitally compressed background, light phone processing, natural colors and auto white balance; realistic photo, no retouching, no AI look.
```

### 7.1 Presets de câmera (trocar o bloco 4 quando a foto pedir)
- **Flash com arrasto + filme 35mm** (noite, rastro de movimento) — `guia/06`.
- **Selfie de iPhone 11 com flash frontal** (tela acende, luz chapada rosada) — `guia/06`.
- **Filme analógico com flash** (tom esverdeado, grão) — exemplo no EXT99.
Usar **só um** por prompt, no lugar do bloco "cara de celular".

### 7.2 Cenas próprias × prints
- **Cena própria** (ideia nova): vai pra `prompts/exemplos.md` como **C[n]**.
- **Print recebido**: vai pra `prompts/externos.md` como **EXT[n]**, no **modo réplica** (7.3).

### 7.3 Modo réplica (quando o dono manda um print)
Reproduzir **exatamente**: composição (onde ela está no quadro e o que corta), câmera (quem tira,
altura, ângulo, distância), pose, expressão, luz (direção, cor, o que fica no escuro), coloração, textura
da imagem, cada objeto do cenário, roupa (cor/tecido/caimento). Checklist completo em
`prompts/templates.md` ("Modo réplica").

**Só 4 exceções**, sempre avisadas ao dono numa linha no topo da entrada:
1. Joia/piercing/tatuagem saem (e texto/legenda/logo do print).
2. Rosto, cor de cabelo e corpo vêm da personagem.
3. Lingerie/transparência/peça íntima → peça equivalente mais próxima (mesmo corte e cor).
4. Recorte feito pra destacar corpo → mesma pose e luz, muda só o mínimo.

Ombros nus sem roupa visível → escrever a peça ("top de alcinha", "toalha presa acima do peito") pra o
gerador não ler como nudez e bloquear.

---

## FASE 8 — Gerar e refinar

### 8.1 Como gerar
1. **Imagem 1 = hero shot da personagem**, sempre anexada **primeiro**.
2. Imagem 2/3 = ambiente/roupa, só se o prompt disser `[AQUI — Imagem 2]` / `conforme a Imagem 3`.
3. **No máximo 3 imagens.** Nunca anexar o print original de outra pessoa.
4. Gerar **3–4 variações**, escolher a mais fiel. **Nunca encadear.**
5. Sequência da mesma sessão (mesma roupa/lugar): a imagem aprovada entra como **Imagem 2** (cenário/
   roupa) nas próximas — o rosto continua vindo da Imagem 1.

### 8.2 Ciclo de refinamento
```
gerar → comparar LADO A LADO com o print/ideia → listar diferenças → achar a causa no prompt
      → mudar UMA coisa por vez → gerar de novo → quando acertar, salvar e commitar
```
Mudar uma categoria por vez, nesta ordem: **composição → rosto → luz → textura/detalhe.**

### 8.3 Tabela de diagnóstico (sintoma → causa → correção)

| Sintoma | Causa provável | Correção |
|---|---|---|
| Rosto muda / parece outra pessoa | Imagens sem papel definido; traço de rosto descrito no texto; encadeamento | Trava de rosto na Imagem 1; tirar "boca carnuda/sobrancelha grossa/pele bronzeada"; sempre partir da âncora |
| Nítido demais, HDR "crocante", cara de IA | Prompt pedindo nitidez/detalhe/HDR | Bloco de câmera suave ("pouco detalhe fino, sem nitidez exagerada, JPEG de rede social") |
| Careta, gargalhada, cabelo desgrenhado | Imperfeição escrita forte demais | Expressão "natural e sutil"; "poucos fios soltos"; imperfeições discretas |
| Foto certinha, posada, "de estúdio" | Tudo descrito "no lugar"; sem momento | Bloco de imperfeição + 1 detalhe "errado" concreto (fiapo, braço cortado, rindo no meio) |
| Fundo desfocado de câmera profissional | Modelo assume retrato | "quase tudo em foco, sem bokeh" (já no bloco) |
| Cenário inventado (ex.: pôs o Rio) | Descrição vaga do lugar | Descrever o que é **e o que não é** ("só pinheiros, sem paredão de pedra") |
| Pose diferente (pra frente em vez de pra trás) | Pose ambígua | Dizer direção do corpo e onde ficam as mãos ("braços abertos na barra **atrás** dela") |
| Distorção de grande-angular colada | Câmera perto demais | "tirada a uns 3 metros, perspectiva normal" |
| Acne / pele irritada | Excesso de imperfeição na pele | "Bloco de pele seguro"; imperfeição fica em cabelo/roupa/foto, nunca na pele |
| Joia/tatuagem aparecendo | Modelo copia padrão | Exclusões explícitas em DETALHES DA PESSOA |
| Texto/legenda do print aparece | Print anexado ou texto sem trava | Não anexar o print; "imagem limpa, sem texto, legenda ou figurinha" |
| Corpo "médio" | Só texto pro biotipo | Dual-reference com foto-guia de corpo |
| Flash que não devia / sem flash que devia | Não afirmado | Afirmar duas vezes (AMBIENTE e POSE): "sem flash" / "flash direto" |
| Gerador bloqueia | Ombros nus lidos como nudez; arma; roupa íntima | Escrever a peça de roupa; alternativa de pose; trocar peça íntima |

### 8.4 Registrar o que funcionou
Quando uma correção funciona, anotar na entrada do prompt (linha de observação) e, se valer pra todos,
virar regra no `HANDOFF.md` (seção 6) e no guia correspondente.

---

## Checklist final (copiar pra outra sessão)

```
FASE 1  [ ] Entrevista preenchida (identidade, aparência, regras, estilo, limites, ferramenta)
FASE 2  [ ] Ficha canônica + mini-ficha + exclusões + objeto-assinatura
FASE 3  [ ] Rosto-base escolhido (nítido, frontal, não parece famoso)
FASE 4  [ ] Kit de rosto A1–A13 (mín. A1–A5) + corpo B1–B4, curado
FASE 5  [ ] Hero shot definido (= Imagem 1 pra sempre) + set de treino + Character na Library
FASE 6  [ ] Kits dos cenários fixos (quarto etc.)
FASE 7  [ ] Molde com os 4 blocos (trava de rosto, pele segura, imperfeição discreta, câmera suave)
        [ ] Cenas próprias em exemplos.md (C1…) e prints em externos.md (EXT1…) no modo réplica
FASE 8  [ ] Gerar com Imagem 1 primeiro, máx. 3 refs, 3–4 variações, nunca encadear
        [ ] Comparar lado a lado, corrigir uma coisa por vez, registrar o que funcionou
```
