# HANDOFF — Projeto "Fotos com IA / Personagem Vic"

Documento de passagem do projeto. Leia isto **inteiro** antes de começar. Ele explica o que é o
projeto, quem é a personagem, as regras fixas, como os prompts são montados, o que já está pronto
e o que falta fazer.

---

## 1. O que é o projeto

Gerar **fotos ultra-realistas, com cara de foto de celular** de uma **influenciadora virtual**
chamada **Vic**, usando o **Google Nano Banana Pro / Nano Banana 2 (Gemini Image)** — acessado via
**Freepik** (tem MCP/ferramenta de geração). O objetivo é um feed coerente, como se fosse uma
pessoa real postando: praia, viagem, academia, casa, lifestyle.

**Princípio central:** o Nano Banana **lê linguagem natural**, não "tag soup" de palavras-chave.
Os prompts são frases naturais organizadas em campos (ver seção 5). E **não existe negative
prompt** — tudo que você quer (ou não quer) tem que ser **afirmado no texto** (ex.: em vez de
"no jewelry" como negative, escrevemos "sem joias" na prosa).

O que a gente foge (a "cara de IA"): pele plástica, super suavizada, aerografada, brilho
oleoso, luz de estúdio cinematográfica, superexposto, dedos a mais, mãos deformadas, face
morphing, render 3D, cartoon. Como neutralizar cada um: `guia/03-evitando-cara-de-ia.md`.

---

## 2. A personagem Vic (identidade)

Vic é a personagem principal. **A fidelidade do rosto e do corpo vem das IMAGENS de referência
dela, não do texto.** O texto só reforça e trava regras. Ficha completa em
`personagem/ficha-canonica.md` e o bloco curto pra colar em `personagem/mini-ficha.md`.

Resumo do "tipo" (arquétipo — o detalhe fino vem da referência visual):
- Mulher ~26–30 anos, **cabelo loiro com ombré** (raiz mais escura, pontas claras), comprido e
  liso; **olhos verde-acinzentados**; **pele clara com sardas leves**.
- **Biotipo atlético-curvilíneo (ampulheta)**: cintura fina, quadril largo, glúteos volumosos e
  torneados, pernas definidas, barriga sequinha. Altura ~1,70 m.

### ⚠️ Regras fixas da personagem (NUNCA quebrar)
- **Sem tatuagens, sem piercings, sem joias/bijuterias** — em toda foto. (Óculos de grau/de sol e
  fones contam como peça funcional, podem entrar.)
- **O prompt de cena NÃO descreve traços físicos** (cor de cabelo, cor de pele, rosto, corpo) —
  isso a referência puxa. **Exceção:** o **penteado/estado do cabelo** (solto, preso, molhado, ao
  vento) **deve** ser dito por cena. Detalhes: `personagem/mini-ficha.md`.
- **Mãos com anatomia correta, cinco dedos** (afirmar sempre ajuda).

### Consistência (rosto + corpo)
Como manter a Vic idêntica entre fotos está em `guia/05-consistencia-banana-pro.md` e
`personagem/00-consistencia.md`. Pontos-chave:
- **Kit de referência** (rosto multi-ângulo + corpo) + uma **foto-âncora (hero shot)** que se
  reusa sempre. **Nunca encadear** (gerar a partir de geração anterior) — o rosto deriva.
- **Corpo curvilíneo** costuma precisar de **dual-reference**: além da referência de rosto,
  anexar uma referência de **corpo curvy**.
- O **set de treino** tem que **representar o look-alvo** (ombré solto + corpo curvy dominando),
  senão o modelo puxa pra média enviesada. Cobertura de ângulos importa (senão ela "inventa"
  ângulos não vistos). Prompts prontos do kit em `personagem/kit-referencia-prompts.md`,
  `personagem/set-retreino-vic.md` e `personagem/set-expansao-angulos.md`.

---

## 3. Regras de conteúdo (o que fazemos e o que NÃO fazemos)

O projeto é de fotos **filtro-safe, sem sexualização**. Muitas referências que chegam (o usuário
manda prints de fotos de outras pessoas como inspiração) vêm em enquadramento/roupa que **não**
usamos. A regra de conversão:

