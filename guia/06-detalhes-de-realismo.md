# 06 — Detalhes de realismo (âncoras pra deixar a foto mais real)

Pequenos detalhes imperfeitos que "vendem" que a foto é real. **Salpique 2–4 por foto** que
combinem com a cena — não use tudo de uma vez (excesso vira bagunça e pode até atrapalhar).

## Pele (o que mais importa)
Poros visíveis · sardas · uma espinha ou outra · olheiras leves · vermelhidão nas
bochechas/nariz · leve oleosidade na zona T · penugem no rosto · linhas de expressão ·
marca de bronzeado desigual · pequena cicatriz.

## Cabelo
Fios soltos/rebeldes no rosto · leve frizz · raiz aparecendo · meio bagunçado · marca do
elástico · fios grudados de suor.

## Câmera / luz (assinatura de celular real)
Grão de pouca luz · um cantinho estourado de luz · leve subexposição · flare/reflexo ·
sombra dura · foco levemente errado · leve motion blur · distorção de lente frontal ·
reflexo do flash nos olhos · marca de dedo/poeira na lente.

### 📄 O que deixa a foto natural (lições do PDF "AI Models — Soul 2.0 / GPT Image 2")
Parte da naturalidade daquelas fotos vem do **modelo** (Soul 2.0 é treinado pra foto de rede social).
Mas os prompts têm técnicas que copiamos:

1. **Escrever como legenda de uma foto que já existe**, não como ordem: "Foto casual de perto…",
   com palavras de incerteza ("provavelmente", "parece"). O modelo trata como foto real.
2. **Defeitos de câmera descritos de forma positiva**, quase sem "sem X": "foco nítido no rosto, leve
   suavidade da lente nas bordas, fundo um pouco mais suave e com compressão digital". Negação demais
   confunde o modelo — por isso os blocos fixos foram reescritos assim.
3. **Luz física, com 2 fontes e temperatura por lado do rosto** (ex.: neon quente rosado à direita,
   fluorescente fria à esquerda).
4. **Paleta + HEX**: listar as cores dominantes e os códigos HEX da foto de referência no fim do
   AMBIENTE. Extrair com `python3 ferramentas/paleta.py foto.jpg`.
5. **Linha de clima** no fim da POSE: "íntimo, casual e relaxado", "cru, real, não produzido".
6. **Enquadramento casual**: "levemente fora do centro", "levemente torto", "de cima, olhando pra lente".

**Não copiar:** descrição de rosto ("lábios carnudos", "traços de modelo") — puxa o rosto pra longe da
referência (regra do `guia/05`); descrições de corpo sexualizadas e joias (regras do projeto).

### ⭐ Bloco de imperfeição / naturalidade (fixo em TODO prompt, antes do bloco de câmera)
**Foto perfeita = foto de IA.** O que torna uma foto real é o que dá "errado": momento no meio da
ação, cabelo fora do lugar, roupa amassada, enquadramento amador cortando partes, foco imperfeito,
luz desigual e fundo sem arrumar. Descrever tudo "no lugar certinho" gera foto posada. Por isso todo
prompt tem este bloco logo antes do bloco de câmera (exemplo-base: EXT98):

> **PT:** foto casual tirada no momento, com enquadramento meio torto e fora do centro e partes cortadas pelas bordas, expressão natural do momento, alguns fios de cabelo fora do lugar e roupa com leves amassados; crua, real e não produzida, com cara de foto comum postada no Instagram;
>
> **EN:** a casual, in-the-moment photo with slightly tilted, off-center framing and parts cut off by the edges, a natural in-the-moment expression, a few stray hairs and lightly creased clothes; raw, real and not produced, like an ordinary photo posted on Instagram;

**Dicas pra reforçar por cena:** expressão "no meio" (rindo de verdade, falando, piscando, olhando pro
lado); um detalhe de roupa imperfeito (fiapo, alça torta, blusa subindo); um corte "errado" (braço, pé,
topo da cabeça). ⚠️ Isso **não** vale pra pele — pele continua no "bloco de pele seguro" (senão vira acne).

### ⭐ Bloco "cara de celular" (fixo em TODO prompt, no fim da POSE)
O que mais entrega foto de IA é o **desfoque de fundo de câmera profissional (bokeh)** e a luz
"perfeita". Celular faz o contrário: lente grande-angular, quase tudo em foco e processamento
digital visível. Por isso todo prompt termina com este bloco, antes de "foto realista…":

> **PT:** provavelmente tirada com a câmera de um celular moderno: foco nítido no rosto, leve suavidade da lente nas bordas, fundo um pouco mais suave e com compressão digital, leve processamento digital de celular, cores naturais e balanço de branco automático;
>
> **EN:** likely captured on a modern smartphone: sharp focus on the face, slight lens softness at the edges, a slightly softer, digitally compressed background, light phone processing, natural colors and auto white balance;

Já aplicado em todos os prompts de `prompts/exemplos.md` e `prompts/externos.md`. Ele **soma**
com as âncoras da cena (grão, torto, flash, motion blur) — não substitui.

### 🎞️ Preset de efeito: flash com arrasto (slow sync) + filme 35mm
Efeito de foto noturna de rua em que o **flash congela o rosto nítido** e o obturador lento deixa
**rastro de movimento** no cabelo, nas mãos e nas luzes. Colar no fim da POSE **no lugar** do bloco
"cara de celular" (aquele bloco pede "quase tudo em foco", o que briga com o rastro).

