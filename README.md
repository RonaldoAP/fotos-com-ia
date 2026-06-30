# Fotos com IA — Realismo de Celular no Nano Banana 2

Estudo e biblioteca de prompts para gerar **fotos ultra realistas de pessoas** no
**Google Nano Banana 2 (Gemini Image)**, com aparência de foto tirada por celular —
sem "cara de IA".

## Objetivo

Gerar imagens que pareçam **snapshots reais de celular**: luz disponível, pele com
textura natural, enquadramento casual e pequenas imperfeições. O oposto de uma foto
de estúdio "perfeita demais".

## Princípio central

O Nano Banana 2 **não é Midjourney/Stable Diffusion**. Ele não responde bem a listas
de palavras-chave soltas. Ele entende **descrição em linguagem natural** — você
descreve a foto como se contasse para um amigo. Por isso, nossos prompts são frases
narrativas, não "tag soup".

> ❌ `mulher, 25 anos, foto realista, 8k, pele perfeita, iluminação cinematográfica`
>
> ✅ `Foto casual tirada de celular de uma mulher de uns 25 anos na cozinha de casa
> num fim de tarde, luz fraca entrando pela janela, ela rindo de algo fora do quadro,
> a pele mostra poros e leve brilho natural, alguns fios de cabelo soltos no rosto.`

## A fórmula em 6 camadas

Todo prompt realista combina estas camadas (detalhes em [`guia/02-anatomia-do-prompt.md`](guia/02-anatomia-do-prompt.md)):

1. **Dispositivo + captura** — "foto de celular", "selfie de iPhone", "tirada de improviso"
2. **Pessoa + imperfeições** — poros, fios soltos, leve assimetria, pele real
3. **Luz disponível** — janela, sombra, dia nublado (nunca estúdio)
4. **Ambiente cotidiano** — cozinha, rua, ônibus, quarto bagunçado
5. **Estética de snapshot** — candid, torto, sem pose, recorte casual
6. **Marcadores anti-IA** — grão, leve desfoque de movimento, compressão de celular

## O que evitar (specs proibidas)

`plastic skin`, `over-smoothed`, `airbrushed`, `glossy`, `oily`, `cinematic studio
lighting`, `overexposed`, `extra fingers`, `deformed hands`, `face morphing`, `stiff
robotic motion`, `jitter`, `flicker`, `cartoon`, `3d render`, `low quality`.

Como neutralizar cada uma → [`guia/03-evitando-cara-de-ia.md`](guia/03-evitando-cara-de-ia.md).

## Estrutura do repositório

```
guia/
  01-principios.md          Como o Nano Banana 2 "pensa" e por que descrição natural ganha
  02-anatomia-do-prompt.md  A fórmula de 6 camadas com vocabulário pronto
  03-evitando-cara-de-ia.md Cada spec proibida e como combatê-la no prompt
prompts/
  templates.md              Modelos reutilizáveis (preencher os [colchetes])
  exemplos.md               Prompts prontos, completos, por cenário
```

## Fluxo de trabalho sugerido

1. Escolha um **template** em `prompts/templates.md`.
2. Preencha os `[colchetes]` com pessoa, ambiente e luz.
3. Gere no Nano Banana 2.
4. Se sair com "cara de IA", consulte `guia/03-evitando-cara-de-ia.md` e reforce a
   camada correspondente.
5. Salve o que funcionou em `prompts/exemplos.md` para reaproveitar.
