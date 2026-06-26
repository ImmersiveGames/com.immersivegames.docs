# Codex Primary Runtime — Compact Skills v3

Pacote compacto para reduzir gasto de tokens.

## Premissa

`Assets/_ImmersiveGames/NewScripts` é desenvolvimento, não produção. Não preservar arquitetura errada por compatibilidade sem dependência real.

## Seleção padrão

- Sempre: `unity-repository-general`.
- Auditoria/revisão/diagnóstico: + `unity-architecture-audit`.
- Implementação/refatoração/criação/remoção: + `unity-implementation`.
- Base 2.0, Session, pipelines, seams, bridges, ownership: + `base20-session-architecture`.

## Estilo de resposta

- Relatórios curtos.
- Evidência por arquivo/método, sem longas transcrições.
- Sem repetir histórico do projeto.
- Máximo foco em owner, risco e próxima ação.

## Skills

- `unity-repository-general`: regras gerais, SOLID, ownership, identidade, validação.
- `unity-architecture-audit`: auditoria objetiva sem alteração de código.
- `unity-implementation`: implementação escopada, com resumo e validação manual.
- `base20-session-architecture`: decomposição Base 2.0 de pipelines/session architecture.


## Immersive Framework package skills

Use these for the new package-based Immersive Framework work. They intentionally separate the new framework from the old Base 2.0/NewScripts workflow.

- `immersive-framework-package-general`: general rules for package boundaries, UPM/Git, frozen technical packages and validation.
- `immersive-framework-architecture-audit`: audit package/module ownership, public naming and Inspector UX without editing files.
- `immersive-framework-package-implementation`: implement cuts in packages while preserving runtime/Unity/Editor assembly boundaries.
- `immersive-framework-core-architecture`: design the future `com.immersive.framework` package and its internal modules without copying Base 2.0.
