# 00 — Sistema de consistência da personagem

Como mantemos a **mesma pessoa** em todas as fotos do Nano Banana 2. A consistência vem
de três pilares combinados:

## Pilar 1 — Ficha canônica (texto travado)

Um bloco de descrição **idêntico em todo prompt**, definindo os traços que NÃO podem
mudar: formato do rosto, olhos, nariz, boca, tom de pele, marcas/sinais, cabelo (cor,
comprimento, textura), biotipo, altura e idade. Está em [`ficha-canonica.md`](ficha-canonica.md).

> Regra: a ficha é **copiada inteira** em cada prompt. A cena muda; a ficha, nunca.

### Exclusões fixas (em TODO prompt)

A personagem **não tem tatuagens, não tem piercings e não usa nenhuma joia ou bijuteria**
(sem brincos, colares, anéis ou pulseiras). O modelo às vezes adiciona esses itens sozinho,
então a frase abaixo entra em todo prompt:

> **PT:** Sem tatuagens, sem piercings e sem nenhuma joia ou bijuteria.
> **EN:** No tattoos, no piercings, and no jewelry of any kind.

## Pilar 2 — Foto-âncora (referência visual)

Assim que gerarmos a primeira foto perfeita dela (a "hero shot"), ela vira a **âncora**.
Nas gerações seguintes no Nano Banana 2, você anexa a âncora como imagem de referência e
pede para "manter a mesma pessoa/rosto desta imagem". Texto + imagem juntos travam a
identidade muito melhor do que só texto.

- Guarde a âncora aprovada e use sempre a MESMA.
- Se o rosto começar a derivar ("face morphing"), volte para a âncora original em vez de
  encadear foto sobre foto (o erro acumula).

## Pilar 3 — Fluxo de foto de referência → prompt

Quando você me enviar uma foto de referência (uma pose, cena ou estética que quer copiar):

1. Eu descrevo **somente o cenário, pose, enquadramento, luz e roupa** daquela foto —
   **sem nenhum traço físico** (cabelo, cor de pele, corpo, rosto). A pessoa é citada de
   forma neutra ("a mulher da imagem de referência").
2. Eu **colo a mini-ficha + as imagens** da personagem por cima — é daí que vêm cabelo,
   pele, corpo e rosto. Descrever traço no prompt de cenário só conflita com a referência.
3. Você recebe o prompt final em **PT e EN**, pronto para o Nano Banana 2 (texto +
   foto-âncora dela).

Assim copiamos a *vibe* da referência sem copiar a *identidade* de outra pessoa.

## Ordem de criação

1. ✅ Definir nicho e idade-alvo (lifestyle/viagem/fitness, 26–30).
2. ⏳ Receber a foto de 2019 → preencher a ficha canônica (+5 anos).
3. ⏳ Gerar a hero shot → definir como foto-âncora.
4. 🔁 A cada referência enviada, gerar o prompt aplicado à personagem.

## A "ponte" de +5 anos (2019 → hoje)

Da foto de 2019 para a versão atual (26–30), o envelhecimento é **sutil e natural**, não
dramático:

- Traços de identidade (formato de olhos, nariz, boca, proporções) **permanecem iguais** —
  é o que garante que continua sendo "ela".
- Mudam de forma leve: linhas de expressão iniciais (cantos dos olhos/testa), rosto um
  pouco menos "redondo de adolescente", pele um pouco mais madura, possível mudança de
  corte/cor de cabelo (decidimos juntos).
- Documentamos o "antes/depois" na própria ficha para manter coerência.
