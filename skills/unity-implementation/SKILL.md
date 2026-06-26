---
name: unity-implementation
description: Implementação e refatoração assertiva em NewScripts; audita owner local, aplica o corte completo, remove rails/compat errados, migra call sites ativos, sem fallback silencioso e sem parar em patch mínimo.
---

# Unity Implementation

## Objetivo da skill

Executar cortes de implementação/refatoração em `Assets/_ImmersiveGames/NewScripts` com owner correto.

Esta skill não é para patch conservador. Quando a solicitação pedir implementação, o resultado esperado é o corte completo dentro da fronteira pedida.

## Antes de editar

- Auditar somente os arquivos necessários para identificar o owner e os call sites ativos.
- Identificar o owner correto.
- Classificar o alvo: orchestration, stage, policy, command, fact, adapter, endpoint, snapshot, authoring data ou runtime state.
- Identificar se o erro é sintoma local ou fronteira arquitetural errada.
- Identificar o caminho antigo equivalente que precisa sair, ficar inacessível ou ser provado morto.
- Identificar risco SOLID.

Não transformar a auditoria em desculpa para não implementar quando o pedido é de implementação.

## Regra de implementação completa

Implementar o corte até o active path ficar canônico.

Obrigatório quando estiver dentro do escopo pedido:

- migrar todos os call sites ativos afetados;
- remover ou tornar inacessível o caminho antigo equivalente;
- remover compat/alias/wrapper transitório sem dependência real;
- remover fallback silencioso;
- remover reconstrução local de state/identity que pertence a outro owner;
- ajustar logs/facts para mostrar o owner correto;
- corrigir erros estáticos óbvios introduzidos pelo próprio patch;
- manter comentários só quando úteis, em português.

Não entregar apenas:

- novo helper enquanto o pipeline antigo continua executando;
- facade que chama o owner errado;
- patch de um único call site quando existem equivalentes ativos;
- relatório de risco sem alteração;
- TODO para remover compat que já pode ser removida no corte;
- bridge nova sem plano de remoção e sem motivo concreto.

## Tamanho do corte

- Preferir cortes pequenos, mas `pequeno` significa uma fronteira arquitetural coesa, não poucas linhas.
- Se a fronteira correta exige várias alterações coordenadas, faça todas no mesmo patch.
- Não reduzir a mudança ao mínimo quando isso preserva owner duplicado, rail paralelo ou compat errada.
- Não pedir autorização extra apenas porque muitos arquivos dentro da fronteira precisam mudar.

## Permitido

- Remover contratos, métodos, wrappers e aliases obsoletos em `NewScripts`.
- Quebrar compatibilidade de desenvolvimento quando o shape atual está errado.
- Renomear símbolos quando o nome antigo induz rail errado.
- Criar stage/policy/adapter/endpoint concreto quando isso substitui um owner errado.
- Alterar contratos públicos internos de `NewScripts` e migrar os consumers ativos no mesmo corte.

## Proibido

- Unity build/tests/playmode/smoke/batchmode.
- Fallback silencioso.
- Compat/alias oculto ou permanente.
- Service locator como atalho.
- Adapter decidindo lifecycle/policy.
- Registry como owner tardio.
- `partial` para esconder pipeline monolítico.
- Manager/coordinator/processor genérico para esconder ownership.
- String parsing/factory local para fabricar identidade.
- Comparar domínios de identidade diferentes.
- Command carregando Stage, Adapter, Boundary, Func, Action, state mutável compartilhado ou ScriptableObject autoral inteiro quando basta payload runtime resolvido.
- Fact/log/checkpoint executando side-effect ou mudando lifecycle.

## Quando parar sem editar

Parar apenas se:

- o prompt for audit-only;
- arquivos/contratos necessários estiverem ausentes;
- o pedido contradisser ADR/checkpoint aceito sem evidência de regressão;
- o owner permanecer ambíguo após auditoria local;
- o corte depender de serialização Unity que não pode ser editada com segurança em texto.

Ao parar, entregar bloqueio objetivo com arquivo/contrato/evidência e o menor próximo passo. Não parar por medo de diff grande.

## Base 2.0

Para Base 2.0:

- Pipelines decidem ordem/lifecycle/policy/handoff.
- Stages executam passos determinísticos.
- Policies classificam decisões, skips, blocks, stale/foreign e failures.
- Commands carregam payload runtime resolvido.
- Facts registram o ocorrido.
- Adapters executam side-effects comandados.
- Endpoints expõem/reagem a capability local.
- Registries são índices técnicos.
- QA chama caminho canônico.

Não preservar arquitetura errada por compatibilidade em `NewScripts`.

## Validação

- Não rodar Unity build, Unity tests, playmode, smoke ou batchmode.
- Pode rodar checagens estáticas locais não-Unity quando seguras.
- Não declarar PASS.
- Classificar como `implementado / pendente de smoke manual` quando não houver log do usuário.
- Sempre informar smoke/log manual necessário.

## Output compacto

1. Resumo do corte completo.
2. Arquivos criados/alterados/removidos.
3. Ownership corrigido/removido.
4. Caminho antigo removido/inacessível ou evidência de que já estava morto.
5. Contratos migrados/preservados.
6. Validação realizada e validação não realizada.
7. Smoke/log manual exigido.
8. Riscos restantes.
9. Impacto SOLID: SRP/OCP/LSP/ISP/DIP em uma linha cada.

Não colar diffs grandes salvo pedido explícito.
