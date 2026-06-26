---
name: immersive-framework-package-implementation
description: Implementação assertiva e segura em Unity packages do Immersive Framework: package.json, asmdefs, runtime puro, Unity adapters, docs de boundary e validação manual.
---

# Immersive Framework Package Implementation

## Objetivo

Implementar cortes em packages do Immersive Framework preservando boundaries de package, asmdefs e separação runtime puro/Unity adapter/Editor.

## Antes de editar

Leia quando existir:

- `package.json`;
- asmdefs envolvidos;
- `README.md`;
- `Documentation~/...-Boundary.md`;
- arquivos C# afetados.

Identifique:

- package owner;
- assembly owner;
- se é runtime puro, Unity adapter, Editor ou Authoring;
- se há package congelado que não deveria ser alterado;
- se há referência antiga/Base 2.0 apenas como inspiração.

## Regras de implementação

- Entregar o corte completo dentro da fronteira pedida.
- Não criar runtime/lifecycle de framework em package técnico.
- Não criar singleton/global/bootstrap/config global sem pedido explícito.
- Não criar service locator.
- Não criar fallback silencioso.
- Não copiar código antigo sem auditoria e decisão explícita.
- Não instalar packages por path local absoluto.
- Não editar `Packages/manifest.json` salvo pedido explícito.
- Não alterar package congelado salvo pedido explícito.

## Asmdef rules

- Runtime puro: `noEngineReferences: true`.
- Unity adapter: assembly separado, `noEngineReferences: false`, referencia runtime puro.
- Editor assembly: `includePlatforms: ["Editor"]`, referencia runtime/Unity quando necessário.
- Não adicionar referências extras sem necessidade.

## Package skeleton mínimo

Quando criar package:

- `package.json`;
- `README.md`;
- `Runtime/<Package>.Runtime.asmdef`;
- `Editor/<Package>.Editor.asmdef` quando houver Editor;
- `Documentation~/...-Boundary.md`;
- `Tests/Runtime` e `Tests/Editor` quando solicitado ou padrão do pacote;
- pastas planejadas sem código se o corte for skeleton.

## Git/UPM

- Se o corte envolve instalação/release, usar URLs Git tagueadas quando possível.
- Não assumir autenticação GitHub; reportar como validação manual.
- Não criar tag/remote/push salvo pedido explícito.

## Validação

- Não rodar Unity build, tests, playmode, smoke ou batchmode.
- Pode rodar checks textuais/estáticos não-Unity quando seguros.
- Não declarar PASS sem confirmação do usuário.
- Reportar `PENDING UNITY COMPILE/IMPORT VALIDATION` quando aplicável.

## Output

1. Arquivos criados/alterados/removidos.
2. Resumo do corte.
3. Package/assembly boundary preservado.
4. O que explicitamente não foi criado/copiadomigrado.
5. Validação realizada e não realizada.
6. Validação manual necessária.
7. Riscos restantes.
8. Impacto SOLID/boundary.
