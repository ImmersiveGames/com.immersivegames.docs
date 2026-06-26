---
name: unity-repository-general
description: Regras gerais compactas para qualquer tarefa no repositório Unity: desenvolvimento em NewScripts, SOLID, ownership, identidade, seleção de skills, validação segura e respostas objetivas.
---

# Unity Repository General

## Escopo

- Área canônica: `Assets/_ImmersiveGames/NewScripts`.
- `NewScripts` é desenvolvimento, não produção.
- Não preservar arquitetura errada por compatibilidade sem dependência real.
- Legacy `Scripts` é histórico, salvo pedido explícito.

## Seleção de skills

Se o chat não nomear skills:

- sempre usar `unity-repository-general`;
- auditoria/revisão/diagnóstico: + `unity-architecture-audit`;
- implementação/refatoração/criação/remoção: + `unity-implementation`;
- Base 2.0, Session, pipelines, seams, bridges, ownership: + `base20-session-architecture`.

Na dúvida: auditar antes de implementar.

## Regras inegociáveis

- Responder em português.
- Código, classes, métodos, namespaces, assets e arquivos em inglês.
- Comentários em português só quando úteis.
- SOLID é obrigatório.
- Corrigir no owner certo; não remendar módulo alheio.
- Config obrigatória: fail-fast.
- Sem fallback silencioso.
- Sem rails de compatibilidade ocultos.
- Sem service locator como atalho para dependência obrigatória.
- Sem parse/string para fabricar identidade.
- Não comparar domínios de identidade diferentes.
- Não inferir arquivos, contratos ou runtime ocultos.

## Ownership

- Orchestrator: ordem/lifecycle/handoff.
- Policy: classifica decisão/skip/block/failure.
- Command: payload runtime resolvido.
- Fact/Snapshot: registra estado/resultado; não executa side-effect.
- Adapter: executa side-effect.
- Endpoint: expõe capacidade local.
- Registry: índice técnico, não lifecycle owner.
- QA/debug: chama caminho canônico.

## SOLID mínimo

- SRP: uma razão clara para mudar.
- OCP: preferir policy/stage/adapter/endpoint/source a branches crescentes.
- LSP: contrato genérico não pode depender de concreto escondido.
- ISP: interfaces estreitas.
- DIP: alto nível depende de contratos, não infraestrutura concreta.

## Validação

- Não rodar Unity build, tests, playmode, smoke ou batchmode.
- Static/compilation checks só se seguros e relevantes.
- Não declarar PASS sem evidência de repositório ou check executado.
- Sempre listar validação manual.

## Resposta compacta

Evitar histórico. Usar:

- resumo;
- arquivos/classes afetados;
- achados ou mudanças;
- riscos;
- próxima ação/validação manual.
