# 01 — Princípios: como o Nano Banana 2 "pensa"

## 1. Linguagem natural vence keyword soup

O Nano Banana 2 é baseado em Gemini. Ele foi treinado para **entender descrições**,
não para casar tags. Escreva frases completas, com sujeito, ação e contexto. Quanto
mais a sua frase parecer a legenda honesta de uma foto real, mais realista o resultado.

- Pense: "como eu descreveria essa foto pra alguém que não está vendo?"
- Use conectores ("enquanto", "porque", "com", "enquanto ela...").
- Evite números mágicos de qualidade (`8k`, `4k`, `ultra HD`) — eles puxam para o look
  artificial de banco de imagens.

## 2. Realismo vem da imperfeição, não da perfeição

A foto "perfeita" é o que denuncia a IA. O cérebro humano lê pele lisa demais, luz
equilibrada demais e enquadramento centrado demais como "errado". Realismo é:

- Pele com **poros, textura, leve oleosidade na zona T, fios soltos**.
- Luz **desigual** (um lado do rosto mais escuro, sombra dura da janela).
- Enquadramento **descuidado** (cortando o topo da cabeça, torto, descentralizado).
- **Ruído/grão** de sensor de celular em luz baixa.

## 3. Especifique o aparelho e o contexto de captura

Dizer "foto de celular" muda o resultado. Vá além:

- "selfie de braço estendido com a câmera frontal"
- "foto tirada de improviso por um amigo"
- "print de vídeo chamada" / "foto de status de WhatsApp"
- "foto noturna com flash do celular"

Cada um carrega uma assinatura visual (distorção de lente frontal, flash duro,
compressão) que o modelo reproduz e que grita "celular real".

## 4. Descreva a luz que existe, não a luz que você quer

Fotos reais de celular usam **luz disponível**, raramente lisonjeira:

- Luz de janela lateral num dia nublado.
- Lâmpada fluorescente de cozinha à noite.
- Sol forte do meio-dia criando sombra dura sob o nariz.
- Penumbra do quarto iluminada só pela tela do celular.

Evite qualquer coisa que soe a set de cinema ("rim light", "softbox", "golden hour
cinematográfica"). Isso reintroduz a estética de estúdio.

## 5. Contexto cotidiano e banal

Coloque a pessoa num lugar comum e imperfeito: cozinha com louça na pia, ponto de
ônibus, banheiro com espelho embaçado, sofá com roupa jogada. O ambiente "feio e real"
ancora a imagem na realidade.

## 6. Itere por camada, não reescrevendo tudo

Se a imagem saiu plástica, não jogue o prompt fora. Identifique **qual camada falhou**
(luz? pele? enquadramento?) e reforce só ela. Veja `03-evitando-cara-de-ia.md`.

## 7. Sobre "negative prompts"

O Nano Banana 2 não tem um campo de negative prompt como o Stable Diffusion. Você
**afirma o oposto** dentro do prompt: em vez de "não plastic skin", escreva "pele com
poros visíveis e textura natural". Combater pela afirmação positiva funciona melhor do
que listar o que não quer.
