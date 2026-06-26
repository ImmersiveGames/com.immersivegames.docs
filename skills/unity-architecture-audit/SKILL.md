---
name: unity-architecture-audit
description: Auditoria objetiva sem alteração de código para encontrar ownership errado, SOLID violations, seams, bridges, falso genérico, identidade misturada, compat desnecessária e riscos arquiteturais.
---

# Unity Architecture Audit

## Modo

- Não modificar arquivos.
- Não renomear/remover.
- Não propor implementação antes dos achados.
- Evidência por arquivo/classe/método.
- Relatório curto e acionável.

## Premissa

`NewScripts` é desenvolvimento. Compatibilidade não é padrão. Se o shape está errado e não há produção dependente, recomendar remoção/substituição é válido.

## Procurar

- owner errado ou duplicado;
- violação SOLID;
- seam/bridge/trilho transitório ativo;
- falso genérico;
- concrete dependency escondida;
- registry como source tardio de lifecycle;
- side-effect em log/fact/snapshot/checkpoint;
- service locator em orchestration;
- polling em orchestration;
- identity domains misturados;
- fallback silencioso;
- compat/alias sem necessidade;
- branches por concreto onde capability/endpoint/source deveria variar.

## Red flags rápidas

- método grande `ExecuteXxx`, `HandleXxx`, `OrchestrateXxx`;
- command carregando asset autoral inteiro;
- método retorna sucesso antes da execução finalizar;
- pipeline conhece stage interno de outro pipeline;
- serialização manual em orchestrator;
- `partial` só para esconder arquivo grande.

## Severidade

- `Blocker`: quebra fluxo ou impede implementação segura.
- `High`: ownership errado com risco forte de regressão.
- `Medium`: dívida estrutural contida.
- `Low`: limpeza/nome/documentação.

## Output compacto

1. Resumo executivo.
2. Top achados, ordenados por severidade.
3. Matriz curta:
   - arquivo/método;
   - problema;
   - owner correto;
   - severidade;
   - ação recomendada.
4. O que não mexer agora.
5. Próxima ação sugerida.

Não colar trechos longos de código, salvo pedido explícito.
