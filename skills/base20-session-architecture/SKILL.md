---
name: base20-session-architecture
description: Skill compacta para Base 2.0 Session Architecture Convergence / Pipeline Runtime Decomposition: auditar e planejar decomposição de pipelines, stages, policies, commands, facts, adapters, identities e ownership.
---

# Base 2.0 — Session Architecture

## Uso

Usar para Base 2.0, Session architecture, pipeline decomposition, `SessionOperationalPipeline`, `SessionActivityPipeline`, `ActivityEntryPipeline`, seams, bridges, false generic e ownership estrutural.

## Premissa

Base 1.1 é baseline funcional. Base 1.2 é evidência/aprendizado. Base 2.0 pode substituir shape ruim quando houver falha arquitetural clara.

`NewScripts` é desenvolvimento. Não preservar arquitetura intermediária errada por compatibilidade.

## Alvo

Decompor pipelines monolíticos em:

- orchestration;
- Pipeline Stage;
- Pipeline Policy;
- Pipeline Command;
- Pipeline Fact;
- Pipeline Handoff;
- Pipeline Adapter;
- Pipeline Identity;
- Pipeline Snapshot;
- endpoint/source/resolver boundaries.

## Regras

- Pipeline decide ordem/lifecycle/policy/handoff.
- Stage executa passo determinístico.
- Policy classifica decisão/skip/block/failure.
- Command carrega payload runtime resolvido.
- Fact registra resultado, sem side-effect.
- Adapter executa side-effect.
- Registry indexa; não decide lifecycle.
- QA chama comando/stage canônico.
- Remover compat errada se não houver produção dependente.

## Identidades separadas

Não misturar:

- `PipelineIdentity`
- `RouteIdentity`
- `SessionActivityIdentity`
- `ActorId`
- `ActorInstanceRuntimeId`
- `PlayerActorId`
- `PlayerSlotId`
- `ActivityParticipationContext`

## Procurar

- god pipeline;
- service locator no pipeline;
- polling entre pipelines;
- pipeline conhecendo stage interno de outro pipeline;
- side-effect em fact/log/checkpoint;
- command com asset autoral inteiro;
- registry usado após release/teardown;
- policy duplicada;
- falso genérico;
- compat seam;
- branch player/nonplayer onde capability deveria variar.

## Output para auditoria

1. Resumo.
2. Top achados.
3. Matriz curta:
   - arquivo/método;
   - problema;
   - owner correto;
   - severidade;
   - ação.
4. Primeiro corte seguro.
5. O que não mexer agora.

## Output para implementação

1. Resumo.
2. Arquivos alterados.
3. Ownership corrigido.
4. Antes/depois.
5. Validação manual.
6. Riscos.
7. Impacto SOLID.