**NÃO fazemos:**
- Enquadramento feito pra destacar corpo/bumbum/decote (ex.: de costas com o bumbum empinado,
  "glúteo à mostra", pernas abertas pra câmera, foco no busto).
- Lingerie / peças íntimas / transparências / biquíni fio-dental / "cavado na virilha".
- Replicar a **identidade facial de uma pessoa real** de uma foto de referência (usamos só a
  cena/pose/roupa; o rosto é sempre da Vic).

**Fazemos (reframe):** aproveitamos a **cena, o cenário e o look-base** da referência e
reancoramos na Vic com **enquadramento normal, de frente, filtro-safe**. Biquíni/roupa de treino
são ok quando descritos como **atividade/cena** normal (praia, academia), não como destaque de
corpo. Guia de roupas/filtros: `guia/04-roupas-e-filtros.md`.

> Na prática: quando a referência é sexualizada, a gente **recusa aquele recorte** e devolve uma
> versão tratável (mesmo lugar/vibe, pose relaxada, rosto visível). Já tem dezenas de exemplos
> desse "reframe" na biblioteca `prompts/externos.md`.

---

## 4. Estrutura do repositório

```
README.md                         Visão geral + fórmula de 6 camadas + índice
HANDOFF.md                        (este arquivo)

guia/
  01-principios.md                Como o Nano Banana "pensa" (linguagem natural)
  02-anatomia-do-prompt.md        Fórmula de 6 camadas + vocabulário
  03-evitando-cara-de-ia.md       Cada "spec proibida" e como combater
  04-roupas-e-filtros.md          Praia/biquíni sem disparar filtro (sem sexualização)
  05-consistencia-banana-pro.md   Estratégia de consistência de rosto/corpo
  06-detalhes-de-realismo.md      Âncoras de realismo + aviso da "acne por excesso"

personagem/
  00-consistencia.md              3 pilares de consistência + exclusões fixas
  ficha-canonica.md               Ficha de identidade da Vic (campo do criador de personagem)
  mini-ficha.md                   Bloco curto p/ colar + regra do celular padrão + penteado por cena
  kit-referencia-prompts.md       Prompts 3:4 estilo RG (turnaround) p/ gerar o kit de identidade
  set-retreino-vic.md             Set de retreino a partir da âncora ombré
  set-expansao-angulos.md         X1–X10 p/ cobrir ângulos/expressões + estratégia 9 slots (Freepik)

cenarios/
  quarto-vic.md                   CENÁRIO FIXO do quarto da Vic (ver seção 7) + kit Q1–Q6

prompts/
  templates.md                    Molde principal (formato de 5 campos) + templates antigos
  exemplos.md                     Biblioteca de cenas E1–E6 (didáticos) + C1–C38 (cenários da Vic)
  externos.md                     Prompts recebidos de fora, convertidos: EXT1–EXT57
```

---

## 5. ⭐ Formato de prompt (5 campos) — o PADRÃO atual

Todo prompt novo segue esta ordem, **rótulos em MAIÚSCULA e uma linha em branco entre cada um**.
Cada campo é uma **frase natural** (não lista de tags). Molde e exemplos completos em
`prompts/templates.md` (seção "Estrutura padrão").

```
PERSONAGEM: a mesma pessoa das imagens de referência (Vic).

AMBIENTE: [local — ou [AQUI] se for o quarto padrão]; [luz do ambiente].

ROUPA: [peça de cima] + [peça de baixo] + [calçado].

DETALHES DA PESSOA: [penteado]; [expressão/olhar]; pele com textura natural e saudável — poros e
uma sardinha ou outra, leve vermelhidão; sem acne, sem excesso de imperfeição; sem joias, sem
piercing, sem tatuagem.

POSE: [pose e enquadramento]; foto de celular meio torta, grão suave [+ iPhone 15 Pro Max titânio
preto, capinha preta, se o celular aparecer]; foto realista, sem retoque, sem cara de IA.
```

- Todo prompt tem versão **PT e EN** (o EN costuma render um pouco melhor no Nano Banana).
- Mapeamento dos campos: local+luz → AMBIENTE; roupa/calçado/acessório → ROUPA; cabelo, expressão,
  bloco de pele/realismo e as exclusões (sem joia/piercing/tatuagem) → DETALHES DA PESSOA;
  pose/enquadramento/assinatura de celular → POSE.