> **PT:** efeito de flash direto com obturador lento (flash com arrasto): o rosto e o corpo congelados e
> nítidos pelo flash, com um leve contorno fantasma em volta; o cabelo em movimento com rastro borrado;
> a mão em movimento levemente borrada; as luzes do fundo esticadas em riscos e manchas de luz quente
> por causa do movimento da câmera; fundo escuro com luzes amareladas e vermelhas borradas; pele com
> brilho do flash e blush rosado estourado nas bochechas, brancos da roupa levemente estourados; look de
> câmera compacta analógica de 35mm: grão de filme visível, cores quentes puxando pro laranja e dourado,
> pretos levemente lavados, leve vinheta nos cantos; foto realista, sem retoque, sem cara de IA.
>
> **EN:** direct flash with slow shutter (drag-the-shutter / slow-sync flash): the face and body frozen
> sharp by the flash, with a faint ghost outline around them; the moving hair with a blurred motion
> trail; the moving hand slightly blurred; the background lights stretched into streaks and smears of
> warm light from camera movement; dark background with blurred yellow and red lights; flash sheen on the
> skin and blown-out rosy blush on the cheeks, whites of the clothes slightly blown out; 35mm analog
> point-and-shoot look: visible film grain, warm colors leaning orange and gold, slightly lifted blacks,
> slight vignette in the corners; realistic photo, no retouching, no AI look.

Funciona melhor em cena **noturna com luzes no fundo** (rua, festa, restaurante) e com **algo se
mexendo** (cabelo virando, mão, pessoas passando). Pra reforçar o rastro, escrever na POSE o
movimento: "virando a cabeça rápido, cabelo balançando".

### 📱 Preset de efeito: selfie de iPhone 11 com flash frontal (Retina Flash)
Selfie com a câmera frontal em que a **tela acende branca** como flash. Colar no fim da POSE **no
lugar** do bloco "cara de celular".

> **PT:** selfie da câmera frontal de um iPhone 11 com o flash de tela (a tela acende branca na frente
> do rosto): luz chapada, suave e bem de frente, com tom levemente rosado/frio, iluminando o rosto e o
> que está mais perto da câmera e deixando o fundo escuro e apagado; brilhos fortes e molhados na boca,
> na ponta do nariz, nas maçãs e na testa; reflexo retangular claro da tela nos olhos; lente frontal
> grande-angular bem perto, deixando mão e nariz um pouco maiores; qualidade de câmera frontal de iPhone
> antigo em pouca luz: ruído visível, suavização de redução de ruído borrando os detalhes finos da pele e
> do cabelo, sombras esmagadas, leve compressão JPEG, balanço de branco puxando pro magenta; foto
> realista, sem retoque, sem cara de IA.
>
> **EN:** iPhone 11 front-camera selfie with the screen flash (the screen lights up white in front of the
> face): flat, soft, fully frontal light with a slightly pinkish/cool tone, lighting the face and whatever
> is closest to the camera while the background stays dark and dull; strong wet-looking highlights on the
> lips, nose tip, cheekbones and forehead; a light rectangular screen reflection in the eyes; wide-angle
> front lens very close, making the hand and nose slightly larger; old-iPhone front-camera quality in low
> light: visible noise, noise-reduction smoothing smearing fine skin and hair detail, crushed shadows,
> mild JPEG compression, white balance leaning magenta; realistic photo, no retouching, no AI look.

## Enquadramento
Torto · cortando parte da cabeça/ombro · descentralizado · horizonte inclinado · "espaço
morto" no quadro.

## Ambiente real (bagunça)
Fundo bagunçado (roupa jogada, louça na pia, cabos) · espelho com marca de dedo · reflexo do
flash no espelho · objetos banais do dia a dia.

## Roupa
Amassada · etiqueta/costura aparecendo · tecido esticado · fiapo/pelo na roupa · suor.

## Corpo natural
Postura relaxada (não perfeita) · mãos em posição natural · dobras naturais da pele ao
sentar/dobrar · veias leves nas mãos · estrias finas · marca de roupa/meia na pele.

## Momento (vida acontecendo)
Pega no meio de um movimento · expressão espontânea (falando, quase rindo, piscando) ·
olhando pra fora do quadro · interagindo com um objeto.

---

## Combinações por tipo de foto (exemplos)

- **Selfie de dia:** distorção de lente frontal + fio de cabelo no rosto + poro/brilho na pele.
- **Foto noturna com flash:** grão + flash duro + reflexo nos olhos + sombra forte atrás.
- **Mirror selfie:** marca de dedo no espelho + enquadramento torto + reflexo da tela.
- **Praia:** brilho de suor + marca de bronzeado + areia/pegadas + fio ao vento.
- **Casa/cozy:** luz de janela com sombra dura + lençol amassado + cabelo bagunçado.

> Regra de ouro: **2–4 âncoras por foto**, escolhidas pelo contexto. Menos é mais.
> No Nano Banana, tudo isso vai **afirmado no texto** (não existe negative prompt).

---

## ⚠️ Cuidado: não exagere as imperfeições (senão vira "doença de pele")

Empilhar muitas âncoras de pele (sardas + sinais + vermelhidão irregular + poros + manchas)
faz o modelo interpretar como **acne/irritação** — aparece um aglomerado vermelho na bochecha,
pele com aspecto de problema. Aconteceu num teste real.

**Como evitar:**
- Sempre com **"leve/sutil"** (leve vermelhidão, poucas sardas).
- Adicione um **freio**: "pele **saudável**, sem acne, sem espinhas em excesso, sem irritação
  nem manchas vermelhas".
- Use **poucos** termos de imperfeição por vez, não a lista toda.

> **Bloco de pele "seguro" (PT):** pele com textura natural e saudável — poros e uma sardinha ou
> outra, leve vermelhidão suave e uniforme; sem acne, sem espinhas em excesso, sem irritação na pele.
>
> **(EN):** natural, healthy skin texture — pores and a few faint freckles, soft even redness; no
> acne, no clustered blemishes, no skin irritation or red patches.
