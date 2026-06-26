---
name: immersive-framework-package-general
description: Regras gerais para trabalhar no Immersive Framework em formato de Unity packages: boundaries, package roots, dependências, Git/UPM, separação entre packages técnicos e framework core.
---

# Immersive Framework Package General

## Escopo ativo

- Produto ativo: `Immersive Framework` em formato de Unity packages.
- Raízes válidas de package:
  - `Packages/com.immersive.foundation`
  - `Packages/com.immersive.logging`
  - `Packages/com.immersive.pooling`
  - futuro `Packages/com.immersive.framework`
  - repo standalone com `package.json` na raiz.
- `Assets/_ImmersiveGames/NewScripts` é referência antiga/Base 2.0, não área ativa do framework novo, salvo pedido explícito.
- Não copiar `ProjectSettings`, assets, configs ou runtime antigo para o novo framework sem migração controlada explícita.

## Packages técnicos congelados

- `com.immersive.foundation`: `Validation`, `Events`, `Fsm`.
- `com.immersive.logging`: logging primitives + `UnityConsoleLogSink`.
- `com.immersive.pooling`: `IPoolable`, `PoolableBehaviour`, `GameObjectPool`, `PoolReturnHandle`.

Não modificar package congelado salvo pedido explícito.

## Regras de package

- Package é unidade de distribuição/versionamento.
- Módulo de framework é unidade arquitetural interna, normalmente dentro de `com.immersive.framework`.
- Novo package só quando for genérico, reutilizável fora do framework e tiver ciclo próprio de versão.
- Framework-specific behavior entra em `com.immersive.framework`.
- Packages técnicos não devem conhecer `Session`, `Route`, `Activity`, `Actor`, `Input`, `Camera`, `Save` ou lifecycle do framework.
- Runtime puro deve usar `noEngineReferences: true`.
- Unity adapters devem ficar em assembly separado.
- Editor assemblies devem ser Editor-only.
- Não usar paths absolutos locais em código/setup canônico.
- Git dependencies devem ser tagueadas quando o corte for de instalação/release.

## Comunicação

- Responder em português.
- Código, classes, métodos, namespaces, assets e arquivos em inglês.
- Relatórios curtos, estruturados e baseados em evidência.
- Não repetir histórico do Base 2.0 salvo necessidade.

## Validação

- Não rodar Unity build, tests, playmode, smoke ou batchmode.
- Não declarar PASS sem confirmação do usuário de compile/import/smoke.
- Sempre listar validação manual necessária.