---

## 6. Convenções especiais (decisões já tomadas — mantenha)

1. **Celular padrão:** sempre que um celular **aparece em quadro** (mirror selfie, celular
   apontado pro espelho), ele é um **iPhone 15 Pro Max titânio preto, capinha preta lisa**. Em
   selfie de braço esticado o celular fica atrás da câmera — não precisa citar. Regra em
   `personagem/mini-ficha.md`.
2. **Modo natural:** os prompts são escritos como descrição solta de foto de celular real, com
   imperfeições costuradas na frase — não bloco técnico "câmera: … luz: …".
3. **Realismo (2–4 âncoras por foto, não todas):** poros, sardas, fio solto, grão, enquadramento
   torto, motion blur, flash no espelho etc. Lista em `guia/06-detalhes-de-realismo.md`.
4. **⚠️ Não exagerar imperfeição de pele:** empilhar muita imperfeição faz o modelo gerar
   **acne/irritação**. Sempre usar o "bloco de pele seguro": *pele com textura natural e saudável —
   poros e uma sardinha ou outra, leve vermelhidão; sem acne, sem excesso de imperfeição.* (Isso já
   está em todos os prompts.)
5. **⭐ Bloco "cara de celular" (fixo, no fim da POSE):** lente grande-angular de celular, quase tudo
   em foco (**sem bokeh** de câmera profissional), HDR de celular, nitidez digital exagerada, leve
   JPEG e balanço de branco automático. Texto exato PT/EN em `guia/06-detalhes-de-realismo.md`. Já
   aplicado em todos os prompts (exemplos, externos e os dois JSON).
6. **⭐ Modo réplica (pedido do dono):** quando chega uma foto de referência, o prompt reproduz a foto
   **exatamente igual** — luz, textura, cor, enquadramento, posição no quadro, câmera, pose, expressão,
   cenário e objetos. **Nada é "melhorado" por conta própria.** As únicas mudanças permitidas (e
   sempre avisadas ao dono) são: (1) joia/piercing/tatuagem saem; (2) rosto/cor de cabelo/corpo vêm da
   referência da Vic; (3) lingerie/transparência/peça íntima → peça equivalente mais próxima (mesmo
   corte, cor, caimento); (4) recorte feito pra destacar corpo → mesma pose/luz, só o corte muda o
   mínimo. Checklist de precisão em `prompts/templates.md` (seção "Modo réplica").

---

## 7. ⭐ Cenário fixo: o quarto da Vic

Para as **fotos de quarto** a gente definiu um **quarto padrão** (como a personagem, só que de
ambiente). Documento: `cenarios/quarto-vic.md`. Pontos:

- O quarto tem 3 paredes que aparecem (cabeceira preta + cama branca; janela com cortina + mesa;
  porta/armário) e a 4ª parede é o **espelho** (só aparece em mirror selfie). No teto, uma **fita
  de LED** cuja **cor é escolhida no prompt** (`[COR DA LED]`) — ex.: roxo.
- **CONVENÇÃO IMPORTANTE:** nas fotos de quarto **o prompt NÃO descreve o quarto**. Ele vem da
  **imagem de referência do quarto**. O prompt só marca **`AMBIENTE: [AQUI]`** (onde a pessoa
  seleciona a referência do quarto) + a cor da LED. Vários prompts já usam isso (ex.: EXT25–EXT30,
  EXT52–EXT54).
- Há um **kit Q1–Q6** no documento pra **gerar as imagens de referência do quarto** (6 ângulos,
  incluindo a parede do espelho). **Isso ainda NÃO foi gerado — é uma pendência (ver seção 9).**

---

## 8. Estado atual (o que já está pronto)

- **Guias completos** (`guia/01`…`06`) e **docs de personagem** (`personagem/*`).
- **Biblioteca de cenas** `prompts/exemplos.md`: **E1–E6** (exemplos didáticos, pessoas genéricas)
  + **C1–C38** (cenários da Vic — praia/Rio, aquário, carro, eventos, casa, academia). **Todos já
  convertidos pro formato de 5 campos.**
- **Biblioteca de externos** `prompts/externos.md`: **EXT1–EXT57** (prompts que chegaram de fora,
  convertidos/reframados pra Vic). **Todos no formato de 5 campos.**
