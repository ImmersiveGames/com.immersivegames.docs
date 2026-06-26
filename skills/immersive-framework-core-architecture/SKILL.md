---
name: immersive-framework-core-architecture
description: Arquitetura do futuro com.immersive.framework: framework core como package, módulos internos, settings, bootstrap, diagnostics, validators e redesign sem copiar Base 2.0.
---

# Immersive Framework Core Architecture

## Uso

Aplicar para tarefas sobre:

- `com.immersive.framework`;
- Framework Core;
- módulos internos;
- settings;
- bootstrap;
- validators;
- diagnostics;
- Strict/Release policy;
- Scene Lifecycle/Scene Loading;
- Game Flow;
- futuras Session/Route/Activity/Actor abstractions.

## Premissa

`com.immersive.framework` é o produto real que consome os packages técnicos:

- `com.immersive.foundation`;
- `com.immersive.logging`;
- `com.immersive.pooling`.

Ele não deve reimplementar esses packages.

## Package vs module

- `com.immersive.framework` deve começar como um package.
- Módulos do framework começam como módulos internos/folders/asmdefs, não packages separados.
- Só virar package separado depois se houver reuse/versionamento independente real.

## Regras

- Começar mínimo.
- Não criar lifecycle runtime no skeleton inicial sem discussão.
- Não copiar `SessionOperational`, `SessionActivity`, `ActivityEntryPipeline` ou Base 2.0 diretamente.
- Usar Base 2.0 como referência de problemas/ADRs, não como base direta.
- Revisar nomes públicos e Inspector UX antes de criar authoring APIs.
- Settings, Bootstrap, Diagnostics, Validation e Module loading pertencem ao Framework Core.
- Strict/Release policy e degraded mode pertencem ao Framework Core/Diagnostics, não ao Foundation/Logging.
- SceneComposition antigo deve ser redesenhado como Scene Lifecycle/Scene Loading, com linguagem pública melhor.

## Red flags

- criar `Manager`/`Coordinator` genérico como raiz do framework;
- service locator como bootstrap;
- global singleton obrigatório;
- config global escondida;
- lifecycle de jogo no setup;
- repetir nomes antigos como `RuntimeMode`, `SceneComposition`, `Macro`, `Local` sem revisão;
- expor pipeline/stage/command/fact como primeira camada de authoring;
- misturar Session/Route/Activity antes de definir GameFlow público.

## Output para auditoria/plano

1. Conceito público proposto.
2. Owner correto: Core, Settings, Bootstrap, Diagnostics, Validator, Module, Authoring ou Editor.
3. O que consome dos packages técnicos.
4. O que não criar agora.
5. Skeleton mínimo recomendado.
6. Riscos de repetir Base 2.0.
