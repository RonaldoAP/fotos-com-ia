# 03 — Evitando "cara de IA": cada spec proibida e seu antídoto

O Nano Banana 2 não tem campo de *negative prompt*. A estratégia é **afirmar o oposto**
dentro do prompt. Abaixo, cada spec que queremos evitar e a frase positiva que a combate.

| Spec proibida | Por que aparece | Antídoto (afirme isto no prompt) |
|---|---|---|
| **plastic skin** | modelo "embeleza" a pele | "pele com poros visíveis, textura real, pequenas imperfeições" |
| **over-smoothed** | suavização agressiva | "textura de pele detalhada, sem suavização, fios de cabelo individuais" |
| **airbrushed** | look de retoque/revista | "pele sem retoque, vermelhidão e manchas naturais, foto crua" |
| **glossy** | brilho exagerado | "acabamento fosco, sem brilho artificial" |
| **oily** (excesso) | brilho de óleo demais | "leve oleosidade natural só na zona T, resto fosco" |
| **cinematic studio lighting** | viés de set de cinema | "luz disponível do ambiente, luz de janela/lâmpada comum, sem iluminação de estúdio" |
| **overexposed** | estouro de luz | "exposição equilibrada, sombras preservadas, sem estouro de luz" |
| **extra fingers** | erro de mãos | "mãos com exatamente cinco dedos, anatomia correta das mãos" + esconder/ocupar as mãos |
| **deformed hands** | erro de mãos | "mãos naturais e bem formadas" + posicionar mãos fora de quadro ou segurando objeto |
| **face morphing** | rosto instável | "rosto único, simétrico e consistente, traços bem definidos" |
| **stiff robotic motion** | pose travada | "postura relaxada e natural, movimento espontâneo" |
| **jitter / flicker** | (vídeo) instabilidade | "imagem estável, sem tremor; leve desfoque de movimento natural apenas" |
| **cartoon** | estilização | "fotografia realista, não ilustração, não desenho" |
| **3d render** | look de CGI | "fotografia real, não renderização 3D, não CGI" |
| **low quality** | artefatos ruins | "foto nítida de celular, boa exposição" (mas mantendo grão natural) |

## Regras de ouro

1. **Mãos:** o ponto mais frágil. Sempre que possível, dê uma função às mãos (segurando
   xícara, celular, apoiando o rosto) ou deixe-as fora do quadro. Se precisar mostrá-las,
   afirme "cinco dedos, anatomia correta".

2. **Pele:** repita textura em pelo menos duas formas ("poros visíveis" + "sem
   suavização"). É a defesa nº1 contra o look plástico.

3. **Luz:** se aparecer "estúdio/cinematográfico", troque explicitamente por uma fonte
   doméstica nomeada ("luz da lâmpada da sala", "luz da janela").

4. **Não exagere o ruído:** pedir "muito grão/baixa qualidade" pode virar artefato. Peça
   "leve" / "sutil".

5. **Teste isolando camadas:** se a imagem está plástica, reforce só a Camada 2 (pele)
   antes de mexer no resto.

## Mini-bloco anti-IA pronto (cole no fim do prompt)

> Pele com poros visíveis e textura real, sem suavização nem retoque; acabamento fosco;
> luz disponível do ambiente, sem iluminação de estúdio; exposição equilibrada; mãos com
> anatomia correta; fotografia real de celular, não ilustração, não render 3D; leve grão
> natural.

### EN

> Visible skin pores and real skin texture, no smoothing or retouching; matte finish;
> available ambient light, no studio lighting; balanced exposure; anatomically correct
> hands; real smartphone photograph, not an illustration, not a 3D render; subtle natural
> grain.

---

## Booster de realismo (PADRÃO — em todo prompt de cenário)

Bloco fixo que vai no fim de **todo** prompt da Biblioteca de cenários. Ataca os 4 "tells"
mais comuns no resultado gerado: rosto embelezado, luz lisonjeira incoerente, pele lisa e
foto limpa demais.

> **PT:** Mantenha exatamente os traços do rosto da referência, sem embelezar nem padronizar.
> A luz do ambiente incide de forma realista sobre a pele, com áreas em sombra, sem luz
> lisonjeira separada. Textura de pele real com poros e pequenas imperfeições, sem suavização
> nem brilho de IA. Grão e ruído sutis de foto de celular. Mãos com dedos de proporção
> natural, anatomia correta.

> **EN:** Keep the exact facial features from the reference, no beautifying or standardizing.
> Ambient light falls realistically on the skin with shadowed areas, no separate flattering
> light. Real skin texture with pores and small imperfections, no smoothing or AI glow.
> Subtle phone-photo grain and noise. Hands with natural finger proportions, correct anatomy.

**Ordem de impacto:** rosto (não embelezar) e luz (coerência) resolvem ~80% da cara de IA;
pele e grão dão o acabamento.