- **Template principal** (5 campos) em `prompts/templates.md`.
- **Padronização do celular** aplicada em todas as mirror selfies.
- **Cenário do quarto** documentado (`cenarios/quarto-vic.md`) com a convenção `AMBIENTE: [AQUI]`.

> Fluxo típico do dia a dia até aqui: o dono manda um print de referência → a gente **reframa** pra
> Vic (filtro-safe, sem joia/tatuagem) → escreve o prompt em 5 campos (PT+EN) → **salva** em
> `prompts/externos.md` como EXTn → **commita e dá push**.

---

## 9. Pendências / próximos passos

1. **Gerar o kit de referência do quarto (Q1–Q6)** via Freepik/Nano Banana Pro
   (`cenarios/quarto-vic.md`). Decisão em aberto com o dono: **(A)** subir a foto real do quarto
   dele (LED roxa) pra ancorar a geração → quarto **idêntico**; ou **(B)** gerar só pelo texto →
   mesmo estilo, não idêntico. **Recomendado: (A).** Depois de gerar, guardar as melhores como
   âncoras do ambiente (idealmente na **Library do Freepik** como "location").
2. **Gerar/validar o kit de referência da Vic** (rosto multi-ângulo + corpo curvy) se ainda não
   estiver finalizado na ferramenta — prompts em `personagem/kit-referencia-prompts.md`,
   `set-retreino-vic.md`, `set-expansao-angulos.md`.
3. **Continuar a biblioteca**: novas referências chegam via print; reframar + escrever em 5 campos
   + salvar em `externos.md` (próximo id = **EXT58**) ou em `exemplos.md` (próximo = **C39**) e
   commitar.
4. (Opcional) **EXT12** tem "Bico de biquíni preto" (provável typo de "Top de biquíni") — mantido
   literal na conversão; corrigir se quiser. **C38** não tinha "sem cara de IA" no original —
   pode padronizar.

---

## 10. Ferramentas e como gerar (Freepik / Nano Banana Pro)

- A geração é no **Nano Banana Pro (Gemini 3 Pro Image)** dentro do **Freepik**. Há ferramentas
  MCP do Freepik (ex.: `images_generate`, `images_models_list`, `creations_show`, `library_*`).
  O conector **cai e reconecta** de vez em quando; se as ferramentas `mcp__Freepik__*` não
  aparecerem, é porque o servidor está desconectado no momento — reativar o conector.
- **Como uma foto nova é montada na ferramenta:** anexar as **referências da Vic** (rosto/corpo)
  [+ a **referência do quarto** se for foto de quarto] + colar o **prompt de 5 campos** (a
  `mini-ficha` pode ir junto pra reforçar) → gerar 3–4 variações → escolher a mais fiel →
  promover a âncora. **Nunca encadear.**
- A **Library do Freepik** guarda assets reutilizáveis (character/location/style) — vale cadastrar
  a Vic como *character* e o quarto como *location* pra reusar fácil.

---

## 11. Git / entrega

- Repositório: **RonaldoAP/fotos-com-ia** (mesmo GitHub).
- Branch de trabalho atual: **`claude/cool-thompson-c56g2m`**. Todo o material acima já está
  commitado e no push desse branch. (Combinar com o dono se o trabalho novo continua nesse branch
  ou sai um novo a partir da default.)
- Padrão de commit usado: `git add -A && git commit -m "..." && git push -u origin <branch>`.

---

## 12. TL;DR pra quem vai executar

1. Leia `README.md`, depois `personagem/mini-ficha.md`, `cenarios/quarto-vic.md` e
   `prompts/templates.md` (seção "Estrutura padrão").
2. Regras que não se quebram: **Vic sem joia/piercing/tatuagem**; **nada de sexualização/enquadramento
   de corpo**; **rosto/corpo vêm da referência**, não do texto; **celular = iPhone 15 Pro Max
   titânio preto**.
3. Referência nova → **reframa** filtro-safe → escreve em **5 campos (PT+EN)** → salva em
   `externos.md`/`exemplos.md` → **commit + push**.
4. Pendência principal: **gerar as referências do quarto (Q1–Q6)** e fechar o **kit da Vic**.
